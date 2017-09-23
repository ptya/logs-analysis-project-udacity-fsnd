#!/usr/bin/env python3
# -*- coding: latin-1 -*-

import psycopg2
import datetime
import time
import sys

START_TIME = time.time()
DBNAME = "news"

def connect_db(db_name=DBNAME):
    """Return connection to database and cursor."""
    try:
        conn = psycopg2.connect(database=DBNAME)
        c = conn.cursor()
        return conn, c
except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit()


def top_3_articles():
    """Return the top 3 articles, most viewed first."""
    conn, c = connect_db()
    query = """
            SELECT title, count(path)::integer as views
            FROM articles, log
            WHERE path = '/article/' || slug
            AND status LIKE ('200%')
            GROUP BY title
            ORDER BY views DESC
            LIMIT 3
            """
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return result


def popular_authors():
    """Return the most popular authors, most viewed first."""
    conn, c = connect_db()
    query = """
        SELECT authors.name, count(log.path)::integer as views
        FROM authors, articles, log
        WHERE log.path LIKE CONCAT('%', articles.slug, '%')
              AND status LIKE ('200%')
              AND authors.id = articles.author
        GROUP BY authors.name
        ORDER BY views DESC
        """
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return result


def error_days():
    """Return the days where error request count was above 1%."""
    conn, c = connect_db()
    query = """
        SELECT day, errors/total AS percentage
        FROM (SELECT time::date AS day,
                     COUNT(status) AS total,
                     SUM((status NOT LIKE '%200%')::int)::float AS errors
              FROM log
              GROUP BY day) AS pretable
        WHERE errors/total > 0.01
        """
    c.execute(query)
    result = c.fetchall()
    conn.close()
    return result


# Welcome message
print('\n## Fetching data. Please wait.. ##')

# 1 - Print top 3 articles
# Output example:
# "Princess Shellfish Marries Prince Handsome" - 1201 views
hdr1 = """
#############################
#  The top 3 articles are:  #
#############################
"""
msg1 = top_3_articles()
print(hdr1)
for article, views in msg1:
    print('"' + article + '" — ' + '{:,}'.format(views) + ' views')

# 2 - Most popular authors
# Output example:
# Ursula La Multa — 2304 views
hdr2 = """
##################################
#  The most popular actors are:  #
##################################
"""
msg2 = popular_authors()
print(hdr2)
for author, views in msg2:
    print(author + ' — ' + '{:,}'.format(views) + ' views')

# 3 - Days above 1% request errors
# Output example:
# July 29, 2016 — 2.5% errors
hdr3 = """
###################################
#  Days above 1% request errors:  #
###################################
"""
msg3 = error_days()
print(hdr3)
for day, percent in msg3:
    print(day.strftime("%B %d, %Y") + ' — ' + '{:.2%}'.format(percent))

print('\n## End of program — runtime: %s seconds ##\n' %
      round((time.time() - START_TIME), 2))
