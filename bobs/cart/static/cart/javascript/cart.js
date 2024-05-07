let cartGrid = document.querySelector(".cart-area-container");

window.addEventListener("resize", function (e) {
  let width = window.innerWidth;
  if (width < 600) {
    cartGrid.classList.remove("breakout");
    cartGrid.classList.add("full-width");
    cartGrid.classList.add("full-width-container");

    return;
  }
  if (width >= 600) {
    cartGrid.classList.remove("full-width");
    cartGrid.classList.add("full-width-container");
    cartGrid.classList.add("breakout");
    return;
  }
});

function updateQuantity(maxQuantity) {
  for (let i = 1; i <= maxQuantity; i++) {
    let option = document.createElement("option");
    option.value = i;
    option.text = i;
    quantity.appendChild(option);
  }
}
