let input = document.querySelector("#quantity");
let min_on_load = input.min;
let max_on_load = input.max;

input.addEventListener("input", (e) => {
  const validityState = input.validity;
  const min = input.min;
  const max = input.max;
  if (!validityState.valid) {
    input.reportValidity();
    return;
  }

  let sourceChanged = validateSourceMinMax(min, max);
  if (sourceChanged) {
    window.alert("You can't change the min and max values of the input.");
    window.alert("Please refresh the page to reset the input.");
    input.value = 1;
  }
});

function validateSourceMinMax(min, max) {
  if (min != min_on_load || max != max_on_load) {
    return true;
  }
}
