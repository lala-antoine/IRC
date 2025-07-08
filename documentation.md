# Objets

Objet **utilisateur** : 
```json
{
"pseudo" : "string",
"email" : "string",
"statut" : "string", // (enum)
"derAct" : "int", // (timestamp)
"roles" : ["string"],
"avatar" : "string" // ( url )
}
```

Objet **WhoIS** : 
```json
{
"pseudo" : "string",
"cannaux" : ["string"],
"statut" : "string", // (enum)
"derAct" : "int", // (timestamp)
"roles" : ["string"],
}
```

Clé JWT : **on-ny-arrivera-jamais-enfin-peut-etre**
```json
{
"pseudo" : "string",
"expiration" : "int", // (timestamp)
"roles" : ["string"] 
}
```

# Routes

## GET

**GET /seen**

```yaml
    Récupère la dernière activité d'un utilisateur
    ---
    produces:
      - application/json
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: Le pseudo de l'utilisateur
        example: Roger
    responses:
      200:
        description: "Dernière activité trouvée"
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            derAct:
              type: integer
              example: 1720424173210
      404:
        description: "Utilisateur inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Utilisateur inconnu"
```


**GET /Whois**
```yaml
    Récupère les informations publiques d'un utilisateur
    ---
    produces:
      - application/json
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: pseudo
        example: QuackSparrow
    responses:
      200:
        description: "Utilisateur trouvé"
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            cannaux:
              type: array
              items:
                type: string
              example: ["TODO"]
            statut:
              type: string
              example: "en ligne"
            derAct:
              type: integer
              example: 11215568894543
            roles:
              type: array
              items:
                type: string
              example: ["admin", "moderateur"]
      404:
        description: "Utilisateur inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Utilisateur inconnu"
```

GET **/ison**

```yaml
Check online status for a list of users.

    ---
    parameters:
      - name: users
        in: query
        type: string
        required: true
        description: |
          Liste des pseudos séparés par des virgules.
          Exemple : "alice,bob,charlie"
    responses:
      200:
        description: Statuts en ligne des utilisateurs
        schema:
          type: object
          additionalProperties:
            type: boolean
          example:
            alice: true
            bob: false
            charlie: true
      400:
        description: Paramètre 'users' manquant
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Paramètre 'users' requis"
```

GET **/user/roles/<pseudo>**

```yaml
Récupérer les rôles d'un utilisateur.

    ---
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur dont on veut récupérer les rôles.
    responses:
      200:
        description: Liste des rôles de l'utilisateur
        schema:
          type: object
          properties:
            roles:
              type: array
              items:
                type: string
          example:
            roles: ["admin", "moderator"]
      404:
        description: Utilisateur non trouvé
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Utilisateur non trouvé"
```

GET **/user/avatar/\<pseudo>**

```yaml
Récupérer l'avatar d'un utilisateur.

    ---
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur dont on veut récupérer l'avatar.
    responses:
      200:
        description: Avatar récupéré avec succès
        schema:
          type: object
          properties:
            avatar:
              type: string
              description: URL ou chemin de l'avatar
          example:
            avatar: "https://example.com/avatars/alice.png"
      404:
        description: Utilisateur inconnu
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: "Utilisateur inconnu"
```

## POST

POST **/login**
```yaml
    Connecte l'utilisateur et renvoie un jeton JWT
    ---
    produces:
      - application/json
    parameters:
      - name: login
        in: body
        required: true
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            password:
              type: string
              example: "CoinCoin"
    responses:
      200:
        description: "Connexion réussie, JWT retourné"
        schema:
          type: object
          properties:
            token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      401:
        description: "Mot de passe incorrect"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Mot de passe incorrect"
      404:
        description: "Utilisateur Inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Utilisateur inconnu"
```

POST **/register**
```yaml
    Crée un nouvel utilisateur
    ---
    produces:
      - application/json
    parameters:
      - name: user_info
        in: body
        required: true
        schema:
          type: object
          required:
            - pseudo
            - email
            - password
          properties:
            pseudo:
              type: string
              example: "Roger"
            email:
              type: string
              example: "CoinCoin@duckdns.org"
            password:
              type: string
              example: "pa_en!plastik"
            avatar:
              type: string
              example: "super_duper_hot_duck.png"
    responses:
      201:
        description: "Utilisateur créé"
        schema:
          type: object
          properties:
            pseudo:
              type: string
              example: "Roger"
            email:
              type: string
              example: "CoinCoin@duckdns.org"
            password:
              type: string
              example: "pa_en!plastik"
            avatar:
              type: string
              example: "super_duper_hot_duck.png"
            statut:
              type: string
              example: "actif"
            roles:
              type: array
              items:
                type: string
              example: ["user", "..."]
      400:
        description: "Champs obligatoires manquants"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Champs obligatoires manquants"
      409:
        description: "Pseudo ou email déjà utilisé"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Pseudo ou email déjà utilisé"
      404:
        description: "Utilisateur Inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Utilisateur inconnu"
```

