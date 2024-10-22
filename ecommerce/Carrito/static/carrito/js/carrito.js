// const modalOverlay = document.getElementById("modal-overlay");
// const modalContainer = document.getElementById("modal-container");
// const cartBtn = document.getElementById("cart-btn");
// const cartCounter = document.getElementById("cart-counter");


// const displayCart = () => {
//     //Setteo de inicio
//     modalContainer.innerHTML = "";
//     modalContainer.style.display = "block"; //Block
//     modalOverlay.style.display = "block";

//     //Modal header
//     const modalHeader = document.createElement('div'); //Podemos crear lo que queramos
//     const modalClose = document.createElement('div');
//     modalClose.innerText = "❌"
//     modalClose.className = "modal-close";
//     modalContainer.append(modalHeader);

//     // Boton cerrar
//     modalClose.addEventListener("click", ()=>{
//         modalContainer.style.display = "none";
//         modalOverlay.style.display = "none";
//     });

//     modalHeader.append(modalClose);

//     const modalTitle = document.createElement('div');
//     modalTitle.innerText = "Carrito";
//     modalTitle.className = "modal-title";
//     modalHeader.append(modalTitle);

//     // MODAL BODY
//     const modalBody = document.createElement('div');
//     const imgProduct = "../../static/carrito/js/The cart.jpg"
//     modalBody.className = "modal-body";
//     modalBody.innerHTML = `
//     <div class="product">
//         <img id= "imagen1" class="product" src="${imgProduct}"/>
//         <div class="product-info">
//             <h4>"Nombre del producto"</h4>
//         </div>

//         <div class="quantity">
//             <span class="quantity-btn-decrese">-</span>
//             <span class="quantity-input">"Cantidad"</span>
//             <span class="quantity-btn-increse">+</span>
//         </div>

//         <div class="price">"Precio * Cantidad"</div>
//         <div class="delete-product">❌</div>
//     </div>
//     `;
    
//     modalContainer.append(modalBody);
    
//     const decrese = modalBody.querySelector(".quantity-btn-decrese") //Me permite capturar elementos por su clase de css
//     decrese.addEventListener("click", ()=>{
//         // if(product.quantity !== 1){
//         //     product.quantity--;
//         //     displayCart();
//         // }
//         alert("Restar al carrito")
//         // displayCartCounter();
        
//     });
    
//     const increse = modalBody.querySelector(".quantity-btn-increse") //Me permite capturar elementos por su clase de css
//     increse.addEventListener("click", ()=>{
//         // product.quantity++;
//         alert("Agregar mas productos")
//         displayCart();
//         // displayCartCounter();
//     });
    
//     //delete
//     const deleteProduct = modalBody.querySelector(".delete-product");
//     deleteProduct.addEventListener("click", ()=> {
//         // deleteCartProduct(product.id)
//         alert("Eliminar producto")
//     });


//     // MODAL FOOTER
//     const total = "Total de la compra";
//     const modalFooter = document.createElement('div');
//     modalFooter.className = "modal-footer";
//     modalFooter.innerHTML = `
//     <div class="total-price">Total: ${total}</div>
//     <button class="btn-primary" id="checkout-btn"> Go to Checkout</button>
//     `;
//     modalContainer.append(modalFooter);


// }

// cartBtn.addEventListener("click", displayCart);