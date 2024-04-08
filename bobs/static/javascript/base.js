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
