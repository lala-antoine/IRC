import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


# Table d'association Many‑to‑Many entre utilisateurs et rôles
role_utilisateur = db.Table(
    "role_utilisateur",
    db.Column("utilisateur_pseudo", db.String(100), db.ForeignKey("utilisateur.pseudo"), primary_key=True),
    db.Column("role_nom", db.String(50), db.ForeignKey("role.nom"), primary_key=True),
)


class Role(db.Model):
    """Représente un rôle métier attribuable à un utilisateur."""

    __tablename__ = "role"

    nom = db.Column(db.String(100), primary_key=True)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Role {self.nom}>"


class Utilisateur(db.Model):
    """Modèle principal répondant au besoin :
    {
        "pseudo": "string",
        "email": "string",
        "statut": "string",       # Enum
        "derAct": "int",          # timestamp
        "roles": ["string"],      # liste de rôles
        "avatar": "string"        # url
    }
    """

    __tablename__ = "utilisateur"

    pseudo = db.Column(db.String(100), primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)
    statut = db.Column(db.String(100), nullable=False, default="actif")
    derAct = db.Column(db.Integer, nullable=False, default=int(time.time()))
    avatar = db.Column(db.String(255), nullable=True)

    # Relation many‑to‑many avec Role
    roles = db.relationship(
        "Role",
        secondary=role_utilisateur,
        lazy="joined",
        backref=db.backref("utilisateurs", lazy="selectin"),
    )

    @validates("statut")
    def _valide_statut(self, key, value):
        if value not in {"actif", "inactif", "banni"}:
            raise ValueError("Statut invalide")
        return value
