import http from 'k6/http';
import { sleep } from 'k6';
export const options = {
  vus: 200,
  duration: '60s',
};
export default function () {
    try {
        const companias = [
            'dc664148-4d33-4cad-b7de-20964f48a0c3','f65868b7-530b-4f94-a377-9760020a7dae','328ed1f4-9d12-4a69-bd2e-292f166a0a23','c924d330-a575-45e8-b21c-935622dfae23'
        ]

        const headers = {
            'Content-Type': 'application/json',
        };
    
        const data = {
            "descripcion": "transaccion de venta",
            "tipoPersona": "JURIDICA",
            "tipo": "VENTA",
            "compania_origen": "9a57dbf2-97e7-438f-84f1-8ae5334517e1",
            "compania_destino": (Math.floor(Math.random() * 9)).toString() + "23c61c2-ac03-4a03-a361-5e6ceeb812da",
            "pais_transaccion_origen": "Ecuador",
            "valor_transaccion_subtotal": 100,
            "id_propiedad": companias[Math.floor(Math.random() * companias.length)]
        }
        http.post('http://127.0.0.1:5000/transacciones', JSON.stringify(data), { headers });
        sleep(1);
    } 
    catch (error) {
        console.log(error);
    }
}