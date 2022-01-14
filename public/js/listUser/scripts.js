const pageItems = document.querySelectorAll(".page-item");
const pagePrev = document.querySelector(".page-prev");
const pageNext = document.querySelector(".page-next");

const urlSearchParams = new URLSearchParams(window.location.search);
const currentPage = Number(urlSearchParams.get("page")) || 1;

const limit = 5;
const skip = (currentPage - 1) * limit;


function searchNotFoundView() {
    const template = document.querySelector("#search-not-found-template").content;
    const clone = template.cloneNode(true);

    document.querySelector("#product-list").appendChild(clone);
}

async function getUsers() {
    const params = new URLSearchParams(window.location.search);

    params.set("limit", limit * 5);
    params.set("skip", skip);
    params.delete("page");

    const res = await fetch(`/api/users?${params.toString()}`);
    const data = await res.json();
    return data
}


async function showUsers() {
    let data = await getUsers();

    if (data.length == 0 && currentPage != 1) {
        urlSearchParams.set("page", 1);
        window.location.search = urlSearchParams;
    }
    
    if (data.length == 0) {
        searchNotFoundView();
        pageNext.remove();
        pagePrev.remove();
        pageItems.forEach(page => page.remove());

        return;
    }

    let remain = data.splice(limit, data.length - limit);

    showPagination(remain.length);

    for (const user of data) {
        const template = document.querySelector("#user-template").content;
        const clone = template.cloneNode(true);

        clone.querySelector("#user-id").textContent = user.id;
        clone.querySelector("#username").textContent = user.username;
        clone.querySelector("#fullname").textContent = user.name;
        clone.querySelector("#user-detail").href += user.id;
        clone.querySelector("#user-status").textContent = user.deleted_at ? "Đã xóa" : "Đang hoạt động";

        document.querySelector("#user-list").appendChild(clone);
    }
}


function showPagination(remainLen) {
    if (remainLen === 0) {
        pageNext.remove();
    }
    if (currentPage === 1) {
        pagePrev.remove();
    }

    if (currentPage <= 4) {
        pageItems[currentPage - 1].querySelector("a").classList.add("active");
        let extraPage = Math.ceil(remainLen / limit);
        
        if (currentPage + extraPage > 5) {
            extraPage = 5 - currentPage;
        }

        for (let i = currentPage + extraPage + 1; i <= 5; i++) {
            pageItems[i - 1].remove();
        }
    } 
    else {
        pageItems[pageItems.length - 1].querySelector("a").classList.add("active");
        let temp = currentPage;
        for (let i = pageItems.length - 1; i >= 0; i--) {
            pageItems[i].querySelector("a").textContent = temp;
            temp--;
        }
    }

    // page click
    [...pageItems].forEach(page => {
        page.addEventListener("click", function (e) {
            urlSearchParams.set("page", e.target.textContent);
            window.location.search = urlSearchParams;
        })
    });
    // prev click
    pagePrev.addEventListener("click", function (e) {
        urlSearchParams.set("page", currentPage - 1);
        window.location.search = urlSearchParams;
    });
    // next click
    pageNext.addEventListener("click", function (e) {
        urlSearchParams.set("page", currentPage + 1);
        window.location.search = urlSearchParams;
    });
}

showUsers();


