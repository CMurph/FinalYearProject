import psycopg2 as dbapi
import time
import datetime


db_connection = dbapi.connect(database='FYP', user="ciaran")
db_cursor = db_connection.cursor()

class db_manager:
    def __init__(self):
        print("init")

    def get_tweet_max(self):
        try:
            db_cursor.execute("SELECT MAX(tweet_id) FROM tweets;")  # get the lowest value tweet in database
            db_max = db_cursor.fetchone()[0]
            return db_max
        except:
            return 0


    def get_tweet_min(self):
        db_cursor.execute("SELECT MIN(tweet_id) FROM tweets;")  # get the lowest value tweet in database
        db_min = db_cursor.fetchone()[0]
        return db_min


    def get_location(self, text):
        text = text.lower().replace('rd', 'road')
        text = text.lower().replace('st.', 'street')
        key_words = ["accident", "crash", "collision", "incident"]

        db_cursor.execute("select distinct lower(name) from location_names;")
        names = db_cursor.fetchall()
        locations = [name[0] for name in names]

        if (any(word in text.lower() for word in key_words)):

            # if(any(word in text.lower() for word in table)):
            for place in locations:
                if (place in text.lower()):
                    return place
        #if not an accident or place not documented place is none
        return None

    def collision_insert(self, timestamp, location):
        old = timestamp + datetime.timedelta(minutes=-15)
        new = timestamp + datetime.timedelta(minutes=15)
        try:
            db_cursor.execute("SELECT collision_id FROM collisions WHERE location_name like %s AND timestamp BETWEEN %s AND %s ;", (location.lower(), old, new))  # get the lowest value tweet in database
            print(db_cursor.rowcount)
            if (db_cursor.rowcount == 0):
                    db_cursor.execute("INSERT INTO collisions(location_name, TIMESTAMP ) values(%s, %s);",(location.lower(), timestamp))
                    db_connection.commit()
                    db_cursor.execute("SELECT collision_id FROM collisions where location_name like %s AND timestamp BETWEEN %s AND %s ;",(location.lower, old, new))  # get the lowest value tweet in database
                    collision_id = db_cursor.fetchone()[0]

            else:
                collision_id = db_cursor.fetchone()[0]
        except dbapi.DatabaseError as ex:
            db_connection.rollback()
            print(str(ex))
            return None

        print(collision_id)
        return collision_id

    def tweet_insert(self, tweet_id, collision_id, user_id,  text):
        try:
            db_cursor.execute("Insert into tweets(tweet_id, collision_id, user_id, text) values (%s,%s, %s, %s);",(tweet_id, collision_id, user_id, text))
            db_connection.commit()
            print("Tweet: " + str(tweet_id) + " Inserted")

        except dbapi.DatabaseError as ex:
            print("Error In Tweet insert")
            db_connection.rollback()
            print(str(ex))



    def db_insert(self, status):
        tweet_id = status.id_str
        timestamp = status.created_at
        user_id = status.user.id_str
        location = self.get_location(status.text.lower())
        text = status.text.lower()

        if (location is None):
            print("Location is none")
        else:
           collision_id = self.collision_insert(timestamp, location)
           self.tweet_insert(tweet_id, collision_id, user_id, text)



