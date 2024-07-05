// Función para obtener los feriados de un año específico
async function obtenerFeriados(anio) {
    // Se define la URL de la API
    const apiUrl = 'https://api.boostr.cl/feriados/${anio}.json';
  
    // Se realiza la petición a la API
    const response = await fetch(apiUrl.replace('${anio}', anio));
  
    // Se verifica si la petición fue exitosa
    if (!response.ok) {
      throw new Error('Error al obtener los feriados');
    }
  
    // Se define la clave de la respuesta JSON
    const dataKey = 'data';
  
    // Se parsea la respuesta JSON
    const data = await response.json();
  
    // Se retorna la lista de feriados  
    return data[dataKey];
  }
  
  // Función para mostrar los feriados en pantalla
  async function mostrarFeriadosEnPantalla(anio) {
    // Se obtienen los feriados del año especificado
    const feriados = await obtenerFeriados(anio);
  
    // Se crea un elemento para mostrar los feriados
    const contenedorFeriados = document.createElement('div');
    contenedorFeriados.id = 'feriados';
  
    // Se define la clase CSS para los feriados
    const feriadoClass = 'feriado';
  
    // Se recorre la lista de feriados
    for (const feriado of feriados) {
      // Se crea un elemento para cada feriado
      const elementoFeriado = document.createElement('div');
      elementoFeriado.classList.add(feriadoClass);
  
      // Se agrega la fecha del feriado
      const fecha = document.createElement('span');
      fecha.textContent = feriado.date;
      elementoFeriado.appendChild(fecha);
  
      // Se agrega el elemento del feriado al contenedor
      contenedorFeriados.appendChild(elementoFeriado);
    }
  
    // Se agrega el contenedor de feriados al DOM
    document.body.appendChild(contenedorFeriados);
  }
  
  // Se muestra un ejemplo de uso
  mostrarFeriadosEnPantalla(2024);
  