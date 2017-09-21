#!/usr/bin/python

import sys

import pickle
import psycopg2
import psycopg2.extras
import argparse

#reload connect info from
fil_con = open(r'data/connect_info.ecp', 'rb')
dic_con = pickle.load(fil_con)
fil_con.close()

# hardcoded vales
host = "c1400067"
user = "mahvi"
dbnam = "pgv"
schem = "temp_mahvi"
table = "dar_adr"

# overwrite with arguments from the command line
parser = argparse.ArgumentParser(description='Connect to a data base')
parser.add_argument('--host', help='the host name, e.g. localhost')
parser.add_argument('--user', help='the user name')
parser.add_argument('--db', help='the database name')
parser.add_argument('--sch', help='the schema name')
parser.add_argument('--tab', help='the table name')

args = parser.parse_args()
print(args)
if args.host:
    host = args.host
if args.user:
    user = args.user
if args.db:
    dbnam = args.db
if args.sch:
    schem = args.sch
if args.tab:
    table = args.tab

pasw = dic_con[host][user]["pw"]

def main():
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host,dbnam,user,pasw)
    try:
        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        num_error = 101
        print "Error {} : psycopg2.connect({})\n{}".format(num_error, conn_string, e)
        sys.exit(num_error)

    # HERE IS THE IMPORTANT PART, by specifying a name for the cursor
    # psycopg2 creates a server-side cursor, which prevents all of the
    # records from being downloaded at once from the server.
    try:
        cursor = conn.cursor('cursor_unique_name', cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM {}.{} LIMIT 3".format(schem,table))
    except psycopg2.ProgrammingError as e:
        print "Can't fetch curser..."
        print e
        sys.exit(102)

    for row in cursor:
        print "{}".format(row)

if __name__ == "__main__":

    #print psycopg2.__version__
    #print psycopg2.__libpq_version__

    main()