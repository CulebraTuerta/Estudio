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

            Cargar_Lista(1,habilidades);
        }

        private void Cargar_Lista(int i, List<Habilidad> lista)
        {
            switch (i)
            {
                case 1:
                    foreach (Habilidad habilidad in lista)
                    {
                        listaHabilidades.Items.Add(habilidad.Nombre + " " + habilidad.Precio.ToString());
                    }
                    break;
                case 2:
                    foreach (Habilidad habilidad in lista)
                    {
                        listaAprendidas.Items.Add(habilidad.Nombre + habilidad.Precio.ToString());
                    }
                    break;
            }
        }
        private void aprender_Click(object sender, EventArgs e)
        {

        }

        
    }
}
