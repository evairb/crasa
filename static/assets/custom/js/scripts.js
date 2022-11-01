(function () {
    select_variacao = document.getElementById('select-variacoes');
    variation_preco = document.getElementById('variation-preco');
    variation_preco_promocional = document.getElementById('variation-preco-promocional');

    if (!select_variacao) {
        return;
    }

    if (!variation_preco) {
        return;
    }

    select_variacao.addEventListener('change', function () {
        preco = this.options[this.selectedIndex].getAttribute('data-preco');
        preco_promocional = this.options[this.selectedIndex].getAttribute('data-preco-promocional');

        variation_preco.innerHTML = preco;

        if (variation_preco_promocional) {
            variation_preco_promocional.innerHTML = preco_promocional;
        }
    })
})();


$(document).ready(function(){
    $('.RG').mask('00.000.000-0');

  });

$(document).ready(function () {
    $('#listForm').DataTable({
        language: {
            lengthMenu: 'Quantidade: _MENU_',
            zeroRecords: 'Nada encontrado - desculpe',
            info: 'Páginas _PAGE_ até _PAGES_',
            infoEmpty: 'Não há registros disponíveis',
            infoFiltered: '(filtrado de _MAX_ registros totais)',
            search: "Pesquisar:",
            
            paginate: {
                previous: 'Anterior',
                next:     'Próximo',
              }
        },
       
    });
});

