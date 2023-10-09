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

