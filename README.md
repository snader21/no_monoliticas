# Tutorial para correr nuestro proyecto - Escenario de calidad #1 Modificabilidad

Esta implementacion inicial, quiere demostrar como con el uso de la arquitectura hexagonal y una buena division de la logica de dominio, podemos realizar modificaciones por ejemplo al ingresar en un nuevo pais que tiene unas politicas diferentes para el calculo de los valores de las transacciones, y estas solo deben realizarse a 
un unico componente dentro del codigo sin afectar las demas partes del servicio, ademas al manejarse por eventos de dominio, los demas microservicios son agnosticos a este cambio y seguiran operando sin verse afectados por el cambio

## Estructura del proyecto

- El microservicio se encuentra en la raiz del proyecto en la carpeta **src\recopilacion** el cual tiene dos modulos, el de compañias y el de transacciones.
- Ambos modulos se encuentran en **src\recopilacion\modulos** yu cada uno de ellos cuenta con la estructura de careptetas [Aplicacion, Dominio e Infraestructura]
- Los endpoints de nuestro servicio se encuentran en la carpeta **src\recopilacion\api** y hay un archivo para cada modulo
- Cada modulo cuenta con el patron CQS, por lo tanto en la carpeta de aplicacion, encontramos dos carpetas, una para comandos y otra para queries EJ. **src\recopilacion\modulos\compania\aplicacion\comandos**
- Hacemos uso de una seedWork que se encuentra en **src\recopilacion\seedwork**
- Para el manejo de colas y eventos de dominio se usa la capa de infraestructura, para el despachador que esta en compañias usamos **src\recopilacion\modulos\compania\infraestructura\despachadores.py** y para el consumidor que esucha en transacciones **src\recopilacion\modulos\transaccion\infraestructura\consumidores.py**
- Las entidades de persistencia se encuentran en la capa de infraestructura de cada modulo Ej. **src\recopilacion\modulos\transaccion\infraestructura\dto.py**
- Las entidades de dominio, mediante las cuales implementamos la logica de negocio se encuentran en la capa de dominio EJ. **src\recopilacion\modulos\transaccion\dominio\entidades.py**

## Servicio de recoleccion
### Ejecutar Aplicación

Desde el directorio principal ejecute el siguiente comando.

```bash
docker compose up -d
```

**Nota* Una vez ejecutado el contenedor, es probable que la aplicacion de flask no este corriendo, de ser el caso intente arrancando manualmente dicho servicio.

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

Luego asocie una transaccion a esa compañia mediante el EndPoint: (POST) http://127.0.0.1:5000/transacciones pasando el siguiente payload
```
{
    "descripcion": "transaccion de venta",
    "tipoPersona": "JURIDICA",
    "tipo": "VENTA",
    "compania_origen": "<<uuid de la compañia creada en la base de datos>>",
    "compania_destino": "223c61c2-ac03-4a03-a361-5e6ceeb812da",
    "pais_transaccion_origen": "Colombia",
    "valor_transaccion_subtotal": 100
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

