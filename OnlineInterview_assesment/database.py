
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker




sql_url = "mysql+pymysql://root:kamlesh#12@127.0.0.1:3306/library_database"

engine = create_engine(
    sql_url, echo_pool="debug"
)

session_local = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    except:
        db.close()