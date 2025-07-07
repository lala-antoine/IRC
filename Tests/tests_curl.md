# Appels curl

Pour chaques commandes on a :
- L'objectif de la commande derrière le ## 
- La méthode HTTP (POST, GET, DELETE, etc) 
- La commande curl avec les options à renseigner (-H pour le header et -d pour les données)

## Créer un compte utilisateur : 

```
curl -X POST http://localhost:5001/register \
-H "Content-Type: application/json" \
-d '{
  "pseudo": "roger",
  "email": "roger@canaduck.com",
  "password": "mdp_roger" }'
  ```

## Se connecter puis récupérer un token :

```
curl -X POST http://localhost:5001/login \
-H "Content-Type: application/json" \
-d '{
  "pseudo": "roger",
  "password": "motdepasse123"
}'
```


## Voir les infos publiques d’un utilisateur : 

```
curl -X GET http://localhost:5001/whois/roger
```

## Vérifier qui est en ligne :
```
curl -X GET "http://localhost:5001/ison?users=roger,ginette"
```

## Dernière activité d’un utilisateur : 
```
curl -X GET http://localhost:5001/seen/roger
```

## Changer de statut :
```
curl -X POST http://localhost:5001/user/status \
-H "Authorization: Bearer LE_TOKEN" \
-H "Content-Type: application/json" \
-d '{"status": "away"}'
```

## Changer le mot de passe
```
curl -X PATCH http://localhost:5001/user/roger/password \
-H "Authorization: Bearer LE_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "old_password": "ancienmdp",
  "new_password": "nouveaumdp"
}'
```

## Récupérer l’avatar d’un user
```
curl -X GET http://localhost:5001/user/avatar/roger
```

## Supprimer un utilisateur 
```
curl -X DELETE http://localhost:5001/user/roger \
-H "Authorization: Bearer VOTRE_TOKEN_ICI"
```

## Récupérer les rôles d’un utilisateur
```
curl -X GET http://localhost:5001/user/roles/roger
```

## Ajouter un rôle à un utilisateur 
```
curl -X POST http://localhost:5001/user/roles/roger \
-H "Authorization: Bearer LE_TOKEN_ADMIN?" \
-H "Content-Type: application/json" \
-d '{"role": "admin"}'
```
