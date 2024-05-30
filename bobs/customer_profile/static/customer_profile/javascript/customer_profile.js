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
    const object = {};
    formData.forEach(function (value, key) {
      object[key] = value;
    });
    let url = "/profile/update/";
    let formObject = {
      order: object,
    };
    let formInput = JSON.stringify(formObject);

    makeRequest(url, "POST", formInput)
      .then((data) => {
        if (data.success) {
          createNotification(data.success, "success");
        }
        if (data.error) {
          createNotification(data.error, "error");
        }
      })
      .catch((error) => {
        createNotification(error, "error");
      });
  }
});

allInputsProfileForm.forEach((input) => {
  input.addEventListener("change", (e) => {
    validateProfileFormOnChangeObject(input, errorMessageObject);
  });
});

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
