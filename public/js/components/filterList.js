function filterList(filterValue, list) {
  let foundResults = false;

  for (i = 0; i < list.length; i++) {
    const searchterms = list[i].dataset.searchterms;

    if (searchterms.toLowerCase().indexOf(filterValue.toLowerCase()) > -1) {
      list[i].classList.remove("hidden");
      foundResults = true;
    } else {
      list[i].classList.add("hidden");
    }
  }

  if (!foundResults) {
    document.getElementById("NoResultsFound").classList.remove("hidden");
  } else {
    document.getElementById("NoResultsFound").classList.add("hidden");
  }
}
