const buttons = document.getElementsByTagName("button");

function updateTotal() {
  const basePrice = 1299;
  const memoryCost = parseInt(
    document.getElementById("memory-cost").textContent
  );
  const storageCost = parseInt(
    document.getElementById("storage-cost").textContent
  );
  const deliveryCost = parseInt(
    document.getElementById("delivery-cost").textContent
  );
  return basePrice + memoryCost + storageCost + deliveryCost;
}

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function () {
    if (buttons[i].id === "8gb-memory") {
      customizationPrice("memory-cost", 0);
    } else if (buttons[i].id === "16gb-memory") {
      customizationPrice("memory-cost", 150);
    } else if (buttons[i].id === "256gb-storage") {
      customizationPrice("storage-cost", 0);
    } else if (buttons[i].id === "512gb-storage") {
      customizationPrice("storage-cost", 100);
    } else if (buttons[i].id === "1tb-storage") {
      customizationPrice("storage-cost", 200);
    } else if (buttons[i].id === "late-delivery") {
      customizationPrice("delivery-cost", 0);
    } else if (buttons[i].id === "early-delivery") {
      customizationPrice("delivery-cost", 20);
    } else {
      promocode();
    }
  });
}

function customizationPrice(id, cost) {
  const now = document.getElementById(id);
  now.textContent = cost;
  const totalCost = updateTotal();
  const totalPrice = document.getElementById("total-price");
  totalPrice.textContent = totalCost;
}

// function promocode()
function promocode() {
  const promoInput = document.getElementById("input-field").value.trim();
  const totalPriceElement = document.getElementById("total-price");
  const userPaymentElement = document.getElementById("user-payment");
  let totalCost = parseInt(totalPriceElement.textContent);

  if (promoInput === "Ostad") {
    const discountedPrice = totalCost * 0.9;
    totalPriceElement.textContent = discountedPrice.toFixed(2);
    userPaymentElement.textContent = discountedPrice.toFixed(2);
    alert("Promo code applied successfully! You saved 10%.");
  } else {
    alert("Invalid promo code. Please try again.");
  }

  document.getElementById("input-field").value = "";
}
