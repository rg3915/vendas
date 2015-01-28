angular.module('vendas',['api'])
angular.module('vendas').factory('VendasModel', function(ProdutosAPI){
  var m = {
    loading: false,
    produto: null,
    produtos: [],
    selected_products: [],
    init: function(){
      m.loading = true;
      ProdutosAPI.list_products().success(function(produtos){
        m.produtos = produtos;
        m.loading = false;
      });
    },
    adiciona_produto: function(){
      m.selected_products.push(m.produto);
    },
    cria_pedido: function(){
      var produto_ids = [];
      for(var i=0; i<m.selected_products.length; i++){
        produto_ids.push(m.selected_products[i].id);
      }
      ProdutosAPI.cria_pedido(produto_ids).success(function(sale){
        alert('Seu pedido é o numero '+sale.id);
      });
    }
  };
  m.init();
  return m;
});
angular.module('vendas').controller('VendasCtrl', function($scope, VendasModel){
 var m = $scope.m = VendasModel;
});