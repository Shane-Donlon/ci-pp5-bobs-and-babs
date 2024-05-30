let submitBtnProfile = document.querySelector(".submit-btn-profile");
let allInputsProfileForm = document.querySelectorAll("label + *");
let errorMessageObject = {
  id_eircode: "Please enter a valid Eircode format e.g. A65 F4E2",
  id_phone: "Please enter a valid phone number eg. 353871234567",
};

submitBtnProfile.addEventListener("click", (e) => {
  e.preventDefault();

  if (validateProfileFormOnSubmit(allInputsProfileForm)) {
    let form = document.querySelector("#profile-form");
    let formData = new FormData(form);
    console.log(formData);
    // TODO: - send form data to the server
  }
});

allInputsProfileForm.forEach((input) => {
  input.addEventListener("change", (e) => {
    validateProfileFormOnChangeObject(input, errorMessageObject);
  });
});

function validateProfileFormOnChange(input) {
  if (input.id === "id_eircode") {
    if (input.validity.patternMismatch) {
      input.setCustomValidity(
        "Please enter a valid Eircode format e.g. A65 F4E2"
      );
      input.addEventListener("input", (e) => {
        if (!input.validity.patternMismatch) {
          input.setCustomValidity("");
        }
      });
    }
  }
  if (input.id === "id_phone") {
    if (input.validity.patternMismatch) {
      input.setCustomValidity(
        "Please enter a valid phone number eg. 353871234567"
      );
      input.addEventListener("input", (e) => {
        if (!input.validity.patternMismatch) {
          input.setCustomValidity("");
        }
      });
    }
  }
  //   input.reportValidity();
  return input.reportValidity();
}

function validateProfileFormOnSubmit(listOfInputs) {
  let isValid = true;
  listOfInputs.forEach((input) => {
    if (!validateProfileFormOnChangeObject(input, errorMessageObject)) {
      isValid = false;
    }
  });
  return isValid;
}

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
