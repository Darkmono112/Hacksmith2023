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

const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let currentSlide = 0;

function showSlide(n) {
    slides.forEach((slide, index) => {
        slide.style.transform = `translateX(${100 * (index - n)}%)`;
    });
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        showSlide(currentSlide);
    }
}

function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        showSlide(currentSlide);
    }
}

prevBtn.addEventListener('click', prevSlide);
nextBtn.addEventListener('click', nextSlide);

// Initial display
showSlide(currentSlide);


