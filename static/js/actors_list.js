function getShowsForActor(id) {
    fetch("/actors/" + id).then(response => response.json()).then(function (data) {
        let displayed = document.getElementsByClassName("displayed")

        if (displayed[0] && displayed[0].parentNode.id === id.toString()) {
            removeElement(displayed)
        } else {
            if (displayed[0]) {
                removeElement(displayed)
            }
            appendElements(id, data)
        }
    })
}

function appendElements(id, data) {
    for (let i = 0; i < data['actor_list'].length; i++) {
        let list = document.getElementById(id)
        let ul = document.createElement("ul")
        ul.classList.add("displayed")
        let li = document.createElement("li")
        li.innerHTML = data['actor_list'][i]['title']
        ul.appendChild(li)
        list.appendChild(ul)
    }
}

function removeElement(displayed) {
    for (let i = displayed.length - 1; i >= 0; i--) {
        displayed[i].remove()
    }
}


