using System.Media;

//aun tiene un error, mientras no falles, no hay problema, si fallas una vez y dejas de hacer click, te seguira descontando cada vez que cambie
//la imagen.

namespace ToposGame
{
    public partial class Form1 : Form
    {
        public SoundPlayer bgmusic = new SoundPlayer("Recursos/Menu.wav");

        PictureBox imagen = new PictureBox();
        bool yaGolpeado = false;

        List<PictureBox> imagenes = new List<PictureBox>();
        Random random = new Random();
        bool TopoInicio = true;
        int numAux;
        int puntos = 0;
        int mejorPuntaje = 0;
        string tagAux;
        int fallos = 5;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            CargarImgBox();
            bgmusic.PlayLooping();
        }

        private void CargarImgBox()
        {
            int margenIzq = 50;
            int margenTop = 50;
            int columnas = 0;
            int tag = 1;


            for (int i = 0; i < 9; i++)
            {
                PictureBox img = new PictureBox();
                img.Height = 150;
                img.Width = 150;
                img.Image = Image.FromFile("Recursos/interrogante.png");
                img.BackColor = Color.Transparent;
                img.SizeMode = PictureBoxSizeMode.StretchImage;
                img.Tag = tag.ToString();
                tag++;
                img.Click += Img_Click;
                imagenes.Add(img);

                if (tag == 4)
                {
                    tag = 1;
                }
                if (columnas < 3)
                {
                    columnas++;
                    img.Left = margenIzq;
                    img.Top = margenTop;
                    this.Controls.Add(img);
                    margenIzq += 170;
                }
                if (columnas == 3)
                {
                    margenIzq = 50;
                    margenTop += 170;
                    columnas = 0;
                }
            }
        }

        private void Img_Click(object? sender, EventArgs e)
        {
            imagen = (PictureBox)sender;

            if (!yaGolpeado)
            {
                if (imagen.Tag != "topo") //mecanica de fallo
                {
                    Fallo();
                }
                else 
                {
                    yaGolpeado = true;
                    imagen.Image = Image.FromFile("Recursos/golpe" + tagAux + ".png");
                    puntos += 100;
                    etiqueta_puntaje.Text = "Puntos: " + puntos;

                    if(puntos==1000) //añade dificultad, como tetris, deberia aumentar el tiempo (osea mas rapido)
                    {
                        timer_topo.Interval = 1000; //parte en 2000...
                    }

                    if (puntos > mejorPuntaje)
                    {
                        mejorPuntaje = puntos;
                        etiqueta_mejor.Text = "Mejor Puntaje: " + mejorPuntaje;
                    }
                }
            }
        }

        private void Timer_topo(object sender, EventArgs e)
        {
            int randonNum = random.Next(0, 9); //numero aleatorio de 0 a 8
            if (TopoInicio)
            {
                numAux = randonNum;
                tagAux = imagenes[randonNum].Tag.ToString();
                imagenes[randonNum].Image = Image.FromFile("Recursos/animal" + imagenes[randonNum].Tag + ".png");
                imagenes[randonNum].Tag = "topo";
                TopoInicio = false;
                yaGolpeado=true; 
            }
            else //creo la siguiente imagen
            {
                while (randonNum == numAux) //la idea es que elija una diferente, por lo cual esto impide que elija la misma
                {
                    randonNum = random.Next(0, 9);
                }
                imagenes[numAux].Image = Image.FromFile("Recursos/interrogante.png"); //ahora que eligio otra ponemos en gris la anterior
                imagenes[numAux].Tag = tagAux;

                numAux = randonNum; //seteamos nuevametne todo 
                tagAux = imagenes[randonNum].Tag.ToString();
                imagenes[randonNum].Image = Image.FromFile("Recursos/animal" + imagenes[randonNum].Tag + ".png");
                imagenes[randonNum].Tag = "topo";
                yaGolpeado = true; //lo puse aca tambien porque tiene que resetearlo claro esta... 

            }
            if (!yaGolpeado)
            {
                Fallo();
            }

            yaGolpeado = false;
        }

        private void comenzar_click(object sender, EventArgs e)
        {
            timer_topo.Start();
            fallos = 5;
            etiqueta_fallos_restantes.Text = "Fallos Restantes: " + fallos;
            puntos = 0;
            etiqueta_puntaje.Text = "Puntos: " + puntos;
            timer_topo.Interval = 2000;
            yaGolpeado = false;
            TopoInicio = true;
        }

        private void Fallo()
        {
            fallos--;
            etiqueta_fallos_restantes.Text = "Fallos Restantes: " + fallos;

            if(fallos<1)
            {
                timer_topo.Stop();
                MessageBox.Show("Juego Terminado!");
            }
        }
    }
}
