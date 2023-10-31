const modalMask = document.getElementById("modal-mask");
const restock = document.getElementById("restock");
const modalSection = document.getElementById("modal-section");

let modalOpen = false;

restock.addEventListener("click", () => {
    modalOpen = !modalOpen;
    modalMask.dataset.display = `${modalOpen}`;
    modalSection.dataset.display = `${modalOpen}`;
});

modalMask.addEventListener("click", () => {
    modalOpen = !modalOpen;
    modalMask.dataset.display = `${modalOpen}`;
    modalSection.dataset.display = `${modalOpen}`;
});