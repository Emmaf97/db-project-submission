document.addEventListener("DOMContentLoaded", init);

function init() {
    let lightToggle = document.getElementById("dark-icon");
    lightToggle.addEventListener("click", lightMode);
    checkLightActive();
}

let toggleCheck = false;

function checkLightActive() {
    if (localStorage.getItem("light-mode") === "true") {
        lightMode();
    }
}


function lightMode() {
    let { btnElements, head, nav, pLight, icon, body, cardtext  } = getIndexDocElements();
    for (let i = 0; i < btnElements.length; i++) {
        let lightModeAdded = btnElements[i].classList.toggle("dark-icon");
        if (!lightModeAdded) {
            toggleCheck = false;
            localStorage.setItem("light-mode", toggleCheck);
            body.classList.remove("body-light");
            head.classList.remove("bg-light")
            head.classList.add("bg-dark")
            nav.classList.remove("bg-light")
            nav.classList.add("bg-dark")
            nav.classList.toggle("bg-light")
            for (let j = 0; j < pLight.length; j++) {
                pLight[j].classList.remove("p-light");
            }
            for (let c = 0; c < cardtext.length; c++) {
                cardtext[c].classList.remove("card-text-light")
            }
        }
        else {
            toggleCheck = true;
            localStorage.setItem("light-mode", toggleCheck);
            body.classList.add("body-light");
            head.classList.remove("bg-dark")
            head.classList.add("bg-light")
            nav.classList.remove("bg-dark")
            nav.classList.add("bg-light")
            for (let k = 0; k < pLight.length; k++) {
                pLight[k].classList.add("p-light");
            }
            for (let b = 0; b < cardtext.length; b++) {
                cardtext[b].classList.add("card-text-light")
            }
        }
    }
}
function getIndexDocElements() {
    let btnElements = document.querySelectorAll(".material-symbols-outlined");
    let body = document.querySelector("body")
    let head = document.querySelector("header")
    let nav = document.querySelector("nav")
    let icon = document.querySelector("icon")
    let main = document.querySelector("main")
    let foot = document.querySelector("foot")
    let pLight = document.querySelectorAll(".p.left")
    let cardtext = document.querySelectorAll(".card-text")
    return { btnElements, body, pLight, cardtext, icon,head, main,nav, foot};
    // 
}
