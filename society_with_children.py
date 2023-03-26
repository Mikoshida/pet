from loguru import logger
from society_with_pet import BaesAnalitics
import random

class BaesAnalitics_lvl2(BaesAnalitics):
        
    def generate_community(self,population):
        #self.db.drop_table("community_v2")
        #self.db.create_db_community_v2()
        for i in range(population):
            love_child = 1 if random.random()<self.probability_a else 0
            if love_child:
                have_child = 1 if random.random()<self.probability_b_where_a_istrue else 0
            else:
                have_child = 1 if random.random()<self.probability_b_where_a_isfalse else 0
            self.local_community.append({"love_child":love_child,"have_child":have_child})  
            self.db.insert_into_community_v2(have_child,love_child)
        logger.debug(self.local_community)
        #self.db.select_all_from_table("community_v2")
    
    def join_table_lovers(self):
        logger.debug(f"Следующие люди любят и животных и детей, также приведена информация о наличии питомца и ребенка: {self.db.select_join_from_table()}")
        
