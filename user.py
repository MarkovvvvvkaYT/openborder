import sqlite3

from config import db_name


def create_table():
    """Create the small user-role table used by the bot."""
    with sqlite3.connect(db_name) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                role TEXT
            )
            """
        )


class User:
    @staticmethod
    def add_user(user_id):
        with sqlite3.connect(db_name) as connection:
            connection.execute("INSERT OR IGNORE INTO user (id) VALUES (?)", (user_id,))

    @staticmethod
    def add_role_to_user(user_id, role):
        with sqlite3.connect(db_name) as connection:
            connection.execute(
                "UPDATE user SET role = ? WHERE id = ?",
                (role, user_id),
            )

    @staticmethod
    def get_role_by_id(user_id):
        with sqlite3.connect(db_name) as connection:
            row = connection.execute(
                "SELECT role FROM user WHERE id = ?",
                (user_id,),
            ).fetchone()
        return row[0] if row else None