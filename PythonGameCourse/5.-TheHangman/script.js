//const words =["lento","perezoso","Furioso","Rabioso","Audaz","Sensible","Abierto"]

const contenedorPalabras = document.getElementById("wordContainer")
const btnStart = document.getElementById("startButton")
const palabrasUsadas = document.getElementById("usedLetters")
const canvas = document.getElementById("canvas")

let ctx = canvas.getContext("2d")
ctx.canvas.width = 0
ctx.canvas.heigth = 0

const bodyParts =[
    [4,2,1,1],
    [4,3,1,2],
    [3,5,1,1],
    [5,5,1,1],
    [3,3,1,1],
    [5,3,1,1]

]

let palabraSeleccionada;
let palabraUsuario;
let errores;
let aciertos;


const addPalabra = Palabra =>{
    const PalabraElement = document.createElement("span")

    PalabraElement.innerHTML = Palabra.toUpperCase()

    PalabraUsuarioElement.appendChild(PalabraElement)
}

const addbodyParts = bodyPart =>{

    ctx.fillStyle= "#fff";
    ctx.fillRect(...bodyPart)

}
const wrongPalabra = ()=>{

    addBodyPart(bodyParts[Erroes])
    errores++

    if (errores === bodyParts.length){
        endgame()
    }

}
const endgame = () => {
    document.removeEventListener("keydown",evalPalabraEvent)

    btnStart.style.display="block"
}
const correctPalabra = Palabra =>{

    const {children} = contenedorPalabras;

    for(let i = 0; i< children.length; i++){
        if (children[i.innerHTML == Palabra]){
            children[i].classList.toggle("hidden")
            aciertos++
        }
        
    }
    if (aciertos == palabraSeleccionada.length){
        endgame()
    }
}

const palabraInput = Palabra =>{
        if(palabraSeleccionada.includes(Palabra)){
            correctPalabra(Palabra)
        }else{
            wrongPalabra()
        }
}

const evalPalabraEvent = Event =>{
    let newPalabraE = event.key.toUpperCase()

    if(newPalabraE.match(/^[a-zñ]$/i) && !palabraUsuario.includes(newPalabraE)){
        palabraInput(newPalabraE)

    }
}
const selectRandomWord =()=>{
    const words =["lento","perezoso","Furioso","Rabioso","Audaz","Sensible","Abierto"]
    let palabra = words[Math.floor((Math.random()*words.length))].toUpperCase();

    palabraSeleccionada = palabra.split("")
}


const drawingHangMan =()=>{

    ctx.canvas.width=120
    ctx.canvas.heigth=160
    ctx.scale(20,20)
    ctx.clearRect(0,0,canvas.width,canvas.heigth)

    ctx.fillStyle="#d95d39"
    ctx.fillRect(0,7,4,1)
    ctx.fillRect(1,0,1,8)
    ctx.fillRect(2,0,3,1)
    ctx.fillRect(4,1,1,1)
}

const drawWord =()=>{
    palabraSeleccionada.forEach(Palabra => {
        const PalabraElement = document.createElement("span")
        PalabraElement.innerHTML = Palabra.toUpperCase()

        PalabraElement.classList.add("letter")
        PalabraElement.classList.add("hidden")

        contenedorPalabras.appendChild(PalabraElement)
        
    });
}

const iniciarJuego =()=>{
    palabraUsuario =[]
    errores=0
    aciertos=0
    contenedorPalabras.innerHTML =""
    palabraUsuario.innerHTML=""
    btnStart.style.display="none"
    drawingHangMan()
    selectRandomWord()
    drawWord()

    document.add("keydown",evalPalabraEvent)
}

btnStart.addEventListener("click", iniciarJuego)