
let isNavOpen = false;
const drawerButton = document.getElementById("drawer-button");
const drawer = document.getElementById("nav-drawer");
const menuIcon = document.getElementById("menu-icon");
const mask = document.getElementById("mask");

drawerButton.addEventListener("click", () => {
    isNavOpen = !isNavOpen;
    if (isNavOpen) {
        menuIcon.innerText = "close";
    } else {
        menuIcon.innerText = "menu";
    }
    mask.dataset.display = `${isNavOpen}`;
    drawer.dataset.open = `${isNavOpen}`;
});

mask.addEventListener("click", () => {
    isNavOpen = false;
    menuIcon.innerText = "menu";
    mask.dataset.display = `${isNavOpen}`;
    drawer.dataset.open = `${isNavOpen}`;
});
