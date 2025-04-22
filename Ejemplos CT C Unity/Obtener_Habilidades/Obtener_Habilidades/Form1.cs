namespace Obtener_Habilidades
{
    public partial class Form1 : Form
    {
        public class Habilidad
        {
            private string nombre;
            private int precio;

            public Habilidad(string nombre, int precio)
            {
                this.nombre = nombre;
                this.precio = precio;
            }                     
            public int Precio { get => precio; set => precio = value; }
            public string Nombre { get => nombre; set => nombre = value; }
        }

        List<Habilidad> habilidades = new List<Habilidad>();
        List<Habilidad> habilidadesAprendidas = new List<Habilidad>();
        private int puntos = 10;

        Habilidad FuegoVolador = new Habilidad("Fuego Volador", 2);
        Habilidad HieloCongelador = new Habilidad("Hielo Congelador", 4);
        Habilidad ExplocionMana = new Habilidad("Explosion de Mana", 5);

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            etiquetaPuntos.Text= "Puntos: "+ puntos.ToString();    
            habilidades.Add(FuegoVolador);
            habilidades.Add(HieloCongelador);   
            habilidades.Add(ExplocionMana);
            //tambien se podria haber iniciado asi: habilidades.Add(new Habilidad("Fuego Volador", 2);  //y asi nos ahorramos crearlos afuera

            Cargar_Lista(1,habilidades);
        }

        private void Cargar_Lista(int i, List<Habilidad> lista)
        {
            switch (i)
            {
                case 1:
                    listaHabilidades.Items.Clear();//Aqui se eliminan antes de cargarse
                    foreach (Habilidad habilidad in lista) //A estas listas solo le podemos pasar Strings, asi que por eso lo escribimos asi
                    {
                        listaHabilidades.Items.Add(habilidad.Nombre + " " + habilidad.Precio.ToString());  //esta lista habilidades es el recuadro
                    }
                    break;
                case 2:
                    listaAprendidas.Items.Clear();
                    foreach (Habilidad habilidad in lista)
                    {
                        listaAprendidas.Items.Add(habilidad.Nombre + " " + habilidad.Precio.ToString()); // lo mismo de arriba, es el recuadro
                    }
                    break;
            }
        }
        private void aprender_Click(object sender, EventArgs e)
        {
            string habilidadAprender = txtHabilidad.Text; //esta es la entrada de texto, pero necesitamos verificarlo
            bool existe = false; // si encuentra la habilidad entonces cambia esta variable a true
            int indice = 0; // esto es para saber en que posicion esta la habilidad, para poder agregarla despues a la otra lista

            foreach (Habilidad habilidad in habilidades)  // con esto revisamos una variable habilidad en la lista habilidades
            {
                if(habilidadAprender.ToLower() == habilidad.Nombre.ToLower())  //el tolower hace que ponga todo en minusculas.
                {       // y aqui lo que hacemos es ver si el nombre que ingresamos es igual a alguna habilidad en la lista habilidades 
                    existe  = true; // necesitamos guardar el indice tambien, por eso la siguiente linea de codigo
                    indice = habilidades.IndexOf(habilidad); //con esto sacamos la habilidad de la lista habilidades, y lo guardamos en indice
                }                
            }
            if(!existe) //esto quiere decir que si no existe, ya que como parte falso y el ! es como negar, entonces negar lo falso es True
            {   // por lo tanto quiere decir que no encontro niuna wea y tiene que decirle al usuario que no sea weon que la wea que ingreso no existe
                MessageBox.Show("Esa habilidad no esta disponible");
            }
            else //si encontro la habilidad en la lista, por ende si existe agregamos el nombre a la otra lista
            {
                if (habilidades[indice].Precio <= puntos) //primero verificamos si tiene los puntos suficientes
                { //si es asi, entonces restamos los puntos de la habilidad a la variable puntos y la agregamos a la lista de habilidades aprendidas
                    puntos = puntos - habilidades[indice].Precio; //ojo, si pongo precio en minuscula, al ser privado no podre modificarlo.
                    //MessageBox.Show(habilidades[indice].precio.ToString() + " Puntos Restados"); //simplemente para saber si se ejecutaba
                    etiquetaPuntos.Text = "Puntos: " + puntos.ToString(); //actualizamos los puntos //dm funciono :)
                    // falta solo hacer que pase de una lista a otra....
                    habilidadesAprendidas.Add(habilidades[indice]); //pense que se pasaba solo el nombre, pero se pasa toda la habilidad con el indice
                    // y ahora tenemos que eliminarlo de la otra...
                    habilidades.Remove(habilidades[indice]);

                    //listo con lo anterior, pero ahora con esto hago que se muestren las nuevas listas, pero no puedo eliminar la actual. 
                    //listaHabilidades.Refresh(); // no resulta con esto... 
                    // SE ELIMINAN EN EL CARGAR LISTA, ANTES DE EJECUTARSE!! se ocupa el items.clear()
                    //y luego cargamos las listas nuevamente

                    Cargar_Lista(1,habilidades);                    
                    Cargar_Lista(2,habilidadesAprendidas);


                }
                else { MessageBox.Show("No tienes puntos suficientes"); }
            }  
        }
    }
}
