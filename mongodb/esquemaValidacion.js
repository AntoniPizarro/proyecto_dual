db.createCollection("UFOs",{
    validator:{
        $jsonSchema:{
            bsonType:"object",
            required:["marca","modelo",  "precio", "color","gama", "plazas", "caracteristicas"],
            properties:{
                marca:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                modelo:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                color:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                gama:{
                    bsonType:"string",
                    description:"Debe ser un valor de tipo string"
                },
                plazas:{
                    bsonType:"integer",
                    description:"Debe de ser un integro"
                },
                caracteristicas:{
                    bsonType:"array",
                    description:"Debe ser un valor de tipo array"
                }
            }
        }
    }
})
