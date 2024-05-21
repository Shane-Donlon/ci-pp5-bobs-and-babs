let allBtns = document.querySelectorAll(".del-btn");
let links = document.querySelectorAll("[data-slug]");
let total = document.querySelector(".total-cart");
allBtns.forEach((btn, index) => {
  btn.addEventListener(
    "click",
    debounce((e) => {
      let slug = links[index].getAttribute("data-slug");
      productId = links[index].getAttribute("data-product-id");
      let url = `update/${slug}/`;
      let transactionId = document.querySelector(".transaction-id").textContent;

      let body = generateOrder(
        productId,
        (quantity = 0),
        "remove",
        transactionId
      );
      let response = makeRequest(url, "POST", body);
      response.then((data) => {
        if (data.success) {
          createNotification(data.success, "success");
          let getRequest = makeRequest("", "GET");
          getRequest.then((data) => {
            let selectedEl = document.querySelectorAll(`.cart-grid > .${slug}`);
            selectedEl.forEach((el) => {
              let transitionTime = "250ms";
              transitionAndRemoveElement(el, transitionTime);
            });

            let cartTotal = JSON.parse(data.order)[0].fields.cart_total;
            total.innerHTML = `<data value="${cartTotal}">€${cartTotal}</data>`;
          });

          return;
        }
        if (data.error) {
          createNotification(data.error, "error");
          return;
        }
      });
    }, 300)
  ); // debounce time
});

function generateOrder(productId, quantity, actionType, transactionId) {
  // this function is called in cart and product js files
  let cartBody = new Object();
  cartBody["productId"] = productId;
  cartBody["quantity"] = quantity;
  cartBody["action"] = actionType;
  cartBody["transactionId"] = transactionId;
  let bodyJson = JSON.stringify({ cart: cartBody });
  return bodyJson;
}

function transitionAndRemoveElement(el, transitionTime) {
  el.style.transition = `height ${transitionTime} linear`;

  el.style.opacity = "0";
  let elHeight = el.offsetHeight;

  el.style.height = `${elHeight}px`;

  el.offsetHeight;

  el.style.height = "0px";

  el.addEventListener(
    "transitionend",
    function transitionEnd(event) {
      if (event.propertyName === "height") {
        el.remove();
        el.removeEventListener("transitionend", transitionEnd, false);
      }
    },
    false
  );
}
