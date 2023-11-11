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

function updateTotalPrice() {
    var selectedOption = item.options[item.selectedIndex];
    const price = parseFloat(selectedOption.dataset.price);
    totalPrice.innerHTML = `${((quantity.value * price)/100).toFixed(2)}`;
}

const form = document.getElementById("restock-form");
const quantity = document.getElementById("quantity");
const item = document.getElementById("order-item");
const totalPrice = document.getElementById("total-price");
form.addEventListener("input", () => {
    if (quantity.value > 0 && item.value != "") {
        updateTotalPrice();
    }
});