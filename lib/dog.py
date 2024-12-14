
from sqlalchemy import create_engine
from models import Dog

create_engine = create_engine('sqlite:///:memory:')
def create_table(base):
    sql = '''
        CREATE TABLE IF NOT EXISTS dogs(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        breed TEXT NOT NULL
        );
    
        '''

def save(session, dog):
    pass

def get_all(session):
    pass

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    pass