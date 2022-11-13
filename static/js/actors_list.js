function getShowsForActor(id) {
    fetch("/actors/" + id).then(response => response.json()).then(function (data) {
        let displayedShows = document.getElementsByClassName("actor-shows")
        // usunięcie jeśli klikam w inny element listy
        if (displayedShows[0] && displayedShows[0].parentNode.id === id.toString()) {
            for (let i = displayedShows.length - 1; i >= 0; i--) {
                displayedShows[i].remove()
            }
            // usunięcie jeśli klikam w ten sam element listy drugi raz
        } else {
            if (displayedShows[0]) {
                for (let i = displayedShows.length - 1; i >= 0; i--) {
                    displayedShows[i].remove()
                }
            }
            // dodanie elementów
            for (let i = 0; i < data["actor_list"].length; i++) {
                let listElement = document.getElementById(id)
                let ul = document.createElement("ul")
                ul.classList.add("actor-shows")
                let li = document.createElement("li")
                li.innerHTML = data["actor_list"][i]["title"]
                ul.appendChild(li)
                listElement.appendChild(ul)
            }
        }
    })
}

