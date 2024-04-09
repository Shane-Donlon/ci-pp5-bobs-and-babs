const menuBtn = document.querySelector(".nav-btn");
const navUl = document.querySelector(".nav-ul");

const onTransitionEnd = (e) => {
  navUl.setAttribute("aria-hidden", "");
};

menuBtn.addEventListener("click", (e) => {
  navUl.classList.toggle("nav-open");
  if (navUl.classList.contains("nav-open")) {
    navUl.removeAttribute("aria-hidden");
    navUl.setAttribute("aria-expanded", "true");
    navUl.focus();
    // Remove the event listener when the nav is open
    navUl.removeEventListener("transitionend", onTransitionEnd);
  }
  if (!navUl.classList.contains("nav-open")) {
    // Add the event listener when the nav is closed
    navUl.setAttribute("aria-expanded", "false");
    navUl.addEventListener("transitionend", onTransitionEnd);
  }
});

window.addEventListener("DOMContentLoaded", () => {
  // if the screen is less than 600px, hide the nav menu from screen readers automatically
  const width = window.innerWidth;
  if (width <= 600) {
    navUl.setAttribute("aria-hidden", "");
    navUl.setAttribute("aria-expanded", "false");
  }
});

// if the user has scrolled more than 50px from the top add class box-shadow-show to the header
const primaryHeader = document.querySelector("header");
const scrollWatcher = document.createElement("div");

scrollWatcher.setAttribute("data-scroll-watcher", "");
primaryHeader.before(scrollWatcher);

const navObserver = new IntersectionObserver(
  (entries) => {
    primaryHeader.classList.toggle(
      "box-shadow-show",
      !entries[0].isIntersecting
    );
  },
  { rootMargin: "50px 0px 0px 0px" }
);

navObserver.observe(scrollWatcher);
