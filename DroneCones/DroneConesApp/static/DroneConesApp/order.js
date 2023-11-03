const summarySection = document.getElementById('summary');
const billingSection = document.getElementById('billing');
const shippingSection = document.getElementById('shipping');

const summaryContainer = document.getElementById('summary-container');
const billingContainer = document.getElementById('billing-container');
const shippingContainer = document.getElementById('shipping-container');

const summaryChevron = document.getElementById('summary-chevron');
const billingChevron = document.getElementById('billing-chevron');
const shippingChevron = document.getElementById('shipping-chevron');

const showShipping = document.getElementById('show-shipping');
const showBilling = document.getElementById('show-billing');
const showSummary = document.getElementById('show-summary');

let isSummaryOpen = true;
let isBillingOpen = false;
let isShippingOpen = false;

summaryContainer.dataset.display=`${isSummaryOpen}`;
summaryChevron.dataset.display=`${isSummaryOpen}`; 
showSummary.innerHTML = 'Hide Details';

function closeOthers(section) {
    if (section === 'summary') {
        isBillingOpen = false;
        isShippingOpen = false;
        showShipping.innerHTML = 'Show Details';
        showBilling.innerHTML = 'Show Details';
        billingContainer.dataset.display=`${isBillingOpen}`;
        shippingContainer.dataset.display=`${isShippingOpen}`;
        billingChevron.dataset.display=`${isBillingOpen}`;
        shippingChevron.dataset.display=`${isShippingOpen}`;
    } else if (section === 'billing') {
        isSummaryOpen = false;
        isShippingOpen = false;
        showShipping.innerHTML = 'Show Details';
        showSummary.innerHTML = 'Show Details';
        summaryContainer.dataset.display=`${isSummaryOpen}`;
        shippingContainer.dataset.display=`${isShippingOpen}`;
        summaryChevron.dataset.display=`${isSummaryOpen}`;
        shippingChevron.dataset.display=`${isShippingOpen}`;
    } else if (section === 'shipping') {
        isSummaryOpen = false;
        isBillingOpen = false;
        showBilling.innerHTML = 'Show Details';
        showSummary.innerHTML = 'Show Details';
        summaryContainer.dataset.display=`${isSummaryOpen}`;
        billingContainer.dataset.display=`${isBillingOpen}`;
        summaryChevron.dataset.display=`${isSummaryOpen}`;
        billingChevron.dataset.display=`${isBillingOpen}`;
    }
}

summarySection.addEventListener('click', () => {
    closeOthers('summary')
    isSummaryOpen = !isSummaryOpen;
    if (isSummaryOpen) {
        showSummary.innerHTML = 'Hide Details';
    }
    else {
        showSummary.innerHTML = 'Show Details';
    }
    summaryContainer.dataset.display=`${isSummaryOpen}`;
    summaryChevron.dataset.display=`${isSummaryOpen}`;    
});

billingSection.addEventListener('click', () => {
    closeOthers('billing')
    isBillingOpen = !isBillingOpen;
    if (isBillingOpen) {
        showBilling.innerHTML = 'Hide Details';
    }
    else {
        showBilling.innerHTML = 'Show Details';
    }
    billingContainer.dataset.display=`${isBillingOpen}`;
    billingChevron.dataset.display=`${isBillingOpen}`;
});

shippingSection.addEventListener('click', () => {
    closeOthers('shipping')
    showShipping.innerHTML = 'Hide Details';
    isShippingOpen = !isShippingOpen;
    if (isShippingOpen) {
        showShipping.innerHTML = 'Hide Details';
    }
    else {
        showShipping.innerHTML = 'Show Details';
    }
    shippingContainer.dataset.display=`${isShippingOpen}`;
    shippingChevron.dataset.display=`${isShippingOpen}`;
});

const checkoutButton = document.getElementById('checkout-button');
const requiredCheckoutFields = document.getElementById('checkout-form').querySelectorAll("[required]");
const errorMessage = document.getElementById('error-message');

function checkRequiredFields(requiredFields) {
    for (let i = 0; i < requiredFields.length; i++) {
        field = requiredFields[i];
        if (field.hasAttribute("pattern")) {
            const pattern = new RegExp(field.getAttribute("pattern"));
            if (!pattern.test(field.value)) {
                checkoutButton.title = `Please fill out ${field.name} correctly`;
                return false;
            }
        }
        else {
            if (field.value === "") {
                checkoutButton.title = `Please fill out ${field.name}`;
                return false;
            }
        }
    }
    errorMessage.innerHTML = "";
    return true;
}

requiredCheckoutFields.forEach((field) => { 
    field.addEventListener('keydown', () => {
        setTimeout(() => {
            if (checkRequiredFields(requiredCheckoutFields)) {
                checkoutButton.removeAttribute('disabled');
            } else {
                checkoutButton.setAttribute('disabled', 'disabled');
            }
        }, 0)
    });
});
