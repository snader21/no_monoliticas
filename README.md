# Escenarios de calidad trabajados
## Escenario #1 Modificabilidad

Esta implementacion inicial, quiere demostrar como con el uso de la arquitectura hexagonal y una buena division de la logica de dominio, podemos realizar modificaciones por ejemplo al ingresar en un nuevo pais que tiene unas politicas diferentes para el calculo de los valores de las transacciones, y estas solo deben realizarse a 
un unico componente dentro del codigo sin afectar las demas partes del servicio, ademas al manejarse por eventos de dominio, los demas microservicios son agnosticos a este cambio y seguiran operando sin verse afectados por el cambio

## Escenario #2 Disponibilidad


## Escenario #3 Disponibilidad


## Actividades realizadas por cada integrante

- **Said**: Encargado del desarrollo del microservicio de propiedades, así como de la realización de pruebas de escenarios de calidad para garantizar su funcionamiento óptimo. Su dedicación fue del 25% para el proyecto.

- **Andres**: Responsable de refactorizar el microservicio de transacciones y compañía, convirtiéndolo de un monolito a dos microservicios independientes comunicados por eventos y llevando a cabo pruebas exhaustivas de escenarios de calidad para asegurar su robustez y eficiencia. Su dedicación fue del 25% para el proyecto.

- **Ricardo**: Encargado del desarrollo del microservicio de limpieza, gestionando consumidores y despachadores de eventos, además de llevar a cabo pruebas de escenarios de calidad para garantizar su correcto funcionamiento en diversas situaciones. Su dedicación fue del 25% para el proyecto.

- **Fabian**: Responsable del desarrollo del microservicio de limpieza, junto con la implementación de consumidores y despachadores de eventos, y realización de pruebas de escenarios de calidad para asegurar su rendimiento y fiabilidad. Su dedicación fue del 25% para el proyecto.


## Estructura del proyecto

- El microservicio se encuentra en la raiz del proyecto en la carpeta **src\recopilacion** el cual tiene dos modulos, el de compañias y el de transacciones.
- Ambos modulos se encuentran en **src\recopilacion\modulos** yu cada uno de ellos cuenta con la estructura de careptetas [Aplicacion, Dominio e Infraestructura]
- Los endpoints de nuestro servicio se encuentran en la carpeta **src\recopilacion\api** y hay un archivo para cada modulo
- Cada modulo cuenta con el patron CQS, por lo tanto en la carpeta de aplicacion, encontramos dos carpetas, una para comandos y otra para queries EJ. **src\recopilacion\modulos\compania\aplicacion\comandos**
- Hacemos uso de una seedWork que se encuentra en **src\recopilacion\seedwork**
- Para el manejo de colas y eventos de dominio se usa la capa de infraestructura, para el despachador que esta en compañias usamos **src\recopilacion\modulos\compania\infraestructura\despachadores.py** y para el consumidor que esucha en transacciones **src\recopilacion\modulos\transaccion\infraestructura\consumidores.py**
- Las entidades de persistencia se encuentran en la capa de infraestructura de cada modulo Ej. **src\recopilacion\modulos\transaccion\infraestructura\dto.py**
- Las entidades de dominio, mediante las cuales implementamos la logica de negocio se encuentran en la capa de dominio EJ. **src\recopilacion\modulos\transaccion\dominio\entidades.py**

## Tutorial para correr nuestro proyecto
### Paso 1 Ejecutar apache pulsar y base de datos

Desde el directorio principal ejecute el siguiente comando.

```bash
docker compose up -d
```

**Nota* Una vez ejecutado el contenedor, debera correr manualmente los microservicios (La idea es que en la ultima entrega ya podamos tener esto desplegado en el docker compose, pero por ahora es necesario correrlos por separado).

### Paso 2 Ejecutar los microservicios
Desde el directorio principal ejecute en consolas separadas los siguientes comandos.

```Bash
flask --app ./compania/src/app.py run --port=5000 #Microservicio de compañias
flask --app ./transaccion/src/app.py run --port=5001 #Microservicio de transacciones
flask --app ./propiedades/src/app.py run --port=5002 #Microservicio de propiedades
flask --app ./limpieza/src/app.py run --port=5003 #Microservicio de limpieza
```



### Ejecutar pruebas
Para las pruebas crear una compañia inicialmente apuntando a al endpoint: (POST) http://127.0.0.1:5000/companias pasando este payload,

```
{
    "tipoPersona": "NATURAL",
    "nombre": "predito",
    "tipo": "COMPRADOR",
    "pais": "Colombia",
    "identificacion": "1234"
}
```
**Verifique en la base de datos que la compañia se haya creado correctamente 

Luego asocie una transaccion a esa compañia mediante el EndPoint: (POST) http://127.0.0.1:5001/transacciones pasando el siguiente payload
```
{
    "descripcion": "transaccion de venta",
    "tipoPersona": "JURIDICA",
    "tipo": "ARRIENDO",
    "compania_origen": "9a57dbf2-97e7-438f-84f1-8ae5334517e1",
    "compania_destino": "123c61c2-ac03-4a03-a361-5e6ceeb812da",
    "pais_transaccion_origen": "Ecuador",
    "valor_transaccion_subtotal": 100,
    "id_propiedad": "2a7e6641-d76b-4f09-be62-27b3c10c40e0"
}
```
**Verifique en la base de datos que la transaccion se haya creado correctamente

Luego cambie de pais la compañia original mediante el EndPoint: (PATCH) http://127.0.0.1:5000/companias/<<uuid de la compañia creada en la base de datos>> pasando el siguiente payload
```
{
    "pais": "Peru"
}
```
**Verifique en la base de datos que el pais de la tabla de companias cambio, y ademas en la tabla de transacciones el pais tambien cambio y los impuestos fueron recalculados

Los paises que puede elejir son (Colombia, Peru, Ecuador)

### Ejecutar pruebas entrega 2
Cree una propiedad mediante el EndPoint: (POST) http://127.0.0.1:5002/propiedades pasando el siguiente payload
```
{
    "compania_duena": "dbd9e097-2b6f-4795-b798-389af600a018",
    "compania_arrendataria": "5f6a5bb7-a19d-47d8-b1a4-ed5ec3575108",
    "direccion": "calle falsa 123",
    "tamano": 99,
    "pais_ubicacion": "Colombia"
}
```
**Verifique en la base de datos que la propiedad se haya creado correctamente (si el servicio de limpieza estaba en ejecucion las columnas latitud y longitud deberian estar calculadas)

Cree una transaccion de tipo venta asociada a la propiedad que acaba de crear mediante el EndPoint: http://127.0.0.1:5000/transacciones pasando el siguiente payload
```
{
    "descripcion": "transaccion de venta",
    "tipoPersona": "JURIDICA",
    "tipo": "ARRIENDO",
    "compania_origen": "9a57dbf2-97e7-438f-84f1-8ae5334517e1",
    "compania_destino": "456c61c2-ac03-4a03-a361-5e6ceeb812da",
    "pais_transaccion_origen": "Ecuador",
    "valor_transaccion_subtotal": 100,
    "id_propiedad": "2a7e6641-d76b-4f09-be62-27b3c10c40e0"
}
```
**Verifique en la base de datos que el duaño de la propiedad se haya actualizado correctamente
