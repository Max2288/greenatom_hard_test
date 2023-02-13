"""Create and fill databases."""
import os
import psycopg2
import logging


logger = logging.getLogger("main")
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def init_database():
    """Database initialization."""
    with psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT) as con:
        cur = con.cursor()
        cur.execute(open("init.sql", "r").read())
        logger.info("Database was successfully created.")


def set_missions(mission_id: str, name: str) -> str:
    """Fill missions table.

    Args:
        mission_id (str): mission's id.
        name (str): mission's name.

    Returns:
        str: mission's id.
    """
    with psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT) as con:
        cur = con.cursor()
        cur.execute(
            "INSERT INTO missions (id, name) values ('{0}','{1}') RETURNING id;".format(mission_id, name))
        return cur.fetchone()[0]


def set_rockets(name: str, type: str, county: str, costs: int) -> int:
    """Fill rockets table.

    Args:
        name (str): rocket's name.
        type (str): rocket's type.
        county (str): rocket's country.
        costs (int): price of the launch.

    Returns:
        int: rocket's id.
    """
    with psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT) as con:
        cur = con.cursor()
        cur.execute(
            "SELECT id FROM rockets WHERE name='{0}' and type='{1}';".format(name, type))
        rocket_id = cur.fetchone()
        if rocket_id:
            return rocket_id[0]
        cur.execute(
            "INSERT INTO rockets (name, type, country, cost_per_launch) values ('{0}','{1}','{2}',{3}) RETURNING id;".format(
                name, type, county, costs))
        return cur.fetchone()[0]


def set_launches(rocket_id: int, mission_id: str) -> None:
    """Fill launches table.

    Args:
        rocket_id (int): rocket's id.
        mission_id (str): mission's id.
    """
    with psycopg2.connect(
            database=DATABASE,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT) as con:
        cur = con.cursor()
        if rocket_id == None:
            cur.execute("SELECT id from rockets;")
            rocket_id = cur.fetchall()[-1][0]
        if mission_id == None:
            cur.execute("SELECT id from missions;")
            mission_id = cur.fetchall()[-1][0]
        cur.execute("INSERT INTO launches (rocket_id, mission_id) values ({0},'{1}');".format(
            rocket_id, mission_id))
