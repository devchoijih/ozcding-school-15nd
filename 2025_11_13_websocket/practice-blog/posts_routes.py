from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from model import PostSchema

def create_posts_blueprint(mysql):

    blp = Blueprint("Posts", "posts", url_prefix="/posts", description="Posts API")

    @blp.route("/")
    class PostsList(MethodView):
        @blp.response(200, PostSchema(many=True))
        def get(self):
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM posts")
            rows = cursor.fetchall()
            cursor.close()

            posts = [
                {"id": r[0], "title": r[1], "content": r[2]}
                for r in rows
            ]
            return posts

        @blp.arguments(PostSchema)
        @blp.response(201, PostSchema)
        def post(self, new_post):
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (new_post["title"], new_post["content"]))
            mysql.connection.commit()

    @blp.route("/<int:post_id>")
    class PostsDetail(MethodView):
        @blp.response(200, PostSchema)
        def get(self, post_id):
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM posts WHERE id=%s", (post_id,))
            row = cursor.fetchone()
            cursor.close()

            return jsonify({"id": row[0], "title": row[1], "content": row[2]})

        @blp.arguments(PostSchema)
        @blp.response(200, PostSchema)
        def put(self, update_data, post_id):
            cursor = mysql.connection.cursor()
            query = """ 
                    UPDATE posts 
                       SET title = %s,
                           content = %s 
                     WHERE id = %s 
                    """
            cursor.execute(query, (update_data["title"], update_data["content"], post_id))
            mysql.connection.commit()
            cursor.close()
            return ''

        @blp.response(204)
        def delete(self, post_id):
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM posts WHERE id=%s", (post_id,))
            mysql.connection.commit()
            return ''

    return blp