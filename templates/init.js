import { @Name } from "./@Name.js"

let app = null;

function init() {
    app = new @Name();
    app.Run();
}

document.addEventListener("DOMContentLoaded", ()=> { init(); });