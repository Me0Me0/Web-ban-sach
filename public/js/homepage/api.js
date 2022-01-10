async function showNewProduct() {
    const res = await fetch('/api/products/newest?limit=10', { method: 'POST' });
    const items = await res.json();

    console.log(items)

    for (let { __data__: item } of items) {
        const template = document.querySelector("#new-arrivals-item-template");
        const clone = document.importNode(template.content, true);

        clone.querySelector(".item").dataset.id = item.id;
        // clone.querySelector(".item-img > img").src = "https://i.pinimg.com/736x/53/38/f8/5338f8f34d04e94e076d1d2e6d2350a0.jpg";
        clone.querySelector(".price > p").textContent = item.price;
        clone.querySelector(".title > a").textContent = item.name;
        clone.querySelector(".detail").href = `/products/${item.id}`;
        clone.querySelector(".title > a").href = `/products/${item.id}`;
        document.querySelector(".new-arrivals.item-list").appendChild(clone);
    }
}


showNewProduct()