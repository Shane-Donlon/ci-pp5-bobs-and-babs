let allerginInput = document.querySelector("[name='allergin_info']");
let regexAllergin = /contains:|may contain:/gim;
let errorObject = {
  id_allergin_info:
    "The allergin info must contain the word 'contains:' and 'may contain:' to be valid. </br> Example: contains: peanuts, may contain: nuts",
};
allerginInput.addEventListener("change", (e) => {
  let allerginInfo = e.target.value;
  if (!regexAllergin.test(allerginInfo)) {
    createNotification(
      "The allergin info must contain the word 'contains:' and 'may contain:' to be valid. </br> Example: contains: peanuts, may contain: nuts",
      "error"
    );
  }
});

function validateProfileFormOnChangeObject(input, object) {
  // object = {html_id_of_input:"error message"}

  if (input.validity.patternMismatch) {
    let errorMessage = object[input.id];
    if (errorMessage != undefined) {
      input.setCustomValidity(errorMessage);

      input.addEventListener("input", (e) => {
        if (!input.validity.patternMismatch) {
          input.setCustomValidity("");
        }
      });
    }
  }

  return input.reportValidity();
}

let submitButton = document.querySelector("button[type=submit]");
let allInputs = document.querySelectorAll("label + *");
allInputs.forEach((input) => {
  input.addEventListener("change", (e) => {
    validateProfileFormOnChangeObject(input, errorObject);
  });
});
let url = document.querySelector("form").action;
submitButton.addEventListener("click", (e) => {
  e.preventDefault(); // Prevent the form from being submitted normally
  let valid = true;
  let errorMessages = [];
  allInputs = document.querySelectorAll("label + *");
  for (let input of allInputs) {
    validateProfileFormOnChangeObject(input, errorObject);
    if (!validateProfileFormOnChangeObject(input, errorObject)) {
      valid = false;

      break;
    }
    if (input.id === "id_allergin_info") {
      if (!regexAllergin.test(input.value)) {
        errorMessages.push(
          "The allergin info must contain the word 'contains:' and 'may contain:' to be valid. </br> Example: contains: peanuts, may contain: nuts"
        );
        valid = false;
        break;
      }
    }
  }

  if (errorMessages.length > 0) {
    createNotification(errorMessages.join("</br>"), "error");
  }

  let form = document.querySelector("form");
  let formData = new FormData(form);

  if (valid) {
    console.log(formData);
    sendFormWithFile(url, "POST", formData).then((data) => {
      if (data.success) {
        createNotification(`${data.success}`, "success");
        return;
      }
      if (data.error) {
        createNotification(`${data.error}`, "error");
        return;
      }
    });
  }
});

async function sendFormWithFile(url, requestType, body) {
  // this function is called in cart and product js files
  let headersObj = {
    "X-Requested-With": "XMLHttpRequest",
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