POST **/user/roles/\<pseudo>**

```yaml
Ajouter un rôle à un utilisateur (réservé aux administrateurs).

    ---
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur à modifier
      - name: Authorization
        in: header
        type: string
        required: true
        description: Jeton JWT d'authentification (format "Bearer <token>")
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            new_role:
              type: string
          required:
            - new_role
          example:
            new_role: "moderator"
    responses:
      200:
        description: Rôle ajouté avec succès
        schema:
          type: object
          properties:
            message:
              type: string
          example:
            message: "Rôle 'moderator' ajouté à alice"
      400:
        description: Action interdite ou rôle déjà existant chez l'utilisateur
        schema:
          type: object
          properties:
            error:
              type: string
            message:
              type: string
        examples:
          erreur_admin:
            error: "vous n'etes pas administrateur et ne pouvez pas executer cette action"
          role_existant:
            message: "alice a déjà le rôle 'moderator'"
      401:
        description: Argument manquant dans la requête
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: "argument new_role manquant"
      404:
        description: Utilisateur non trouvé
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: "utilisateur a modifier inconnu"
```

POST **/user/status**

```yaml
Modifier le statut de l'utilisateur authentifié.

    ---
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Jeton JWT d'authentification (format "Bearer <token>")
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            statut:
              type: string
              enum: ["actif", "inactif", "banni"]
          required:
            - statut
          example:
            statut: "actif"
    responses:
      200:
        description: Statut modifié avec succès
        schema:
          type: object
          properties:
            result:
              type: string
          example:
            result: "OK"
      400:
        description: Statut invalide
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: 'Statut invalide (Valeur possible : "actif", "inactif", "banni")'
      401:
        description: Token d'authentification manquant ou invalide
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: "Token manquant"
```

POST **/make-admin/\<pseudo>**

```yaml
Attribuer le rôle d'administrateur à un utilisateur (réservé aux administrateurs).

    ---
    parameters:
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur à promouvoir en admin
      - name: Authorization
        in: header
        type: string
        required: true
        description: Jeton JWT d'authentification (format "Bearer <token>")
    responses:
      200:
        description: Rôle admin ajouté avec succès et nouveau token généré
        schema:
          type: object
          properties:
            message:
              type: string
            token:
              type: string
          example:
            message: "Rôle 'admin' ajouté à alice"
            token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      400:
        description: Action interdite ou rôle déjà présent chez l'utilisateur
        schema:
          type: object
          properties:
            error:
              type: string
            message:
              type: string
        examples:
          erreur_admin:
            error: "vous n'etes pas administrateur et ne pouvez pas executer cette action"
          role_existant:
            message: "alice a déjà le rôle 'admin'"
      404:
        description: Utilisateur non trouvé
        schema:
          type: object
          properties:
            error:
              type: string
          example:
            error: "utilisateur a modifier inconnu"
```


## PATCH

PATCH **/user/\<pseudo>/password**

```yaml
    Modifie le mot de passe d’un utilisateur
    ---
    produces:
      - application/json
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Token JWT au format "Bearer <token>"
        example: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur concerné
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - old_password
            - new_password
          properties:
            old_password:
              type: string
              example: "ancien_mdp"
            new_password:
              type: string
              example: "nouveau_mdp123"
    responses:
      200:
        description: "Mot de passe modifié avec succès"
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Mot de passe mis à jour avec succès"
      400:
        description: "Requête invalide ou utilisateur connecté différent"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "pseudo, old_password ou new_password manquant"
      401:
        description: "Ancien mot de passe incorrect"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "ancien mot de passe incorrect"
      404:
        description: "Utilisateur inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "utilisateur inconnu"
```

## Delete

DELETE **/user/\<pseudo>**

```yaml
Supprime un utilisateur
    ---
    produces:
     - application/json
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: Token JWT au format "Bearer <token>"
        example: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
      - name: pseudo
        in: path
        type: string
        required: true
        description: Pseudo de l'utilisateur à supprimer
    responses:
      200:
        description: "Utilisateur supprimé"
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Utilisateur 'Roger' supprimé"
      400:
        description: "Utilisateur connecté différent"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "l'utilisateur connecté n'est pas le même que celui en argument"
      404:
        description: "Utilisateur inconnu"
        schema:
          type: object
          properties:
            error:
              type: string
              example: "utilisateur inconnu"
```