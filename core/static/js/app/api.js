angular.module('api',[])
 
angular.module('api').factory('ProdutosAPI', function($http){
  var m = {
    list_products: function(){
      return $http.get('/api/list_products');
    },
    cria_pedido: function(product_ids){
      params = {
        product_ids: JSON.stringify(product_ids)
      };
      return $http.post('/api/cria_pedido', params); //<-- Nao eh exatamente assim que
                                                     // a gente faz POST ajax com Angular
    }
  };
  return m;
});