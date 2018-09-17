$(document).ready(function () {

    var searchForm = $(".search-form")
    var searchInput = searchForm.find("[name='q']")
    var searchBtn = searchForm.find("[type='submit']")
    var typingTimer;
    var typingInterval = 1000

    searchInput.keyup(function (event) {
        clearTimeout(typingTimer)
        typingTimer = setTimeout(performSerach, typingInterval)
    })

    searchInput.keydown(function (event) {
        clearTimeout(typingTimer)
    })


    function performSerach() {
        // searchBtn.addclass("disabled")
        searchBtn.html("<i class='fa fa-spin fa-spinner'></i> searching...")
        var query = searchInput.val()
        setTimeout(function () {
            window.location.href = '/search/?q=' + query
        }, 1000)

    }
    var productForm = $(".form-product-ajax")

    productForm.submit(function (event) {
        event.preventDefault()
        // console.log("success")
        var thisForm = $(this)
        var actionEndpoint = thisForm.attr("data-endpoint")
        var httpMethod = thisForm.attr("method")
        var formData = thisForm.serialize()

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                var submitSpan = thisForm.find(".submit-span")
                if (data.added) {
                    submitSpan.html("In Cart <button type='submit' class='btn btn-link'>Remove?</button>")
                }
                else {
                    submitSpan.html("<button type='submit' class='btn btn-success'>Add to Cart</button>")
                }
                var navCartCount = $(".nav-cart-count")
                navCartCount.text(data.cartCount)

                var currentPath = window.location.href
                if (currentPath.indexOf("cart") != -1) {
                    refreshCart()
                }
            },
            error: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        })
    })
    function refreshCart() {
        console.log("in cart")
        var cartTable = $(".cart-table")
        var cartBody = cartTable.find(".cart-body")
        // cartBody.html("<h1>Changed</h1>")
        var productRows = cartBody.find(".cart-product")
        var currentUrl = window.location.href
        var refreshCartUrl = "/api/cart"
        var refreshCartMethod = "GET"
        var data = {}
        $.ajax({
            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            success: function (data) {
                console.log("success")
                console.log(data)
                var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
                if (data.products.length > 0) {
                    productRows.html(" ")
                    i = data.products.length
                    $.each(data.products, function (index, value) {
                        var newCartItemremove = hiddenCartItemRemoveForm.clone()
                        newCartItemremove.css("display", "block")
                        newCartItemremove.find(".cart-item-product-id").val(value.id)
                        cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemremove.html() + "</td><td>" + value.price + "</td></tr>")
                        i--
                    })
                    // productRows.html("<tr><td colspan=3>coming soon</td></tr>")
                    cartBody.find(".cart-subtotal").text(data.subtotal)
                    cartBody.find(".cart-total").text(data.total)
                }
                else {
                    window.location.href = currentUrl
                }
            },
            error: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        })
    }
})        
