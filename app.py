from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Creating the Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname='engagement',
        user='postgres',  # Your PostgreSQL username
        password='User name ',  # Your PostgreSQL password
        host='localhost'
    )
    return conn

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO engagement_post (tenant_id, title, content_url) VALUES (%s, %s, %s) RETURNING id',
                (data['tenant_id'], data['title'], data['content_url']))
    post_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Post created successfully!', 'id': post_id}), 201

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO engagement_post_product (product_name, product_image, sku_number) VALUES (%s, %s, %s) RETURNING id',
                (data['product_name'], data['product_image'], data['sku_number']))
    product_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Product created successfully!', 'id': product_id}), 201

@app.route('/collections', methods=['POST'])
def create_collection():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO collection (collection_name) VALUES (%s) RETURNING id', (data['collection_name'],))
    collection_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Collection created successfully!', 'id': collection_id}), 201

@app.route('/map_product', methods=['POST'])
def map_product_to_post():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO engagement_post_product_mapping (post_id, product_id) VALUES (%s, %s) RETURNING id',
                (data['post_id'], data['product_id']))
    mapping_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Product mapped to post successfully!', 'id': mapping_id}), 201

@app.route('/top_posts/<int:tenant_id>', methods=['GET'])
def top_posts(tenant_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM engagement_post WHERE tenant_id = %s ORDER BY views DESC LIMIT 5', (tenant_id,))
    posts = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(posts)

@app.route('/top_products/<int:tenant_id>', methods=['GET'])
def top_products(tenant_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT product_name, SUM(duration_in_seconds) / 3600 as duration_watched '
                'FROM engagement_post_product_mapping '
                'JOIN engagement_post ON engagement_post.id = engagement_post_product_mapping.post_id '
                'WHERE tenant_id = %s GROUP BY product_name ORDER BY SUM(duration_in_seconds) DESC LIMIT 5', (tenant_id,))
    products = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
