window.addEventListener("DOMContentLoaded", (e) => {
  // if the user is on the home page update the href attribute of the about us link as to avoid a page refresh
  if (document.body.contains(document.querySelector("#about-us-link"))) {
    let aboutUsLink = document.querySelector("#about-us-link");
    aboutUsLink.setAttribute("href", "#about-us");
  }

  // set the css variable for the nav height so that the nav does not cover the content
  let navWrapper = document.querySelector(".nav-wrapper");
  let height = navWrapper.getBoundingClientRect().height;
  document.body.style.setProperty("--nav-height", `${height}px`);
});
