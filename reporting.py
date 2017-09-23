#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import psycopg2
import datetime
import time

def connect_db(db_name='news'):
    """Return connection to database and cursor.

        args:
            db_name - name of the database, default 'news'

        returns:
            Database connection
            Cursor to the database
    """
    try:
        conn = psycopg2.connect(database=db_name)
        c = conn.cursor()
        return conn, c
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def execute_query(query):
    """Takes an SQL query and returns as a list of tuples.

        args:
            query - an SQL query statement to be executed.

        returns:
            A list of tuples containing the results of the query.
    """
    try:
        conn, c = connect_db()
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def main():
    START_TIME = time.time()

    # Welcome message
    print('\n## Fetching data. Please wait.. ##')

    # 1 - Print top 3 articles, most viewed first.
    # Output example:
    # "Princess Shellfish Marries Prince Handsome" - 1201 views
    # SQL query
    query1 = """
    SELECT title, views
    FROM articles
    INNER JOIN
    (SELECT path, count(path)::integer AS views
    FROM log
    GROUP BY path) AS log
    ON path = '/article/' || slug
    ORDER BY views DESC
    LIMIT 3
    """

    # Fetch rows
    msg1 = execute_query(query1)

    # Print header
    hdr1 = """
    #############################
    #  The top 3 articles are:  #
    #############################
    """
    print(hdr1)

    # Print results
    for article, views in msg1:
        print('{0} — {1:,} views'.format(article, views))

    # 2 - Most popular authors, most viewed first.
    # Output example:
    # Ursula La Multa — 2304 views
    # SQL query
    query2 = """
    SELECT authors.name, sum(views) AS total_views
    FROM articles
    INNER JOIN
    (SELECT path, count(path)::integer AS views
    FROM log
    GROUP BY path) AS log
    ON path = '/article/' || slug
    INNER JOIN authors
    ON authors.id = articles.author
    GROUP BY authors.name
    ORDER BY total_views DESC
    """

    # Fetch rows
    msg2 = execute_query(query2)

    # Print header
    hdr2 = """
    ##################################
    #  The most popular actors are:  #
    ##################################
    """
    print(hdr2)

    # Print results
    for author, views in msg2:
        print('{0} — {1:,} views'.format(author, views))

    # 3 - Days above 1% request errors
    # Output example:
    # July 29, 2016 — 2.5% errors
    # SQL query
    query3 = """
    SELECT day, errors/total AS percentage
    FROM (SELECT time::date AS day,
    COUNT(status) AS total,
    SUM((status NOT LIKE '%200%')::int)::float AS errors
    FROM log
    GROUP BY day) AS pretable
    WHERE errors/total > 0.01
    """

    # Fetch rows
    msg3 = execute_query(query3)

    # Print header
    hdr3 = """
    ###################################
    #  Days above 1% request errors:  #
    ###################################
    """
    print(hdr3)

    # Print results
    for day, percent in msg3:
        print('{0:%B %d, %Y} — {1:.2%}'.format(day, percent))

    # Goodby message
    print('\n## End of program — runtime: %s seconds ##\n' %
          round((time.time() - START_TIME), 2))


if __name__ == '__main__':
    main()
