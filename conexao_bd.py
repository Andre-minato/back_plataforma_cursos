from sqlalchemy import create_engine, text

def getConexao():
    engine = create_engine("mysql+pymysql://root:mudar123@172.19.0.2:3306/teste")
    return engine








