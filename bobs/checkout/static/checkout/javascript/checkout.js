window.addEventListener("resize", (e) => {
  let section = document.querySelector("section");
  let left = section.getBoundingClientRect().left;
  console.log(left);
  //   document.body.style.setProperty("--left", left + "px");
});
