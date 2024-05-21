let allBtns = document.querySelectorAll(".del-btn");
let links = document.querySelectorAll("[data-slug]");

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
            console.log(data.order);
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
