let delivery = document.querySelector(".delivery-charge-price > data");
let deliverValue = delivery.value;
let deliveryPrice = parseFloat(deliverValue);

let radioBtns = document.querySelectorAll(".delivery-method-radio");
let deliveryPriceElement = document.querySelector(".delivery-charge-price");

radioBtns.forEach((btn) => {
  // updates the delivery price based on the radio button selected
  btn.addEventListener("input", (e) => {
    let btnSelected = e.target.value;
    if (btnSelected === "collection") {
      let priceForDelivery = 0;
      delivery.value = priceForDelivery;

      deliveryPriceElement.textContent = `€${priceForDelivery.toFixed(2)}`;
      return;
    }
    if (btnSelected === "delivery") {
      delivery.value = deliveryPrice;
      deliveryPriceElement.textContent = `€${deliveryPrice.toFixed(2)}`;
      return;
    }
  });
});
