const drones_button = document.getElementById('Drones-button');  // button
const inventory_button = document.getElementById('Inventory-button');  // button
const drones_table = document.getElementById('drones');
const inventory_table = document.getElementById('inventory')


drones_button.addEventListener('click', () => {
    drones_table.dataset.display = "true";
    inventory_table.dataset.display = "false";
});

inventory_button.addEventListener('click', () => {
    drones_table.dataset.display = "false";
    inventory_table.dataset.display = "true";
});