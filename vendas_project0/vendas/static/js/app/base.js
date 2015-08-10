(function(){

  if(!window.Global){
  window.Global = {};
  }
  if(!Global.angular_dependencies){
  Global.angular_dependencies = [];
  }

  angular.module('base', Global.angular_dependencies);

  angular.module('base').config(function($interpolateProvider, $httpProvider){
  $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
   
  //Configuração do CSRF passou pro base.js!
  $httpProvider.defaults.headers.common['X-CSRFToken'] = Global.CSRF_TOKEN; // alguem precisa ter setado isso aqui!
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
  });

})();