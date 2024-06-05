let deleteForm = document.querySelector("form");
deleteForm.addEventListener("submit", (event) => {
  event.preventDefault();
  if (window.confirm("Are you sure you want to delete this item?")) {
    let formData = new FormData(deleteForm);
    makeRequest(deleteForm.action, "DELETE", formData)
      .then((data) => {
        window.location.href = `${data.redirect}`;
      })
      .catch((error) => {console.error(error);});
  } else {
    return;
  }
});
