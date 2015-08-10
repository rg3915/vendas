jQuery(function ($) {
    $('.field-produto').on('change', 'select', function () {
        var select = $(this);
        
        var pk_produto = select.val();

        $.ajax({
            url: '/url/detalhes/produto/' + pk_produto,
            dataType: 'json',
        }).done(function (produto) {
            var input_preco_venda = select.closest('tr').find('.field-precovenda input');

            input_preco_venda.val(produto.preco);
        });
    });
});

/*


{
    "pk": 2,
    "nome": "abc",
    "preco": 2.6
}


*/
