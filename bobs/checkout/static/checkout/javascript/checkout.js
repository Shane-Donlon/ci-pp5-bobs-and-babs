let delivery = document.querySelector(".delivery-charge-price > data");
let deliverValue = delivery.value;
let deliveryPrice = parseFloat(deliverValue);
let totalCheckoutPrice = document.querySelector(".total-checkout-price");
let radioBtns = document.querySelectorAll(".delivery-method-radio");
let deliveryPriceElement = document.querySelector(".delivery-charge-price");
let deliveryWrapper = document.querySelector(".subtotal-inc-delivery");
let originalPrice = document.querySelector(".total-checkout-price > data");
let html;

radioBtns.forEach((btn) => {
  // updates the delivery price based on the radio button selected
  btn.addEventListener("input", (e) => {
    let btnSelected = e.target.value;
    if (btnSelected === "collection") {
      let priceForDelivery = 0;
      delivery.value = priceForDelivery;
      let currentPrice = document.querySelector(".total-checkout-price > data");
      let originalPriceAsNumber = parseFloat(originalPrice.value);
      let currentPriceAsNumber = parseFloat(currentPrice.value);
      deliveryPriceElement.textContent = `€${priceForDelivery.toFixed(2)}`;
      if (originalPriceAsNumber != currentPriceAsNumber) {
        html = `<p>Total:</p>
        <p class="total-checkout-price">
            <data value="${originalPriceAsNumber.toFixed(
              2
            )}">€${originalPriceAsNumber.toFixed(2)}</data>
        </p>`;
        deliveryWrapper.innerHTML = html;
      }

      return;
    }
    if (btnSelected === "delivery") {
      delivery.value = deliveryPrice;
      deliveryPriceElement.textContent = `€${deliveryPrice.toFixed(2)}`;
      let price = parseFloat(deliveryPrice + +total);
      price = price.toFixed(2);
      html = `<p>Total:</p>
      <p class="total-checkout-price">
          <data value="${price}">€${price}</data>
      </p>`;
      deliveryWrapper.innerHTML = html;

      return;
    }
  });
});

let quantityInput = document.querySelectorAll(".cart-main-col-2 input");
quantityInput.forEach((input) => {
  input.setAttribute("disabled", "true");
});

const stripe = Stripe(
  "pk_test_51PJYG3HByftY2T6IfoqBjGHqW61IszSUjx2nqgtMqigIyOqYK69LD1GbetyAnFsYR9l3p328nvC8S1GcggGO0g3g00rd5nKEE6"
);

// Pass the appearance object to the Elements instance
let total = document
  .querySelector(".total-checkout-price > data")
  .getAttribute("value");

const elements = stripe.elements({
  fonts: [
    {
      cssSrc: "https://fonts.googleapis.com/css?family=Roboto",
    },
  ],

  locale: "auto",
});

const nameOnCard = document.querySelector("#full-name");
const WindowStyle = window.getComputedStyle(nameOnCard);
let inputBgColor = WindowStyle.backgroundColor;
let inputColor = WindowStyle.color;
let inputPlaceholderColor = WindowStyle.placeholder;
let inputFont = WindowStyle.fontFamily;
let fontSize = WindowStyle.fontSize;
let fontSmoothing = WindowStyle.fontSmoothing;

if (inputBgColor !== "rgb(255, 255, 255)") {
  // get computed style doesn't seem to work correctly for dark mode input background color
  // returns wrong color value works find in light mode
  inputBgColor = "#3b3b3b";
}
const style = {
  base: {
    backgroundColor: inputBgColor,
    color: inputColor,

    fontFamily: inputFont,
    fontSmoothing: fontSmoothing,
    fontSize: fontSize,
    "::placeholder": {
      color: inputPlaceholderColor,
    },
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a",
  },
};
const card = elements.create("card", { style: style, hidePostalCode: true });
card.mount("#card-element");

function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  const form = document.getElementById("payment-form");
  const hiddenInput = document.createElement("input");
  hiddenInput.setAttribute("type", "hidden");
  hiddenInput.setAttribute("name", "stripeToken");
  hiddenInput.setAttribute("value", token.id);
  form.appendChild(hiddenInput);

  const formData = new FormData(form);
  let cost = document.querySelector(".total-checkout-price").textContent;
  cost = cost.replace("€", "").trim();

  let deliveryBtn = document.querySelector("#delivery");

  const object = { cost: cost, delivery: deliveryBtn.checked };
  formData.forEach(function (value, key) {
    object[key] = value;
  });

  const formInput = JSON.stringify(object);

  makeRequest(form.action, "POST", formInput)
    .then((data) => {
      console.log(data);
      if (data.redirect_url) {
        window.location.href = data.redirect_url;
      }
      if (data.error) {
        createNotification(data.error, "error");
      }
    })
    .catch((error) => {
      createNotification(error, "error");
    });
}

let debouncedHandler = debounce(function () {
  stripe.createToken(card).then(function (result) {
    if (result.error) {
      createNotification(result.error.message, "error");
    } else {
      // Send the token to server, and send post request
      stripeTokenHandler(result.token);
    }
  });
}, 250);

function handleClick(event) {
  debouncedHandler();
}

let submitBtn = document.querySelector("#submit-btn");
submitBtn.addEventListener("click", (event) => {
  event.preventDefault();
  let name = document.querySelector("#full-name");
  let email = document.querySelector("#email");
  if (name.reportValidity() && email.reportValidity()) {
    handleClick(event);
  }
});
