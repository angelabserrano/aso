clear
echo "*** MENU ***"
echo "1. AÑADIR"
echo "2. BUSCAR"
echo "3. LISTAR"
echo "4. ORDENAR"
echo "5. BORRAR"

read -p "Introduce una opcion" opcion
case $opcion in 
  1) echo "Opcion 1 seleccionada";;
  2) echo "Opcion 2 seleccionada";;
  3) echo "Opcion 3 seleccionada";;
  4) echo "Opcion 4 seleccionada";;
  5) echo "Opcion 5 seleccionada";;
  *) echo "Opcion no valida";;
esac
