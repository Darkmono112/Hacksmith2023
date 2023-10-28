const summarySection = document.getElementById('summary');
const billingSection = document.getElementById('billing');
const shippingSection = document.getElementById('shipping');

const summaryContainer = document.getElementById('summary-container');
const billingContainer = document.getElementById('billing-container');
const shippingContainer = document.getElementById('shipping-container');

const summaryChevron = document.getElementById('summary-chevron');
const billingChevron = document.getElementById('billing-chevron');
const shippingChevron = document.getElementById('shipping-chevron');

let isSummaryOpen = false;
let isBillingOpen = false;
let isShippingOpen = false;

function closeOthers(section) {
    if (section === 'summary') {
        isBillingOpen = false;
        isShippingOpen = false;
        billingContainer.dataset.display=`${isBillingOpen}`;
        shippingContainer.dataset.display=`${isShippingOpen}`;
        billingChevron.dataset.display=`${isBillingOpen}`;
        shippingChevron.dataset.display=`${isShippingOpen}`;
    } else if (section === 'billing') {
        isSummaryOpen = false;
        isShippingOpen = false;
        summaryContainer.dataset.display=`${isSummaryOpen}`;
        shippingContainer.dataset.display=`${isShippingOpen}`;
        summaryChevron.dataset.display=`${isSummaryOpen}`;
        shippingChevron.dataset.display=`${isShippingOpen}`;
    } else if (section === 'shipping') {
        isSummaryOpen = false;
        isBillingOpen = false;
        summaryContainer.dataset.display=`${isSummaryOpen}`;
        billingContainer.dataset.display=`${isBillingOpen}`;
        summaryChevron.dataset.display=`${isSummaryOpen}`;
        billingChevron.dataset.display=`${isBillingOpen}`;
    }
}

summarySection.addEventListener('click', () => {
    closeOthers('summary')
    isSummaryOpen = !isSummaryOpen;
    summaryContainer.dataset.display=`${isSummaryOpen}`;
    summaryChevron.dataset.display=`${isSummaryOpen}`;    
});

billingSection.addEventListener('click', () => {
    closeOthers('billing')
    isBillingOpen = !isBillingOpen;
    billingContainer.dataset.display=`${isBillingOpen}`;
    billingChevron.dataset.display=`${isBillingOpen}`;
});

shippingSection.addEventListener('click', () => {
    closeOthers('shipping')
    isShippingOpen = !isShippingOpen;
    shippingContainer.dataset.display=`${isShippingOpen}`;
    shippingChevron.dataset.display=`${isShippingOpen}`;
});