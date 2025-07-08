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
        description: Description
      400:
        description: Description
```

POST **/login**
```yaml
    Description
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
      401:
        description: "Mot de passe incorrect"
      404:
        description: "Utilisateur Inconnu"
```