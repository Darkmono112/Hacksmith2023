const drones= document.getElementById('Drones');  // button
const Inventory = document.getElementById('Inventory');  // button

let inventoryPage = true;
let dronesPage = false;

drones.addEventListener('click', () => {
    inventoryPage = false;
    dronesPage = true;
});

drones.addEventListener('click', () => {
    inventoryPage = false;
    dronesPage = true;
});