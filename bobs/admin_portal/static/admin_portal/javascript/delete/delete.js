let deleteForm = document.querySelector("form");
deleteForm.addEventListener("submit", (event) => {
  event.preventDefault();
  window.confirm("Are you sure you want to delete this product?");
  if (window.confirm) {
    let formData = new FormData(deleteForm);
    makeRequest(deleteForm.action, "DELETE", formData)
      .then((data) => {
        window.location.href = `${data.redirect}`;
      })
      .catch((error) => {});
  } else {
    return;
  }
});
