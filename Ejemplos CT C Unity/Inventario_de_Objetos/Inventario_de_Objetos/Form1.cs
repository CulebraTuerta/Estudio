namespace Inventario_de_Objetos
{
    public partial class Form1 : Form
    {
        // Primero creamos las clases para poder determinar que necesitamos para cada objeto
        public class Producto
        {
            private string nombre;
            private int precio;

            public Producto(string nombre, int precio)
            {
                this.Nombre = nombre;
                this.Precio = precio;
            }

            public int Precio { get => precio; set => precio = value; }
            public string Nombre { get => nombre; set => nombre = value; }
        }

        public class Comida : Producto
        {
            private string caducidad;
            public Comida(string nombre, int precio, string caducidad) : base(nombre, precio)
            {
                this.Caducidad = caducidad;
            }

            public string Caducidad { get => caducidad; set => caducidad = value; }
        }

        public class Herramientas : Producto
        {
            private string material;
            public Herramientas(string nombre, int precio, string material) : base(nombre, precio)
            {
                this.Material = material;
            }

            public string Material { get => material; set => material = value; }
        }

        public class Aseo : Producto
        {
            private string uso;
            public Aseo(string nombre, int precio, string uso) : base(nombre, precio)
            {
                this.Uso = uso;
            }

            public string Uso { get => uso; set => uso = value; }
        }

        //Ahora necesitamos crear las listas, para asi utilizarlas y modificarlas 
        List<Comida> lista_comida = new List<Comida>();
        List<Herramientas> lista_herramienta = new List<Herramientas>();
        List<Aseo> lista_aseo = new List<Aseo>();

        int seleccionTipoNumero = 0;

        private void Form1_Load(object sender, EventArgs e)
        {
            //con esto iniciamos los primeros productos a nuestra lista, esto es lo base, luego podremos agregarle nuevos
            lista_comida.Add(new Comida("Manzana", 3000, "22/06/25"));
            lista_comida.Add(new Comida("Pera", 4000, "25/05/25"));
            lista_comida.Add(new Comida("Chocolate", 2500, "12/07/24"));
            lista_herramienta.Add(new Herramientas("Martillo", 45000, "Metal"));
            lista_herramienta.Add(new Herramientas("Destornillador", 37000, "Metal y plástico"));
            lista_aseo.Add(new Aseo("Detergente", 7000, "1 tapa de detergente por cada 5 litros de agua"));

            combo_box_tipoProducto.Items.Add("Comida");
            combo_box_tipoProducto.Items.Add("Herramienta");
            combo_box_tipoProducto.Items.Add("Aseo");
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void btn_inventario_Click(object sender, EventArgs e)
        {
            // En este paso, vamos a especificar que cuando apretemos el boton inventario, nos de el nombre y datos de todos los inventarios juntos
            box_list_productos.Items.Clear();//con esto eliminamos lo que este ahi, antes de imprimir nueva informacion
            foreach (Comida item_comida in lista_comida)
            {
                box_list_productos.Items.Add(item_comida.Nombre + " " + item_comida.Precio + " " + item_comida.Caducidad.ToString());
            }
            foreach (Herramientas item_herramienta in lista_herramienta)
            {
                box_list_productos.Items.Add(item_herramienta.Nombre + " " + item_herramienta.Precio + " " + item_herramienta.Material.ToString());
            }
            foreach (Aseo item_aseo in lista_aseo)
            {
                box_list_productos.Items.Add(item_aseo.Nombre + " " + item_aseo.Precio + " " + item_aseo.Uso.ToString());
            }
        }

        private void seleccion_tipo(object sender, EventArgs e)
        {
            //Cuando el usuario aprete la lista desplegable, nos va a dar una de las opciones que agregamos al principio
            //con la opcion que seleccione, cambiaremos la etiqueta de descripcion
            seleccionTipoNumero = combo_box_tipoProducto.SelectedIndex;

            switch (seleccionTipoNumero)
            {
                case 0:
                    etiqueta_descripcion.Text = "Caducidad";
                    break;
                case 1:
                    etiqueta_descripcion.Text = "Material";
                    break;
                case 2:
                    etiqueta_descripcion.Text = "Uso";
                    break;
            }

        }

        private void btn_aseo_Click(object sender, EventArgs e)
        {
            box_list_productos.Items.Clear();//con esto eliminamos lo que este ahi, antes de imprimir nueva informacion
            foreach (Aseo item_aseo in lista_aseo)
            {
                box_list_productos.Items.Add(item_aseo.Nombre + " " + item_aseo.Precio.ToString() + " " + item_aseo.Uso.ToString()); // ojo, da lo mismo el tostring desde int aqui
            }
        }

        private void btn_herramientas_Click(object sender, EventArgs e)
        {
            box_list_productos.Items.Clear();//con esto eliminamos lo que este ahi, antes de imprimir nueva informacion
            foreach (Herramientas item_herramienta in lista_herramienta)
            {
                box_list_productos.Items.Add(item_herramienta.Nombre + " " + item_herramienta.Precio.ToString() + " " + item_herramienta.Material.ToString()); // ojo, da lo mismo el tostring desde int aqui
            }
        }

        private void btn_comida_Click(object sender, EventArgs e)
        {
            box_list_productos.Items.Clear();
            foreach (Comida item_comida in lista_comida)
            {
                box_list_productos.Items.Add(item_comida.Nombre + " " + item_comida.Precio.ToString() + " " + item_comida.Caducidad.ToString()); // ojo, da lo mismo el tostring desde int aqui
            }
        }

        private void btn_agregar_Click(object sender, EventArgs e)
        {
            //aqui tenemos que crear un nuevo producto para agregarlo a la lista que corresponda (voy a partir de abajo para arriba)
            int numero=0; // pude tambien haber usado la variable "seleccionTipoNumero"
            box_list_productos.Items.Clear();

            //creamos las variables desde los text box
            string nombreProducto = txt_box_nombreProducto.Text;
            int precioIngresado = int.Parse(txt_box_precio.Text); // Con esta instruccion siempre, que ingrese un texto aqui, lo convertira en INT
            string descripcionIngresada = txt_box_descripcion.Text; //Caducidad, Material ,Uso

            // Para agregarlo necesito saber si es comida, herramienta o aseo (determinar variable numero)
            if (combo_box_tipoProducto.Text=="Comida"){numero = 0;}
            else if (combo_box_tipoProducto.Text == "Herramienta") { numero = 1; }
            else if (combo_box_tipoProducto.Text == "Aseo") { numero = 2; }

                // Ultimo paso, agregarlo a la lista correspondiente
                switch (numero)
                {
                    case 0: //comida
                        lista_comida.Add(new Comida(nombreProducto, precioIngresado, descripcionIngresada));
                        btn_comida_Click(sender, e);
                        break;

                    case 1: //herramienta
                        lista_herramienta.Add(new Herramientas(nombreProducto, precioIngresado, descripcionIngresada));
                        btn_herramientas_Click(sender , e);
                        break;

                    case 2: //aseo
                        lista_aseo.Add(new Aseo(nombreProducto, precioIngresado, descripcionIngresada));
                        btn_aseo_Click(sender , e); 
                        break;
                }            
            // Mostar un aviso de que se agrego
            //MessageBox.Show("Item Agregado");

            //podemos hacer tambien que se actualice la lista de inmediato, para asi dar a entender que se agrego a la lista.
            //partiremos eliminando la lista actual (lo hare al principio de esta accion)
        }

        

        
    }
}
