from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

usuarios = []
chamados = []

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

@app.get("/")
def home():
    return {
        "mensagem": "API funcionando"
    }

@app.post("/register")
def cadastrar(usuario: Usuario):

    usuarios.append(usuario.dict())

    return {
        "mensagem": "Usuário cadastrado"
    }

@app.get("/users")
def listar_usuarios():
    return usuarios

@app.post("/login")
def login(email: str, senha: str):

    for usuario in usuarios:

        if usuario["email"] == email and usuario["senha"] == senha:
            return {
                "mensagem": "Login realizado com sucesso"
            }

    return {
        "mensagem": "Email ou senha inválidos"
    }


class Chamado(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str

@app.post("/tickets")
def criar_chamado(chamado: Chamado):

    chamados.append(chamado.dict())

    return {
        "mensagem": "Chamado criado com sucesso"
    }




@app.get("/tickets")
def listar_chamados():
    return chamados



@app.get("/tickets/{id}")
def buscar_chamado(id: int):

    for chamado in chamados:

        if chamado["id"] == id:
            return chamado

    return {
        "erro": "Chamado não encontrado"
    }

@app.put("/tickets/{id}")
def atualizar_chamado(id: int, novo_chamado: Chamado):

    for i, chamado in enumerate(chamados):

        if chamado["id"] == id:

            chamados[i] = novo_chamado.dict()

            return {
                "mensagem": "Chamado atualizado com sucesso"
            }

    return {
        "erro": "Chamado não encontrado"
    }

@app.patch("/tickets/{id}/status")
def alterar_status(id: int, status: str):

    for chamado in chamados:

        if chamado["id"] == id:

            chamado["status"] = status

            return {
                "mensagem": "Status atualizado com sucesso"
            }

    return {
        "erro": "Chamado não encontrado"
    }

@app.delete("/tickets/{id}")
def excluir_chamado(id: int):

    for chamado in chamados:

        if chamado["id"] == id:

            chamados.remove(chamado)

            return {
                "mensagem": "Chamado removido com sucesso"
            }

    return {
        "erro": "Chamado não encontrado"
    }


    