import sqlite3
from loguru import logger

class Db:
    def __init__(self):
        self.sqlite_connection = sqlite3.connect('database.db')
        self.cursor = self.sqlite_connection.cursor()


    def create_db_community(self):
        try:
            #self.sqlite_connection.set_trace_callback(logger.debug)
            sqlite_create_table_query = '''CREATE TABLE community (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        have_pet text NOT NULL,
                                        love_pet text NOT NULL);'''
            self.cursor.execute(sqlite_create_table_query)
            self.sqlite_connection.commit()
            logger.debug("Таблица SQLite создана")
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    def create_db_community_v2(self):
        try:
            #self.sqlite_connection.set_trace_callback(logger.debug)
            sqlite_create_table_query = '''CREATE TABLE community_v2 (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        have_child text NOT NULL,
                                        love_child text NOT NULL);'''
            self.cursor.execute(sqlite_create_table_query)
            self.sqlite_connection.commit()
            logger.debug("Таблица SQLite создана")
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    def drop_table(self, table):
        try:            
            drop_table = f"""DROP TABLE {table} ;"""
            self.cursor.execute(drop_table)
            logger.debug(f"Таблица {table} удалена")
            
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    def insert_into_community(self, have_pet, love_pet):
        try:   
            #self.sqlite_connection.set_trace_callback(logger.debug)
            insert_into = """INSERT INTO 'community' (have_pet, love_pet)
VALUES (:have_pet, :love_pet) ;"""
            self.cursor.execute(insert_into,{"have_pet": have_pet, "love_pet": love_pet})
            self.sqlite_connection.commit()
            
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    def insert_into_community_v2(self, have_child, love_child):
        try:   
            #self.sqlite_connection.set_trace_callback(logger.debug)
            insert_into = """INSERT INTO 'community_v2' (have_child, love_child)
VALUES (:have_child, :love_child) ;"""
            self.cursor.execute(insert_into,{"have_child": have_child, "love_child": love_child})
            self.sqlite_connection.commit()
            
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    def select_all_from_table(self, table):
        try:        
            #self.sqlite_connection.set_trace_callback(logger.debug)
            sqlite_select_query = f"""SELECT * from {table} ;"""
            self.cursor.execute(sqlite_select_query)
            rows = self.cursor.fetchall()
            #logger.debug(rows)
            return rows
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
            
    def select_join_from_table(self):
        try:        
            #self.sqlite_connection.set_trace_callback(logger.debug)
            sqlite_select_query = """SELECT community.id, community.have_pet, community_v2.have_child from community 
INNER JOIN community_v2 ON 
(community.love_pet=community_v2.love_child)AND(community.id=community_v2.id) 
order by community.have_pet desc, community_v2.have_child desc;"""
            self.cursor.execute(sqlite_select_query)
            rows = self.cursor.fetchall()
            #logger.debug(rows)
            return rows
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
            
    def select_where_from_table(self, table, column, value):
        try:   
            self.sqlite_connection.set_trace_callback(logger.debug)
            sqlite_select_query = f"""SELECT * from {table} WHERE {column}= :value;"""
            self.cursor.execute(sqlite_select_query,{"value": value})
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as error:
            logger.error(f"Ошибка при подключении к sqlite {error}")
            
    
            

