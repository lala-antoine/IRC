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

**Route GET Generique**
```yaml
    Description
    ---
    parameters:
      - name: param_name
        in: query
        type: string
        required: true
        example: "Exemple"
    responses:
      200:
        description: Description
      400:
        description: Description
```

**Route GET WhoIs**
```yaml
    Récupère les informations pubiques d'un utilisateur
---
parameters:
  - name: pseudo
    in: path
    type: string
    required: true
    description: pseudo
    example : Quack Sparrow
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
          type: int
          example: "11215568894543"
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


## POST

**Route POST Générique**
```yaml
    Description
    ---
    parameters:
      - name: param_name
        in: body
        required: true
        schema:
          type: object
          properties:
            joke:
              type: string
              example: "exemple"
    responses:
      201:
        description: "Description"
      400:
        description: "Description"
```

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
          example: {"error" : "Mot de passe incorrect"}
  404:
    description: "Utilisateur Inconnu"
        schema:
      type: object
      properties:
        error:
          type: string
          example: {"error" : "Utilisateur inconnu"}
```

POST **/register**
```yaml
     Crée un nouvel utilisateur
    ---
    parameters:
      - name: user_info
        in: body
        required: 
          - pseudo
          - email
          - password
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
    responses:
      201:
        description: "Ok"
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
                types: string
                example: ["user","..."]
      400:
        description: "Champs obligatoires manquants"
        schema:
      type: object
      properties:
        error:
          type: string
          example: {"error" : "Champs obligatoires manquants"}
      409:
        description: "Pseudo ou email déjà utilisé"
        schema:
      type: object
      properties:
        error:
          type: string
          example: {"error" : "Pseudo ou email déjà utilisé"}
      404:
        description: "Utilisateur Inconnu"
        schema:
      type: object
      properties:
        error:
          type: string
          example: {"error" : "Utilisateur inconnu"}
```