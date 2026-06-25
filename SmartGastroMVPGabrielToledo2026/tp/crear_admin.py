from app import app
from models import db, Usuario
from werkzeug.security import generate_password_hash


with app.app_context():

    email_admin = "admin@smartgastro.com"

    usuario_existente = Usuario.query.filter_by(email=email_admin).first()

    if usuario_existente:
        print("El usuario admin ya existe.")
    else:
        admin = Usuario(
            nombre="Administrador",
            email=email_admin,
            password_hash=generate_password_hash("admin123")
        )

        db.session.add(admin)
        db.session.commit()

        print("Usuario admin creado correctamente.")