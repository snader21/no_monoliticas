# Escenarios de calidad trabajados
## Escenario #1 Modificabilidad (Lógica de transacciones en un nuevo mercado)

Esta implementación inicial tiene como objetivo destacar la efectividad de la arquitectura hexagonal y una adecuada división de la lógica de dominio. Esto se evidencia al realizar modificaciones, como ingresar a un nuevo país con políticas distintas para el cálculo de valores de transacciones. Estas modificaciones se aplican de manera focalizada a un único componente dentro del código, sin afectar otras partes del servicio. Gracias a la gestión mediante eventos de dominio, los demás microservicios permanecen agnósticos a estos cambios y continúan operando sin verse afectados por las actualizaciones realizadas.
![image](https://github.com/snader21/no_monoliticas/assets/124009412/55291b55-2b7a-4609-9c85-de399f774f1b)

## Escenario #2 Disponibilidad (El sistema ante ingesta de grandes volúmenes de información, sigue haciendo consultas sin lentitudes)

En esta segunda implementación, observamos cómo el empleo de arquitecturas orientadas a eventos y el patrón CQS nos posibilita mantener una respuesta eficaz ante solicitudes de consulta, incluso en situaciones de elevada demanda. Esto se debe a que cada microservicio opera de manera independiente. Por ejemplo, al crear una transacción de tipo VENTA que requiere la actualización de una propiedad, el microservicio de transacciones no espera a que dicha actualización se complete. Esta independencia garantiza que las consultas no se vean afectadas por bloqueos, permitiendo que se realicen sin experimentar alteraciones en sus tiempos de respuesta.
![image](https://github.com/snader21/no_monoliticas/assets/124009412/7c60dfb9-1e7f-4cf0-ac15-b91a062c9f28)

## Escenario #3 Disponibilidad (Ante el fallo de un componente el sistema sigue funcionando correctamente ante la recolecciónn de información)
En este escenario, destacamos otra ventaja de los microservicios y los tópicos de eventos. En este caso, nos interesa observar cómo, si un componente suscriptor (como el microservicio de limpieza) está inactivo, ello no afecta la operación normal del aplicativo. Además, cuando dicho componente se reactiva, tiene la capacidad de retomar las tareas que fueron publicadas en el tópico durante su ausencia. Este enfoque previene la pérdida de información ante posibles fallos, asegurando una continuidad efectiva en la gestión de eventos incluso en circunstancias adversas.
![image](https://github.com/snader21/no_monoliticas/assets/124009412/3f1ffa0a-d8e4-4527-b0d3-9c212c8007ac)


## Actividades realizadas por cada integrante

- **Said Nader**: Encargado del desarrollo del microservicio de propiedades, así como de la realización de pruebas de escenarios de calidad para garantizar su funcionamiento óptimo. Su dedicación fue del 25% para el proyecto.

- **Andres Martinez**: Responsable de refactorizar el microservicio de transacciones y compañía, convirtiéndolo de un monolito a dos microservicios independientes comunicados por eventos y llevando a cabo pruebas exhaustivas de escenarios de calidad para asegurar su robustez y eficiencia. Su dedicación fue del 25% para el proyecto.

- **Ricardo Vivas**: Encargado del desarrollo del microservicio de limpieza, gestionando consumidores y despachadores de eventos, además de llevar a cabo pruebas de escenarios de calidad para garantizar su correcto funcionamiento en diversas situaciones. Su dedicación fue del 25% para el proyecto.

- **Fabian Orozco**: Responsable del desarrollo del microservicio de limpieza, junto con la implementación de consumidores y despachadores de eventos, y realización de pruebas de escenarios de calidad para asegurar su rendimiento y fiabilidad. Su dedicación fue del 25% para el proyecto.

## Consideraciones
- En la actualidad, la comunicación entre todos nuestros microservicios se realiza mediante eventos delta. Este enfoque permite evitar el envío completo del payload de una entidad al reescribir el estado o el historial. Para la definición de estos esquemas, hemos optado por utilizar AVRO. Cada microservicio cuenta con su propia definición incorporada en la capa de infraestructura, lo que contribuye a una implementación más eficiente y a una gestión más precisa de la información intercambiada entre los servicios.
- En nuestra implementación actual, hemos adoptado un modelo de persistencia para el estado basado en las operaciones CRUD. Esta elección se debe, en parte, a la familiaridad del equipo de desarrollo con este enfoque. Además, la consideración de Event Sourcing se descartó debido a que su implementación hubiera añadido complejidad al desarrollo. En este caso, habríamos tenido que modificar nuestros eventos, pasando de un formato delta a un formato más completo, lo cual habría implicado cambios sustanciales en la arquitectura existente.

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

Cree una transaccion de tipo venta asociada a la propiedad que acaba de crear mediante el EndPoint: http://127.0.0.1:5001/transacciones pasando el siguiente payload
```
{
    "descripcion": "transaccion de venta",
    "tipoPersona": "JURIDICA",
    "tipo": "VENTA",
    "compania_origen": "9a57dbf2-97e7-438f-84f1-8ae5334517e1",
    "compania_destino": "456c61c2-ac03-4a03-a361-5e6ceeb812da",
    "pais_transaccion_origen": "Ecuador",
    "valor_transaccion_subtotal": 100,
    "id_propiedad": "2a7e6641-d76b-4f09-be62-27b3c10c40e0"
}
```
**Verifique en la base de datos que el duaño de la propiedad se haya actualizado correctamente
