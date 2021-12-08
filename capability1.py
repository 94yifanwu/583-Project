import config
import sqlite_utils
import sqlite3
import knowledge_base

def cap_1(your_age,your_genres,your_language):
    result = knowledge_base.kb(your_age,your_genres,your_language)  
    return result