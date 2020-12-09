db.createCollection("UFOs",{
    validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["marca","modelo",  "precio", "color","gama", "plazas", "caracteristicas"],
            properties:{
                modelo:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                marca:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                gama:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                tasa:{
                    bsonType:"integer",
                    description:"Debe ser un valor de tipo integro"
                },
                color:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                plazas:{
                    bsonType:"integer",
                    description:"Debe de ser un integro"
                },
                caracteristicas:{
                    bsonType:"array",
                    items: {
                        bsonType: "string",
                        description: "se requiere un valor de tipo string"
                    }
                }
            }
        }
    }
})
