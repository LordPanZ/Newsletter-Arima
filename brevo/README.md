# Arima aldizkaria en Brevo

`arima-aldizkaria.html` es la newsletter en formato correo (tablas, estilos en línea, 600 px, adaptada a móvil). Incluye los enlaces de Brevo `{{ unsubscribe }}` (baja) y `{{ mirror }}` (ver en navegador).

## 1. Subir las imágenes
1. Brevo → **Contenido → Biblioteca de imágenes** (Content → Image gallery) → sube el logo (`assets/arima-logo.jpg`) y una foto por trabajo (7 fotos).
2. Copia la URL de cada imagen en `imagenes.json` (`logo`, `foto1` … `foto7`). El orden es el de la revista: Ortuella, Sestao, Ugao-Miraballes, Irun, Portugalete (7 de octubre), Erandio, Portugalete (16 de octubre).
3. Ejecuta `python3 build.py` para regenerar `arima-aldizkaria.html` con tus URLs.
   (También puedes sustituir a mano las URLs de `placehold.co` en el HTML.)

> El artículo 08 de la revista web (Inguru Minguru) no está en esta plantilla de correo. Si lo quieres, dímelo y lo añado.

## 2. Crear la campaña
1. **Campañas → Crear una campaña de email**. Nombre interno: `Aldizkaria 2026-10`.
2. Remitente: `arimacooltour@gmail.com`, nombre `Arima`. Asunto sugerido: `Esku lanetik bihotzera · Arima aldizkaria`.
3. Diseño: **Editor de código / HTML personalizado** → pega el contenido de `arima-aldizkaria.html`.
4. Envía antes un **mensaje de prueba** a tu correo y revísalo en móvil.

## 3. Contactos (altas y bajas)
1. En Google Contactos, abre cada etiqueta (Bizkaia, Gipuzkoa, Araba) → **Exportar → CSV de Google**.
2. Brevo → **Contactos → Importar contactos** (un archivo por etiqueta) y asígnalos a tres listas: `Bizkaia`, `Gipuzkoa`, `Araba`.
3. Al crear la campaña, elige las tres listas como destinatarios.
4. Las **bajas** las gestiona Brevo con el enlace del pie: quien se da de baja queda bloqueado y no recibe más envíos.
5. Las **altas nuevas**: crea un formulario de suscripción en Brevo (Contactos → Formularios) y comparte el enlace; las altas manuales también se pueden importar.

## 4. Antes de enviar
- Importa solo contactos que hayan aceptado recibir vuestras comunicaciones (RGPD). Si no estás seguro, envía primero un correo corto pidiendo confirmación.
- Brevo exige una dirección postal en el pie de los envíos masivos. Añádela en el pie de `arima-aldizkaria.html` o en los ajustes de la cuenta.
- Las fuentes Abel y Cormorant solo se ven en algunos clientes; en el resto aparecerán Arial y Georgia.
