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
        description: Descriptioin
      400:
        description: Description
```

**Route GET WhoIs**
```yaml
    Renvoie des informations publiques sur un utilisateur
    ---
    parameters:
      - name: user_info
        in: query
        type: string
        required: true
        example: "QuackSparrow"
    responses:
      200:
        description: "Ok"
      404:
        description: "Utilisateur inconnu"
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
        description: "Ok"
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                  example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      401:
        description: "Mot de passe incorrect"
      404:
        description: "Utilisateur Inconnu"
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
      400:
        description: "Champs obligatoires manquants"
      409:
        description: "Pseudo ou email déjà utilisé"
      404:
        description: "Utilisateur Inconnu"
```