/* Created by Tivotal */

const priceInputs = document.querySelectorAll(".price-input input");
const rangeInputs = document.querySelectorAll(".range-input input");
const range = document.querySelector(".slider .progress");

let full_scale = rangeInputs[1].max - rangeInputs[0].min
let priceGap = full_scale * 0.1;

let minVal = parseInt(rangeInputs[0].value);
let maxVal = parseInt(rangeInputs[1].value);


if (full_scale === 0){
    rangeInputs[1].max = maxVal + 1
    rangeInputs[1].value = maxVal + 1
    range.style.left = 0 +"%";
    range.style.right = 0 + "%";
}

else {
  range.style.left = ((100 * (minVal - rangeInputs[0].min)) / full_scale) + "%";
  range.style.right =  ((100 * (rangeInputs[0].max - maxVal)) / full_scale) + "%";
}



priceInputs.forEach((input) => {
  input.addEventListener("input", (e) => {

    let minPrice = priceInputs[0].value === '' ? 0: parseInt(priceInputs[0].value)

    let maxPrice = parseInt(priceInputs[1].value);


    if ( minPrice >=rangeInputs[0].min && maxPrice - minPrice >= priceGap && maxPrice <= rangeInputs[1].max) {
      if (e.target.className === "min-input") {
        rangeInputs[0].value = minPrice;
        range.style.left = ((100 * (minPrice - rangeInputs[0].min)) / full_scale) + "%";
      } else {
        rangeInputs[1].value = maxPrice;
        range.style.right = ((100 * (rangeInputs[1].max - maxPrice)) / full_scale)+ "%";
      }
    }
    else {
      rangeInputs[0].value = rangeInputs[0].min;
      range.style.left = 0 + "%";
      rangeInputs[1].value = rangeInputs[0].max;
      range.style.right =  0 + "%";

    }
  });
});


rangeInputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    let minVal = parseInt(rangeInputs[0].value);
    let maxVal = parseInt(rangeInputs[1].value);

    if (maxVal - minVal < priceGap) {
      if (e.target.className === "min-range") {
        rangeInputs[0].value = maxVal - priceGap;
      } else {
        rangeInputs[1].value = minVal + priceGap;
      }
    } else {
      priceInputs[0].value = minVal;
      priceInputs[1].value = maxVal;
      range.style.left = ((100 * (minVal - rangeInputs[0].min)) / full_scale) + "%";
      range.style.right = ((100 * (rangeInputs[0].max - maxVal)) / full_scale)  + "%";
    }
  });
});
