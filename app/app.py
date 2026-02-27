"""
NEOLAF Vibe Coding Bootcamp — Week 3: Legacy System
WARNING: This application contains INTENTIONAL security vulnerabilities for educational purposes.
DO NOT deploy to production without completing the Week 3 security refactoring.

Intentional issues include:
- SQL injection vulnerability in search
- Hardcoded credentials
- Missing CSRF protection
- Insecure direct object references
- No rate limiting
- N+1 query pattern
- Missing error handling
- Business logic mixed with routes
"""

from flask import Flask, request, jsonify, render_template, session
import sqlite3
import hashlib

app = Flask(__name__)
# VULNERABILITY: Hardcoded secret key
app.secret_key = "super_secret_key_123"

# VULNERABILITY: Hardcoded database credentials
DB_PATH = "blog.db"
ADMIN_PASSWORD = "admin123"  # Never do this in real code


def get_db():
    """Get database connection - no connection pooling, no error handling."""
    return sqlite3.connect(DB_PATH)


@app.route("/search")
def search():
    """
    VULNERABILITY: SQL Injection
    The query parameter is directly interpolated into the SQL query.
    
    Example attack: /search?q=' OR '1'='1
    """
    query = request.args.get("q", "")
    db = get_db()
    cursor = db.cursor()
    # VULNERABILITY: Direct string interpolation - SQL injection possible
    results = cursor.execute(
        f"SELECT * FROM posts WHERE title LIKE '%{query}%'"
    ).fetchall()
    return jsonify(results)


@app.route("/posts")
def get_posts():
    """
    PERFORMANCE ISSUE: N+1 query pattern
    Fetches all posts, then makes a separate query for each post's author.
    """
    db = get_db()
    posts = db.execute("SELECT * FROM posts").fetchall()
    
    result = []
    for post in posts:
        # N+1: One query per post to get author
        author = db.execute(
            f"SELECT * FROM users WHERE id = {post[2]}"
        ).fetchone()
        result.append({
            "id": post[0],
            "title": post[1],
            "author": author[1] if author else "Unknown"
        })
    
    return jsonify(result)


@app.route("/post/<post_id>")
def get_post(post_id):
    """
    VULNERABILITY: Insecure Direct Object Reference (IDOR)
    No authorization check - any user can access any post by ID.
    """
    db = get_db()
    # No check if the requesting user has permission to view this post
    post = db.execute(f"SELECT * FROM posts WHERE id = {post_id}").fetchone()
    if not post:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"id": post[0], "title": post[1], "content": post[3]})


@app.route("/login", methods=["POST"])
def login():
    """
    VULNERABILITY: No rate limiting, weak password hashing, timing attack possible.
    VULNERABILITY: Missing CSRF protection.
    """
    username = request.form.get("username")
    password = request.form.get("password")
    
    # VULNERABILITY: MD5 is cryptographically broken
    password_hash = hashlib.md5(password.encode()).hexdigest()
    
    db = get_db()
    user = db.execute(
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password_hash}'"
    ).fetchone()
    
    if user:
        session["user_id"] = user[0]
        return jsonify({"success": True})
    
    return jsonify({"success": False}), 401


@app.route("/admin")
def admin():
    """
    VULNERABILITY: Weak authorization check.
    Only checks if user_id is in session, not if they have admin role.
    """
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    # VULNERABILITY: Any logged-in user can access admin panel
    db = get_db()
    all_users = db.execute("SELECT * FROM users").fetchall()
    return jsonify(all_users)


if __name__ == "__main__":
    # VULNERABILITY: Debug mode enabled in production
    app.run(debug=True, host="0.0.0.0")
