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

Clé JWT : **on-ny-arrivera-jamais**
```json
{
"pseudo" : "string",
"expiration" : "int", // (timestamp)
"roles" : ["string"] 
}
```

# Routes

**Route GET**
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

**Route POST**
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