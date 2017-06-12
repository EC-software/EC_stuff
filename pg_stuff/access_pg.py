#!/usr/bin/python

import sys

import pickle
import psycopg2
import psycopg2.extras

#reload connect info from
fil_con = open(r'data/connect_info.ecp', 'rb')
dic_con = pickle.load(fil_con)
fil_con.close()

host = "localhost"
user = "martin"
pasw = dic_con[host][user]["pw"]
dbnam = "martin"
schem = "test"
table = "dkn10_add_dens"

def main():
    # Define our connection string
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host,dbnam,user,pasw)
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
    except:
        num_error = 101
        print "Error {} : psycopg2.connect({})".format(num_error, conn_string)
        sys.exit(num_error)

    # HERE IS THE IMPORTANT PART, by specifying a name for the cursor
    # psycopg2 creates a server-side cursor, which prevents all of the
    # records from being downloaded at once from the server.
    cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM {}.{} LIMIT 10".format(schem,table))

    for row in cursor:
        print "{}".format(row)

if __name__ == "__main__":

    print psycopg2.__version__
    print psycopg2.__libpq_version__

    main()