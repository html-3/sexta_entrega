from app import create_app

app=create_app()

if __name__=="__main__":
    app.run(debug=True)

# app nao roda
# RuntimeError: No application found. Either work inside a view function or push an application context.
# db.relationship nao funciona
# api provavelmente nao vao rodar
# opcoes para deletar deletam todos os objetos, nao um específico
# qualquer usuário pode editar a loja
# ilegível
# desrespeita DRY