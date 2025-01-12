let cart = [];
let appliedPromoCode = null; // Track applied promo code

// Fetch and display products
async function fetchProducts(query = "") {
  const productList = document.getElementById("product-list");
  productList.innerHTML = "<p>Loading products...</p>";

  try {
    const response = await fetch("https://fakestoreapi.com/products");
    if (!response.ok) {
      throw new Error("Failed to fetch products");
    }
    const products = await response.json();

    const filteredProducts = query
      ? products.filter((product) =>
          product.title.toLowerCase().includes(query.toLowerCase())
        )
      : products;

    if (filteredProducts.length === 0) {
      productList.innerHTML = "<p>No products found.</p>";
    } else {
      displayProducts(filteredProducts);
    }
  } catch (error) {
    console.error("Error fetching products:", error);
    productList.innerHTML = "<p>Failed to load products.</p>";
  }
}

// Display products in the UI
function displayProducts(products) {
  const productList = document.getElementById("product-list");
  productList.innerHTML = "";

  products.forEach((product) => {
    const productCard = document.createElement("div");
    productCard.className = "col-md-4 mb-4";

    productCard.innerHTML = `
      <div class="card">
        <img src="${product.image}" class="card-img-top product-image" alt="${
      product.title
    }">
        <div class="card-body">
          <h5 class="card-title">${product.title}</h5>
          <p class="card-text">$${product.price.toFixed(2)}</p>
          <button class="btn btn-primary add-to-cart" data-id="${
            product.id
          }" data-title="${product.title}" data-price="${
      product.price
    }" data-image="${product.image}">Add to Cart</button>
        </div>
      </div>
    `;
    productList.appendChild(productCard);
  });

  attachAddToCartEventListeners();
}

// Add event listeners to "Add to Cart" buttons
function attachAddToCartEventListeners() {
  const buttons = document.querySelectorAll(".add-to-cart");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.getAttribute("data-id");
      const title = button.getAttribute("data-title");
      const price = parseFloat(button.getAttribute("data-price"));
      const image = button.getAttribute("data-image");
      addToCart(id, title, price, image);
    });
  });
}

// Add product to cart
function addToCart(id, title, price, image) {
  const existingProduct = cart.find((item) => item.id === id);

  if (existingProduct) {
    existingProduct.quantity++;
  } else {
    cart.push({ id, title, price, image, quantity: 1 });
  }

  updateCartUI();
}

// Update cart UI
function updateCartUI() {
  const cartItems = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");

  cartItems.innerHTML = "";
  let subtotal = 0;

  cart.forEach((item) => {
    const itemTotal = item.price * item.quantity;
    subtotal += itemTotal;

    const row = document.createElement("tr");
    row.innerHTML = `
      <td><img src="${item.image}" alt="${
      item.title
    }" style="width: 50px; height: 50px; object-fit: cover;"></td>
      <td>${item.title}</td>
      <td>$${item.price.toFixed(2)}</td>
      <td>
        <button class="btn btn-sm btn-secondary decrease-quantity" data-id="${
          item.id
        }">-</button>
        ${item.quantity}
        <button class="btn btn-sm btn-secondary increase-quantity" data-id="${
          item.id
        }">+</button>
      </td>
      <td>$${itemTotal.toFixed(2)}</td>
      <td><button class="btn btn-danger btn-sm remove-from-cart" data-id="${
        item.id
      }">Remove</button></td>
    `;
    cartItems.appendChild(row);
  });

  const discount = calculateDiscount(subtotal);
  const total = subtotal - discount;

  document.getElementById(
    "cart-subtotal"
  ).textContent = `Subtotal: $${subtotal.toFixed(2)}`;
  document.getElementById(
    "cart-discount"
  ).textContent = `Discount: $${discount.toFixed(2)}`;
  cartTotal.textContent = `Total: $${total.toFixed(2)}`;

  attachRemoveFromCartEventListeners();
  attachQuantityChangeEventListeners();
}

// Calculate discount based on promo code
function calculateDiscount(subtotal) {
  if (!appliedPromoCode) return 0;
  if (appliedPromoCode === "ostad10") return subtotal * 0.1;
  if (appliedPromoCode === "ostad5") return subtotal * 0.05;
  else return subtotal;
  return 0;
}

// Handle promo code application
document.getElementById("apply-promo").addEventListener("click", () => {
  const promoInput = document.getElementById("promo-code");
  const promoCode = promoInput.value.trim().toLowerCase();
  const promoMessage = document.getElementById("promo-message");

  if (promoCode === "ostad10" || promoCode === "ostad5") {
    if (appliedPromoCode === promoCode) {
      promoMessage.textContent = "Promo code already applied.";
      promoMessage.style.color = "orange";
    } else {
      appliedPromoCode = promoCode;
      promoMessage.textContent = `Promo code "${promoCode}" applied successfully.`;
      promoMessage.style.color = "green";
      updateCartUI();
    }
  } else {
    promoMessage.textContent = "Invalid promo code.";
    promoMessage.style.color = "red";
  }

  promoInput.value = "";
});

// Attach event listeners to "Remove" buttons
function attachRemoveFromCartEventListeners() {
  const buttons = document.querySelectorAll(".remove-from-cart");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.getAttribute("data-id");
      removeFromCart(id);
    });
  });
}

// Remove product from cart
function removeFromCart(id) {
  cart = cart.filter((item) => item.id !== id);
  updateCartUI();
}

// Attach event listeners to increase and decrease buttons
function attachQuantityChangeEventListeners() {
  const increaseButtons = document.querySelectorAll(".increase-quantity");
  const decreaseButtons = document.querySelectorAll(".decrease-quantity");

  increaseButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.getAttribute("data-id");
      changeQuantity(id, 1);
    });
  });

  decreaseButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.getAttribute("data-id");
      changeQuantity(id, -1);
    });
  });
}

// Change product quantity in the cart
function changeQuantity(id, delta) {
  const product = cart.find((item) => item.id === id);

  if (product) {
    product.quantity += delta;

    if (product.quantity <= 0) {
      cart = cart.filter((item) => item.id !== id);
    }

    updateCartUI();
  }
}

// Initialize
fetchProducts();
