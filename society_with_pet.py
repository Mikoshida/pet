import random
from sqlite import Db
from loguru import logger
from exceptions import Incorrect_data


class BaesAnalitics():
    def __init__(self,metrics_dict):
        for probability in metrics_dict.values():
            logger.debug(probability)
            if probability >1 or probability <0:
                raise Incorrect_data("Невозможное значение вероятности")
        self.probability_a = metrics_dict["a"]
        self.probability_b_where_a_istrue = metrics_dict["b_a_true"]
        self.probability_b_where_a_isfalse = metrics_dict["b_a_false"]
        self.rate_a = metrics_dict.get("rate_a",0.5) 
        self.probability_b = self.rate_a * self.probability_b_where_a_istrue + (1-self.rate_a)*self.probability_b_where_a_isfalse
        self.local_community = []
        self.db = Db()
        

    def calculations(self):
        self.probability_a_where_b_istrue = (self.probability_b_where_a_istrue*self.probability_a)/self.probability_b
        if self.probability_a_where_b_istrue<=1:
            logger.debug(self.probability_a_where_b_istrue)
        else:
            raise Incorrect_data("Невозможное значение вероятности")
        
        
    def generate_community(self,population):
        for i in range(population):
            love_pet = 1 if random.random()<self.probability_a else 0
            if love_pet:
                have_pet = 1 if random.random()<self.probability_b_where_a_istrue else 0
            else:
                have_pet = 1 if random.random()<self.probability_b_where_a_isfalse else 0
            self.local_community.append({"love_pet":love_pet,"have_pet":have_pet})  #пополняем локальное сообщество любителей животных
            self.db.insert_into_community(have_pet,love_pet)   #пополняем глобальную выборку
        logger.debug(self.local_community)
        #self.db.select_all_from_table("community")
        
    
    
    def analyze_community(self,a,b):
        try:
            pet_lovers=list(filter(lambda human: human[a] == 1, self.local_community))
            pet_owners=list(filter(lambda human: human[b] == 1, self.local_community))
            pet_owners_with_love=self.local_community.count({a: 1, b: 1})
            pet_owners_without_love=self.local_community.count({a: 0, b: 1})
            logger.debug(f"pet_lovers={len(pet_lovers)}, pet_owners={len(pet_owners)}, pet_owners_with_love={pet_owners_with_love},"+ 
                  f"pet_owners_without_love={pet_owners_without_love}")
        except Exception as e:
            logger.error(f"ошибка: {e}")
    
    def analyze_global_community(self,table,a,b):
        try:
            global_community = self.db.select_all_from_table(table)
            logger.debug(f"global_community={len(global_community)}")
            community_a = self.db.select_where_from_table(table,a,1)
            community_b = self.db.select_where_from_table(table,b,1)
            probability_a=len(community_a)/len(global_community)
            probability_b=len(community_b)/len(global_community)
            probability_b_where_a_istrue = len(list(filter(lambda human: human[1] == "1", community_a)))/len(community_a)
            probability_a_where_b_istrue = (probability_b_where_a_istrue*probability_a)/probability_b
            logger.debug(f"""Итого в нашем сообществе {len(global_community)} людей,
из них {probability_a*100}% {a},
{probability_b*100}% {b},
{probability_b_where_a_istrue*100}% {a} и {b},                    
и вероятность, что случайный человек {b} попадает в {a} составляет={probability_a_where_b_istrue*100}%""")
        except Exception as e:
            logger.error(f"ошибка: {e}")

        
 