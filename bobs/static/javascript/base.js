const menuBtn = document.querySelector(".nav-btn");
const navUl = document.querySelector(".nav-ul");
const regex = /\S+/im;

const onTransitionEnd = (e) => {
  navUl.setAttribute("aria-hidden", "");
};

menuBtn.addEventListener("click", (e) => {
  navUl.classList.toggle("nav-open");
  if (navUl.classList.contains("nav-open")) {
    navUl.removeAttribute("aria-hidden");
    navUl.setAttribute("aria-expanded", "true");
    navUl.focus();
    // Remove the event listener when the nav is open
    navUl.removeEventListener("transitionend", onTransitionEnd);
  }
  if (!navUl.classList.contains("nav-open")) {
    // Add the event listener when the nav is closed
    navUl.setAttribute("aria-expanded", "false");
    navUl.addEventListener("transitionend", onTransitionEnd);
  }
});

window.addEventListener("DOMContentLoaded", () => {
  // if the screen is less than 600px, hide the nav menu from screen readers automatically
  const width = window.innerWidth;
  if (width <= 600) {
    navUl.setAttribute("aria-hidden", "");
    navUl.setAttribute("aria-expanded", "false");
  }
});

// if the user has scrolled more than 50px from the top add class box-shadow-show to the header
const primaryHeader = document.querySelector("header");
const scrollWatcher = document.createElement("div");

scrollWatcher.setAttribute("data-scroll-watcher", "");
primaryHeader.before(scrollWatcher);

const navObserver = new IntersectionObserver(
  (entries) => {
    primaryHeader.classList.toggle(
      "box-shadow-show",
      !entries[0].isIntersecting
    );
  },
  { rootMargin: "50px 0px 0px 0px" }
);

navObserver.observe(scrollWatcher);

async function makeRequest(url, requestType, body) {
  // this function is called in cart and product js files
  let headersObj = {
    "X-Requested-With": "XMLHttpRequest",
    "Content-type": "application/json",
  };
  if (requestType.toLowerCase() != "get") {
    // != get covers post and delete requests
    let csrfValue = document.querySelector("[name=csrfmiddlewaretoken").value;
    headersObj["X-CSRFToken"] = csrfValue;
  }
  let response = await fetch(url, {
    method: requestType,
    headers: headersObj,
    body: body,
  });
  let data = await response.json();

  return data;
}

function generateData(productId, quantity, actionType) {
  // this function is called in cart and product js files
  let cartBody = new Object();
  cartBody[productId] = quantity;
  cartBody["action"] = actionType;
  let bodyJson = JSON.stringify({ cart: cartBody });
  return bodyJson;
}

function createNotification(message, type) {
  // this creates a popup notification for the user
  // called in cart and product js files
  let notification = document.createElement("span");
  if (type == "error") {
    type = "error-notification";
  }
  if (type == "success") {
    type = "success-notification";
  }
  notification.classList.add(type, "notification");
  notification.innerHTML = `<p>${message}</p>`;
  document.body.appendChild(notification);
  setTimeout(() => {
    notification.remove();
  }, 3000);
}

function debounce(func, wait) {
  // this will wait until the user stops before executing the function
  // primarily used for the add to cart button in the product page
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}
function removeLoader() {
  if (document.body.contains(document.querySelector(".loader"))) {
    const loader = document.querySelector(".loader");
    loader.remove();
  }
}

function addAstriksToRequiredFields() {
  // this function adds an asterisk to the required fields in the form
  const requiredFields = document.querySelectorAll("[required]");
  if (requiredFields) {
    requiredFields.forEach((field) => {
      if (field.id) {
        const label = document.querySelector(`label[for=${field.id}]`);
        if (label) {
          label.classList.add("labelRequiredAsterisk");
        }
      }
    });
  }
  return;
}

window.addEventListener("DOMContentLoaded", () => {
  addAstriksToRequiredFields();
});

function validateProfileFormOnChangeObject(input, object) {
  // object = {html_id_of_input:"error message"}
  if (input.validity.patternMismatch) {
    let errorMessage = object[input.id];

    if (errorMessage != undefined) {
      input.setCustomValidity(errorMessage);

      input.addEventListener("input", (e) => {
        if (!input.validity.valid) {
          input.setCustomValidity(errorMessage);
        }

        if (!input.validity.patternMismatch) {
          input.setCustomValidity("");
        }
      });
    }
  }

  return input.reportValidity();
}
