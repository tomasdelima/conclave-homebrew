"use strict";
const search = document.querySelector("#search");
const cards = [...document.querySelectorAll("article[data-search]")];
search.addEventListener("input", () => {
  const query = search.value.trim().toLowerCase();
  for (const card of cards) card.hidden = !card.dataset.search.includes(query);
  document.querySelector("#no-results").hidden = cards.some(card => !card.hidden);
});
for (const link of document.querySelectorAll("nav a")) {
  link.addEventListener("click", () => {
    search.value = "";
    for (const card of cards) card.hidden = false;
    document.querySelector("#no-results").hidden = true;
  });
}
