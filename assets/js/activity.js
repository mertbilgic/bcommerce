var productCard = null;

function cloneDiv(id) {
  let div = document.getElementById(id);

  return div.cloneNode(true);
}
function addCartButton() {
  var addToCartDiv = document.createElement("div");
  addToCartDiv.className = "addToCart";
  addToCartDiv.id = "addToCart";

  var addToCartBtn = document.createElement("a");
  addToCartBtn.innerHTML = "Add To Cart";
  addToCartBtn.className = "btn";

  addToCartDiv.appendChild(addToCartBtn);
  document.getElementById("productCardPrice").appendChild(addToCartDiv);
}

document.getElementById("productCard").onmouseover = function () {
  productCard = cloneDiv("productPrice");
  document.getElementById("productPrice").remove();
  addCartButton();
};
document.getElementById("productCard").onmouseout = function () {
  document.getElementById("addToCart").remove();
  document.getElementById("productCardPrice").appendChild(productCard);
};
