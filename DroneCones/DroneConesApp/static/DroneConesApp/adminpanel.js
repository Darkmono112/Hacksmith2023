const drones_button = document.getElementById('Drones-button');  // button
const inventory_button = document.getElementById('Inventory-button');  // button
const drones_table = document.getElementById('drones');
const inventory_table = document.getElementById('inventory')


drones_button.addEventListener('click', () => {
    dronesPage.dataset.display = "true";
    inventoryPage.dataset.display = "false";
});

inventory_button.addEventListener('click', () => {
    dronesPage.dataset.display = "false";
    inventoryPage.dataset.display = "true";
});