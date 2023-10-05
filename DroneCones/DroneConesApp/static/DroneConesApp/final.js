let isDrawerOpen = false;
drawer = document.getElementById('navdrawer');
document.getElementById('menuButton').addEventListener('click', () => {
    isDrawerOpen = !isDrawerOpen
    drawer.dataset.open = `${isDrawerOpen}`;
});

document.getElementById('button').addEventListener('mousedown', () =>{
    document.getElementById('button').classList.add('clicked')
})
document.getElementById('button').addEventListener('mouseup', () =>{
    document.getElementById('button').classList.remove('clicked')
})
document.getElementById('button').addEventListener('mouseleave', () =>{
    document.getElementById('button').classList.remove('clicked')
})

let FAB = document.getElementById('FAB')
FAB.addEventListener('mousedown', () => {
    FAB.classList.add('clicked')
})
FAB.addEventListener('mouseup', () => {
    FAB.classList.remove('clicked')
})
FAB.addEventListener('mouseleave', () => {
    FAB.classList.remove('clicked')
})

let vine = document.getElementById('vine')
let flower = document.getElementById('sunflower')
let spinner3 = document.getElementById('spinner3')
spinner3.addEventListener("mouseover", () => {
    vine.animate([{
        width: `75px`,
        height: `75px`,
        zIndex: `-1`,
        position: `relative`,
        left: `-25px`,
        bottom: `120px`,
    }], {duration: 300, fill: "forwards"})
})
spinner3.addEventListener("mouseleave", () => {
    vine.animate([{
        width: `1px`,
        height: `1px`,
        transform: `rotateZ(5deg)`,
        position: `relative`,
        left: `30px`,
        bottom: `45px`



    }], {duration: 300, fill: "forwards"})
})

document.getElementById('flower-html').innerText = `
<div class="spinner-container">
    <div id="spinner3">
        <img src="img.png" alt="Sunflower" id="sunflower">
        <img src="img_1.png" alt="Vine" id="vine">
    </div>
</div>
`;

