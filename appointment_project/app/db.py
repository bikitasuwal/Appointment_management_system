import psycopg2
def get_connection():
  return psycopg2.connect(
      host="localhost",
      user="postgres",
      password="bikita",
      database="automationdb",
      port="5432"
  )
def create_table():
  conn = get_connection()
  cur = conn.cursor()
  cur.execute("""
              create table if not exists appointments (id serial primary key,
              name varchar(255),
              date date,
                  time time,
                  reason varchar(255));""")
  conn.commit()
  cur.close()
  conn.close()
