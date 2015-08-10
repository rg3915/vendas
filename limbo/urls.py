urlpatterns += patterns(
    'vendas_project.vendas.json_views',
    url(r'^api/list_products$', 'list_products', name='api_list_products'),
    url(r'^api/cria_pedido$', 'cria_pedido', name='api_cria_pedido'),

)
