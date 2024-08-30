function filterList(filterValue, list) {
  if (filterValue === "") {
    document.getElementById("NoResultsFound").classList.add("hidden");
    return;
  }

  let foundResults = false;

  for (i = 0; i < list.length; i++) {
    try {
      const searchterms = list[i].dataset.searchterms;

      if (searchterms.toLowerCase().indexOf(filterValue.toLowerCase()) > -1) {
        list[i].classList.remove("hidden");
        foundResults = true;
      } else {
        list[i].classList.add("hidden");
      }
    } catch {
      // no searchterms probably
    }
  }

  if (!foundResults) {
    document.getElementById("NoResultsFound").classList.remove("hidden");
  } else {
    document.getElementById("NoResultsFound").classList.add("hidden");
  }
}
