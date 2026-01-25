# 💻 IP-Logger

**IP Logger** es una web que simula no funcionar pero por detras a todo el que entre le extrae la ip sin su consentimiento, la registra en una base de datos SQLite3 y la agrega a un archivo con extencion .txt ademas de que te permite vincular la web a un bot de telegram y por cada persona que entre el bot envia un mensaje a tu chat diciendo la ip y el pais al que pertenece la persona, en la base de datos las IPs son unicas, ninguna se repite debido a un algoritmo que elimina las repetidas

## 📊 Badges

![License](https://img.shields.io/github/license/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Stars](https://img.shields.io/github/stars/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Forks](https://img.shields.io/github/forks/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Issues](https://img.shields.io/github/issues/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Pull Requests](https://img.shields.io/github/issues-pr/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/bellcodev/IP-Logger?style=for-the-badge&logo=git)
![Repo Size](https://img.shields.io/github/repo-size/bellcodev/IP-Logger?style=for-the-badge&logo=github)
![Code Size](https://img.shields.io/github/languages/code-size/bellcodev/IP-Logger?style=for-the-badge&logo=github)

![Top Language](https://img.shields.io/github/languages/top/bellcodev/IP-Logger?style=for-the-badge&logo=python)
![Languages Count](https://img.shields.io/github/languages/count/bellcodev/IP-Logger?style=for-the-badge&logo=code)

![Docs](https://img.shields.io/badge/docs-available-brightgreen?style=for-the-badge&logo=readthedocs)
![Wiki](https://img.shields.io/badge/wiki-enabled-blue?style=for-the-badge&logo=github)

![Status](https://img.shields.io/badge/status-active-success?style=for-the-badge&logo=github)
![Made With Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red?style=for-the-badge)

## ⚒️ Funciones

### 👤 Web Falsa

<img width="761" height="685" alt="image" src="https://github.com/user-attachments/assets/184b6ba6-774b-451a-98ad-daa6bc19fd92" />

Esta es la web principal a la que accede el usuario para obtener su ip sin su permiso, la web simula ser una web de error 404(Not Found) que "no funciona"

---

### 🗺️ Mapa Visual

<img width="1358" height="724" alt="image" src="https://github.com/user-attachments/assets/72a97ecb-9c71-4b70-ba6e-33f048dd8b90" />

La Web contiene dos endpoints, uno llamado /map y otro /seeMap

**/map**: Al entrar crea un html con un *mapa interactivo* con las ubicaciones geograficas de todas las IPs de la base de datos y muestra el mapa (tarda en cargar de 1 a x minutos, depende de la cantidad de IPs de la base de datos y de la conexion del servidor

**/seeMap**: Cuando ya tienes una version del *mapa* la puedes cargar rapidamente con este endpoint sin tener que volver a crearlo

---

### 🌐 Telegram

La Web aparte de registrar las IPs en la base de datos, tambien envia un mensaje al id del usuario puesta en el codigo desde un *bot de telegram*(el admin tiene que crear el bot y copiar el token en la variable TOKEN)

---

### 📄 Archivo TXT

Al mismo tiempo que se registra la ip en la base de datos, se registra en un archivo txt

---

### 👨‍💻 Control Panel

Usuario: admin\
Contraseña: 4dm1n666

La web contiene el EndPoint /admin, dentro de el te pide un usuario y una contraseña, si se introducen bien puedes acceder si no envia un mensaje desde el bot de telegram vinculado al chat diciendo que un usuario intento entrar al panel y te da toda la info posible del usuario.

---

## 🛜 Resultados
| Base de datos | Telegram |
|---|---|
| <img width="326" height="436" alt="image" src="https://github.com/user-attachments/assets/0a19cf18-c843-4b1a-b4e7-26c0fc8d0e71" /> | <img width="488" height="76" alt="image" src="https://github.com/user-attachments/assets/e0b71fce-d9a3-45da-86e9-75a351f40978" /> |

---

## 🧮 Funcionamiento
La web es exactamente igual que una de error 404(Not found), al entrar se extrae con un JavaScript la ip publica del usuario, se registra en una base de datos local SQLite3 llamada IPsDatabase.db, se le agrega a un TXT ubicado en la misma carpeta y llamado ips.txt, al mismo tiempo le hace una peticion GET a /map el cual registra la ubicacion geografica en un mapa interactivo hecho en HTML y registrado en un archivo mapa_ips.html el cual puedes ver en el endpoint /seeMap o desde el boton "Ver Mapa Interactivo" en el Panel de Control, tambien esta el endpoint /admin que si no accedes con las credenciales correctas te envia un mensaje por telegram mostrandote toda la info del intruso y si accedes con las credenciales correctas (usuario: admin , contraseña: 4dm1n666) te muestra una interfaz con el dominio actual, las ips recolectadas actualmente, y todas las estadisticas de la cantidad de ips por paises recolectadas y un boton que te permite ver el mapa interactivo con las IPs geolocalizadas.


## **NO ME RESPONSABILIZO POR EL USO INDEBIDO DE ESTA HERRAMIENTA**

