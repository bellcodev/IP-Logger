# IP-Logger

## Web Falsa

<img width="761" height="685" alt="image" src="https://github.com/user-attachments/assets/184b6ba6-774b-451a-98ad-daa6bc19fd92" />

**IP Logger** es una web que simula no funcionar pero por detras a todo el que entre le extrae la ip sin su consentimiento, la registra en una base de datos SQLite3 y la agrega a un archivo con extencion .txt ademas de que te permite vincular la web a un bot de telegram y por cada persona que entre el bot envia un mensaje a tu chat diciendo la ip y el pais al que pertenece la persona, en la base de datos las IPs son unicas, ninguna se repite debido a un algoritmo que elimina las repetidas

## Resultados
| Base de datos | Telegram |
|---|---|
| <img width="326" height="436" alt="image" src="https://github.com/user-attachments/assets/0a19cf18-c843-4b1a-b4e7-26c0fc8d0e71" /> | <img width="488" height="76" alt="image" src="https://github.com/user-attachments/assets/e0b71fce-d9a3-45da-86e9-75a351f40978" /> |

## Funcionamiento
La web visualmente se ve igual que una pagina de error 404(Not Found), por detras hay un JavaScript que extrae la ip atravez de la api (https://api.ipify.org?format=json), despues envia por un fetch la ip a la api local getIp hecha con fastapi, la api obtiene la ip, comprueba el pais de la ip y si ya estaba registrada, envia el mensaje atravez del bot al admin utilizando la api de telegram (api.telegram.org), registra la ip en la base de datos y en el archivo .txt llamado ips.txt

**NO ME RESPONSABILIZO POR EL USO INDEBIDO DE ESTA HERRAMIENTA**
