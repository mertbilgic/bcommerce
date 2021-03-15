var productCard = null;

function cloneDiv(id) {
  let div = document.getElementById(id).getElementsByClassName('productPrice')[0];

  return div.cloneNode(true);
}
function addCartButton(id) {
  var addToCartDiv = document.createElement("div");
  addToCartDiv.className = "addToCart";
  addToCartDiv.id = "addToCart";

  var addToCartBtn = document.createElement("a");
  addToCartBtn.innerHTML = "Add To Cart";
  addToCartBtn.className = "btn";

  addToCartDiv.appendChild(addToCartBtn);
  document.getElementById(id).appendChild(addToCartDiv);
}

function CardBtnShow(id) {
  productCard = cloneDiv(id);
  document.getElementById(id).getElementsByClassName('productPrice')[0].remove();
  addCartButton(id);
};
function priceShow(id) {
  document.getElementById(id).getElementsByClassName('addToCart')[0].remove();
  document.getElementById(id).appendChild(productCard);
};
