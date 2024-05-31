let delivery = document.querySelector(".delivery-charge-price > data");
let deliverValue = delivery.value;
let deliveryPrice = parseFloat(deliverValue);
let totalCheckoutPrice = document.querySelector(".total-checkout-price");
let radioBtns = document.querySelectorAll(".delivery-method-radio");
let deliveryPriceElement = document.querySelector(".delivery-charge-price");
let deliveryWrapper = document.querySelector(".subtotal-inc-delivery");
let originalPrice = document.querySelector(".total-checkout-price > data");
let paymentForm = document.querySelector("#payment-form");
let html;
let emailData;
window.addEventListener("load", (event) => {
  // <input class="InputElement is-empty Input Input--empty" autocomplete="cc-number" autocorrect="off" spellcheck="false" type="text" name="cardnumber" data-elements-stable-field-name="cardNumber" inputmode="numeric" aria-label="Credit or debit card number" placeholder="Card number" aria-invalid="false" tabindex="0" value="">
});

radioBtns.forEach((btn) => {
  // updates the delivery price based on the radio button selected
  btn.addEventListener("input", (e) => {
    let btnSelected = e.target.value;

    let deliveryForm = document.querySelector(".delivery-form");

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
      if (deliveryForm.classList.contains("delivery-form-visible")) {
        deliveryForm.classList.remove("delivery-form-visible");
        deliveryForm.removeAttribute("aria-expanded");
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
      if (!deliveryForm.classList.contains("delivery-form-visible")) {
        // show delivery form
        // TODO: work on transitioning from display none
        deliveryForm.classList.add("delivery-form-visible");
        deliveryForm.setAttribute("aria-expanded", "true");
      }
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
let placeholder;
if (inputBgColor !== "rgb(255, 255, 255)") {
  // get computed style doesn't seem to work correctly for dark mode input background color
  // returns wrong color value works find in light mode
  inputBgColor = "#2b2a33";
  placeholder = "#ffffff";
} else {
  placeholder = "#000000";
}
const style = {
  base: {
    backgroundColor: inputBgColor,
    color: inputColor,
    fontFamily: inputFont,
    fontSmoothing: fontSmoothing,
    fontSize: fontSize,
    "::placeholder": {
      color: placeholder,
    },
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a",
  },
};
const card = elements.create("card", { style: style, hidePostalCode: true });
card.mount("#card-element");
if (card.mount) {
}
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

  if (
    document.body.contains(document.querySelector(".delivery-form-visible"))
  ) {
    let deliveryForm = document.querySelector(".delivery-form-visible");
    let deliveryData = new FormData(deliveryForm);

    emailData = {};
    deliveryData.forEach(function (value, key, index) {
      emailData[`${key}`] = value;
    });
  }

  let formInput;
  // const formInput = JSON.stringify(object);
  if (emailData != undefined) {
    let combinedData = {
      order: object,
      email: emailData,
    };
    formInput = JSON.stringify(combinedData);
  } else {
    let formObject = {
      order: object,
    };
    formInput = JSON.stringify(formObject);
  }

  makeRequest(form.action, "POST", formInput)
    .then((data) => {
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

card.addEventListener("change", function (event) {
  let displayError = document.createElement("div");
  displayError.style.color = "red";
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = "";
  }

  paymentForm.appendChild(displayError);
  setTimeout(() => {
    displayError.remove();
  }, 5000);
});

let submitBtn = document.querySelector("#submit-btn");
submitBtn.addEventListener("click", (event) => {
  event.preventDefault();

  let name = document.querySelector("#full-name");
  let email = document.querySelector("#email");
  if (
    document.body.contains(document.querySelector(".delivery-form-visible"))
  ) {
    let valid = formValidation(".delivery-form-visible");
    if (!valid) {
      return;
    }
  }

  if (name.reportValidity() && email.reportValidity()) {
    if (card._empty) {
      let cardError = document.createElement("div");
      cardError.textContent = "Card, Expire Date, and CVC are all required";
      cardError.style.color = "red";
      paymentForm.appendChild(cardError);
      setTimeout(() => {
        cardError.remove();
      }, 5000);
      return;
    }

    handleClick(event);
  }
});

function formValidation(formSelector) {
  // given the conditional nature of the form, validation only occurs on submit and if the delivery method is delivery
  let valid;
  let invalidInputs = [];
  let allInputs = document.querySelectorAll(`${formSelector} label + *`);
  let allLabels = document.querySelectorAll(`${formSelector} label`);
  let containsEircode;

  for (let index = 0; index < allInputs.length; index++) {
    const input = allInputs[index];
    input.setCustomValidity("");

    if (input.id === "id_eircode") {
      containsEircode = true;
      if (containsEircode) {
        let eircode = document.querySelector("#id_eircode");
        formatEircode(eircode.value, eircode);
        if (input.id === "id_eircode") {
          let eircode = document.querySelector("#id_eircode");
          formatEircode(eircode.value, eircode);
          if (eircode.validity.patternMismatch) {
            let message = "Please enter a valid Eircode format e.g. A65 F4E2";
            input.setCustomValidity(message);
            input.addEventListener("input", (e) => {
              if (!e.target.validity.patternMismatch) {
                input.setCustomValidity("");
              }
            });
          }
        }
      }
    }
    if (input.id === "id_phone") {
      let phone = document.querySelector("#id_phone");

      if (phone.validity.patternMismatch) {
        let message = phone.validationMessage;

        if (message.includes("format")) {
          message = "Please enter a valid phone number eg. 353871234567";
          input.setCustomValidity(message);
          input.addEventListener("input", (e) => {
            if (!e.target.validity.patternMismatch) {
              input.setCustomValidity("");
            }
          });
        }
      }
    }

    input.reportValidity();
    if (!input.reportValidity()) {
      invalidInputs.push(false);
      break;
    }
  }
  formValid = invalidInputs.length > 0 ? false : true;
  return formValid;
}

function formatEircode(eircode, eircodeInput) {
  eircode = eircode.trim();
  if (eircode.at(3) != " ") {
    eircode = eircode.split("");
    eircode.splice(3, 0, " ");
    eircode = eircode.join("").toUpperCase();
    eircodeInput.value = eircode.trim();
  }
}
