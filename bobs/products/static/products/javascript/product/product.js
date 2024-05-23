let input = document.querySelector("#quantity");
let minOnLOad = input.min;
let maxOnLoad = input.max;
const data = document.currentScript.dataset;

input.addEventListener("input", (e) => {
  const validityState = input.validity;
  const min = input.min;
  const max = input.max;
  if (!validityState.valid) {
    input.reportValidity();
    return;
  }

  // let sourceChanged = validateSourceMinMax(min, max);
  // if (sourceChanged) {
  //   window.alert("You can't change the min and max values of the input.");
  //   window.alert("Please refresh the page to reset the input.");
  //   input.value = 1;
  // }
});

function validateSourceMinMax(min, max) {
  if (min != minOnLOad || max != maxOnLoad) {
    return true;
  }
}
let addToCartButton = document.querySelector(".add-to-cart");
const slug = addToCartButton.getAttribute("data-product-name-as-slug");
const link = `/products/${slug}/cart/add/`;

addToCartButton.addEventListener(
  "click",
  debounce((e) => {
    const validityState = input.validity.valid;
    let type;
    let message;
    if (validityState) {
      let quantity = input.value;
      let productId = slug;
      let body = generateData(productId, quantity, "add");
      let response = makeRequest(link, "POST", body);
      response.then((data) => {
        if (data.success) {
          message = data.success;
          type = "success";
          createNotification(message, type);
          return;
        }
        if (data.error) {
          message = data.error;
          type = "error";
          createNotification(message, type);
          return;
        }
      });
    }
    if (!validityState) {
      input.reportValidity();
    }
  }, 300)
); // debounce time
