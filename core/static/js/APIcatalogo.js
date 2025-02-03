let jsonData = {};

async function getData() {
    const resp = await fetch("http://127.0.0.1:8000/api/imagenes");

    jsonData = await resp.json();

    showData();
}

function showData() {
    if (jsonData) {
        console.log(jsonData);
        const listContainer = document.querySelector("#contenido");
        for (let i = 0; i < jsonData.length; i++) {
            const card = document.createElement("DIV");
            card.classList.add("col");

            const img = document.createElement("IMG");
            img.classList.add("card-img-top");
            img.src = jsonData[i].imagenAPI;
            img.width = "100";

            const title = document.createElement("H3");
            title.classList.add("text-center");
            title.textContent = jsonData[i].nombre;

            const cardBody = document.createElement("DIV");
            cardBody.classList.add("card","h-100","color-cuerpo");
            
            const cardText = document.createElement("DIV");
            cardText.classList.add("card-body");

            cardText.appendChild(title);
            cardBody.appendChild(img);
            cardBody.appendChild(cardText);
            card.appendChild(cardBody);
            listContainer.appendChild(card);
        }
    }
}

getData();
