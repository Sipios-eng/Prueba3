fetch('https://api.boostr.cl/feriados/en.json')
  .then(response => response.json())
  .then(data => {
    // Almacenar los datos en variables
    const fecha = data[0].date;
    const titulo = data[0].title;
    const tipo = data[0].type;
    const inalienable = data[0].inalienable;
    const extra = data[0].extra;
    

    // (Opcional) Mostrar los datos en la consola
    console.log('Fecha:', fecha);
    console.log('Título:', titulo);
    console.log('Tipo:', tipo);
    console.log('Inalienable:', inalienable);
    console.log('Extra:', extra);
  });