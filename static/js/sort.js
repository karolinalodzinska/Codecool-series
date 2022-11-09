function sortTable(head_id) {
    const titleHeader = document.getElementById(head_id);
    let direction;

    if (titleHeader.classList.contains("arrow-down")) {
        titleHeader.classList.remove("arrow-down")
        titleHeader.classList.add("arrow-up")
        direction = "asc"
    } else {
        titleHeader.classList.remove("arrow-up")
        titleHeader.classList.add("arrow-down")
        direction = "desc"
    }

    const titleHeaderParent = titleHeader.parentElement.children

    for (let i = 0; i < titleHeaderParent.length; i++) {
        if (titleHeaderParent[i].id !== head_id) {
            titleHeaderParent[i].classList.remove("arrow-down")
            titleHeaderParent[i].classList.remove("arrow-up")
        }
    }

    const tBody = document.getElementsByTagName("tbody")
    const tBodyElements = tBody[0]
    let rows = tBodyElements.children


    //sorting here
    if (head_id === 'title') {
        sortTitles(rows, direction, 0)
    }
    if (head_id === 'year') {
        sortDates(rows, direction, 1)
    }
    if (head_id === 'runtime') {
        sortRuntimeAndRating(rows, direction, 2)
    }
    if (head_id === 'rating') {
        sortRuntimeAndRating(rows, direction, 3)
    }
}


function sortRuntimeAndRating(rows, direction, th_n) {
    let switching, i, x, y, shouldSwitch
    switching = true

    while (switching) {
        switching = false;
        for (i = 0; i < (rows.length - 1); i++) {
            x = Number(rows[i].getElementsByTagName("td")[th_n].innerText);
            y = Number(rows[i + 1].getElementsByTagName("td")[th_n].innerText);

            if (direction === "asc") {
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            } else if (direction === "desc") {
                if (x < y) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}


function sortTitles(rows, direction, th_n) {
    let switching, i, x, y, shouldSwitch
    switching = true

    while (switching) {
        switching = false;
        for (i = 0; i < (rows.length - 1); i++) {
            x = rows[i].getElementsByTagName("td")[th_n].innerText;
            y = rows[i + 1].getElementsByTagName("td")[th_n].innerText;

            if (direction === "asc") {
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            } else if (direction === "desc") {
                if (x < y) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}


function sortDates(rows, direction, th_n) {
    let switching, i, x, y, shouldSwitch
    switching = true

    while (switching) {
        switching = false;
        for (i = 0; i < (rows.length - 1); i++) {
            x = Date.parse(rows[i].getElementsByTagName("td")[th_n].innerText);
            y = Date.parse(rows[i + 1].getElementsByTagName("td")[th_n].innerText);

            if (direction === "asc") {
                if (x > y) {
                    shouldSwitch = true;
                    break;
                }
            } else if (direction === "desc") {
                if (x < y) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}
