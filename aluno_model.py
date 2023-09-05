from flask import jsonify
from sqlalchemy import text
import conexao_bd

engine = conexao_bd.getConexao()

# Corrigido
def cadastrarAluno(aluno):
    nome = aluno['nome']
    email = aluno['email']
    cpf = aluno['cpf']
    data_nasc = aluno['data_nasc']
    with engine.connect() as con:    
        sql_criar = text("INSERT INTO alunos (nome, email, cpf, nascimento) VALUES  (:_meuNome, :_meuEmail, :_meuCpf, :_meuData_nasc)")
        con.execute(sql_criar, _meuNome=nome, _meuEmail=email, _meuCpf=cpf, meuData_nasc=data_nasc)


# Corrigido                    	
def getAlunos():
    with engine.connect() as con:  
        statement = text ("""SELECT * FROM alunos""") 
        rs = con.execute(statement) 
        alunos = rs.fetchall()                 
        if alunos == []:                       
            return None
        result = [dict(aluno) for aluno in alunos]
        return jsonify(result)
        
        

# Corrigido
def getAlunoId(id_aluno):
    with engine.connect() as con: 
        statement = text ("""SELECT * FROM alunos WHERE id = :id_""") 
        rs = con.execute(statement, id_=id_aluno) 
        aluno = rs.fetchone()                   
        if aluno == None:
            return None
        return dict(aluno)                  

# Corrigido
def getAlunoNome(nome_aluno):
    with engine.connect() as con:   
        statement = text ("""SELECT * FROM alunos WHERE nome = :nome_""") 
        rs = con.execute(statement, nome_=nome_aluno) 
        alunos = []
        while True:
            batch = rs.fetchmany(20)  
            if not batch:
                break  
            for aluno in batch:
                alunos.append(dict(aluno))  
    return jsonify(alunos)

    
# Corrigido
def excluirAluno(id_aluno):
    aluno = getAlunoId(id_aluno)
    if aluno == None:
        return None
    with engine.connect() as con:    
        sql = text ("DELETE FROM alunos WHERE id = :_id")
        con.execute(sql, _id=id_aluno)
    return aluno


# Corrigido
def alterarAluno(id_aluno, novos_dados):
    aluno = getAlunoId(id_aluno)
    if aluno == None:
        return None
    with engine.connect() as con: 
        sql_editar = text ("UPDATE alunos SET nome=:nome, email=:email, cpf=:cpf, data_nasc=:data_nasc WHERE id =:id_")
        con.execute(sql_editar, nome=novos_dados['nome'], email=novos_dados['email'], cpf=novos_dados['cpf'], data_nasc=novos_dados['data_nasc'], id_=id_aluno)
        return aluno