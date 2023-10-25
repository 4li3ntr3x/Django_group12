var addEtiqueta = document.querySelector('#addEtiqueta');
console.log('registro2');
if (addEtiqueta)
{
    var etiquetaNewCount = document.querySelector('#etiquetaNewCount');
    var etiquetaSave = document.querySelector('#addEtiquetaSave');
    var etiquetaCancel = document.querySelector('#addEtiquetaCancel');
    var etiquetaInput = document.querySelector('#addEtiquetaInput');

    addEtiqueta.addEventListener('click', function() {
    toggleEtiqueta();
  })


  etiquetaCancel.addEventListener('click', function(event){
    event.preventDefault();
    toggleEtiqueta();
  })


    etiquetaSave.addEventListener('click', function(event){
    event.preventDefault();
    let newCheckDiv = document.createElement('div');
    let newChek = document.createElement('Input');
    newChek.type = 'checkbox';
    etiquetaNewCount.value = parseInt(etiquetaNewCount.value) + 1;
    newChek.name = 'newEtiqueta' + etiquetaNewCount.value;
    let newCheckLbl = document.createElement('label');
    newCheckLbl.for = 'newEtiqueta' + etiquetaNewCount.value;
    newCheckLbl.innerHTML = etiquetaInput.value;
    let addDiv = document.querySelector('#addEtiquetaDiv');
    newChek.checked = true;
    let newCheckI = document.createElement('input');
    newCheckI.hidden = true;
    newCheckI.readOnly = true;
    newCheckI.value = etiquetaInput.value;
    newCheckI.name = 'inewEtiqueta' + etiquetaNewCount.value;
    newCheckDiv.appendChild(newChek);
    newCheckDiv.appendChild(newCheckLbl);
    newCheckDiv.appendChild(newCheckI);
    etiquetaInput.value = '';
    addDiv.appendChild(newCheckDiv);
    document.querySelector('#newEtiquetasP').hidden = false;
    toggleEtiqueta();

    })
    toggleEtiqueta();
}
function toggleEtiqueta()
{
    etiquetaInput.hidden = !etiquetaInput.hidden;
    etiquetaSave.hidden = !etiquetaSave.hidden;
    etiquetaCancel.hidden = !etiquetaCancel.hidden;
}