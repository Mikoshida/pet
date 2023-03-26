from society_with_children import BaesAnalitics_lvl2
from society_with_pet import BaesAnalitics
from exceptions import Incorrect_data
from loguru import logger
from sqlite import Db


def main(population):
    try:
        obj = BaesAnalitics({"a":0.7,"b_a_true":0.3,"b_a_false":0.3,"rate_a":0.5})
        obj.calculations()
        obj.generate_community(population)
        obj.analyze_community("love_pet","have_pet")
        obj.analyze_global_community("community","love_pet","have_pet")
        
        obj1 = BaesAnalitics_lvl2({"a":0.7,"b_a_true":0.3,"b_a_false":0.3,"rate_a":0.5})
        obj1.calculations()
        obj1.generate_community(population)
        obj1.analyze_community("love_child","have_child")
        obj1.analyze_global_community("community_v2","love_child","have_child")
        
        obj1.join_table_lovers()
        
    except Incorrect_data as e:
        logger.error(f"ошибка: {e}")

def boom_and_new_community():
    obj = Db()
    obj.drop_table("community")
    obj.drop_table("community_v2")
    obj.create_db_community()
    obj.create_db_community_v2()

    
#boom_and_new_community()
if __name__ == '__main__':        
    main(100)   