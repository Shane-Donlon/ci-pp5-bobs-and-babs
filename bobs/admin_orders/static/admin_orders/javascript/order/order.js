let submitBtn = document.querySelector(".submit");
submitBtn.addEventListener("click", (e) => {
  e.preventDefault();
  let url = form.action;
  let body = new FormData(form);
  let requestType = "POST";
  makeRequest(url, requestType, body).then((data) => {
    if (data.redirect) {
      window.location.href = `${data.redirect}`;
    } else {
      createNotification(data.message, "error");
    }
  });
});
