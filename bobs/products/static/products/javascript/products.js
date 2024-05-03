const allCards = document.querySelectorAll(".card");
const allInnerCards = document.querySelectorAll(".card-inner");
const allCardBack = document.querySelectorAll(".card-back");

allCards.forEach((card, index) => {
  const handleTransitionEnd = (e) => {
    const rotated = window
      .getComputedStyle(allInnerCards[index])
      .getPropertyValue("transform");

    if (rotated != "none") {
      allInnerCards[index].style.transition = "none";
      allInnerCards[index].style.transform = "rotateY(0deg)";
      setTimeout(() => {
        allInnerCards[index].removeAttribute("style");
      }, 5);
    }

    card.removeEventListener("transitionend", handleTransitionEnd);
  };

  card.addEventListener("transitionend", (e) => {
    const rotated = window
      .getComputedStyle(allInnerCards[index])
      .getPropertyValue("transform");

    if (rotated !== "none") {
      card.addEventListener("mouseleave", (e) => {
        let cardRightPosition = card.getBoundingClientRect().right;
        if (e.clientX > cardRightPosition) {
          allInnerCards[index].style.transform = "";
          allInnerCards[index].style.transform = "rotateY(360deg)";
          card.addEventListener("transitionend", handleTransitionEnd);
        }
      });
    }
  });
});
