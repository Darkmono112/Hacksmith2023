const restockMask = document.getElementById("restock-mask");
const restock = document.getElementById("restock");
const restockModal = document.getElementById("restock-modal");

let modalOpen = false;

restock.addEventListener("click", () => {
    modalOpen = !modalOpen;
    restockMask.dataset.display = `${modalOpen}`;
    restockModal.dataset.display = `${modalOpen}`;
});

restockMask.addEventListener("click", () => {
    modalOpen = !modalOpen;
    restockMask.dataset.display = `${modalOpen}`;
    restockModal.dataset.display = `${modalOpen}`;
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
    else {
        totalPrice.innerHTML = `${0.00}`;
    }
});

let editOpen = false;
const editModal = document.getElementById("edit-modal");
const editButton = document.querySelectorAll(".edit-button");
const editMask = document.getElementById("edit-mask");
const editName = document.getElementById("edit-name");
const editPrice = document.getElementById("edit-price");
const editQuantity = document.getElementById("edit-quantity");
const editNameInput = document.getElementById("edit-name-input");
editButton.forEach((button) => {
    button.addEventListener("click", () => {
        editOpen = !editOpen
        editModal.dataset.display = `${editOpen}`;
        editMask.dataset.display = `${editOpen}`;

        const tableRow = button.closest("tr");
        const name = tableRow.querySelector("td:nth-child(1)").innerHTML;
        const price = tableRow.querySelector("td:nth-child(2)").innerHTML;
        const quantity = tableRow.querySelector("td:nth-child(3)").innerHTML;

        editName.innerHTML = `${name}`;
        editNameInput.value = `${name}`;
        editPrice.value = `${parseFloat(price.replace("$", "")).toFixed(2)}`;

        editQuantity.value = `${quantity}`;
        console.log(editNameInput.value);
    });
});

editMask.addEventListener("click", () => {
    editOpen = !editOpen
    editModal.dataset.display = `${editOpen}`;
    editMask.dataset.display = `${editOpen}`;
});