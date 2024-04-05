const menuBtn = document.querySelector(".nav-btn");
const navUl = document.querySelector(".nav-ul");

const onTransitionEnd = (e) => {
  navUl.setAttribute("aria-hidden", "");
};

menuBtn.addEventListener("click", (e) => {
  navUl.classList.toggle("nav-open");

  if (navUl.classList.contains("nav-open")) {
    navUl.removeAttribute("aria-hidden");
    // Remove the event listener when the nav is open
    navUl.removeEventListener("transitionend", onTransitionEnd);
  }
  if (!navUl.classList.contains("nav-open")) {
    // Add the event listener when the nav is closed
    navUl.addEventListener("transitionend", onTransitionEnd);
  }
});

window.addEventListener("DOMContentLoaded", () => {
  const width = window.innerWidth;
  if (width <= 600) {
    navUl.setAttribute("aria-hidden", "");
  }
});
