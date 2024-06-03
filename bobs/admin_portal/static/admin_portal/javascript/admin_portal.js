const data = document.currentScript.dataset;
if (data.success) {
  createNotification(data.success, "success");
}
