namespace Hola_Mundo
{
    public partial class Ventana : Form
    {
        public double num1 = 1.3;
        public float num2 = 1.3f;
                
        public Ventana()
        {
            InitializeComponent();
        }

        private void HolaMundo(object sender, EventArgs e)
        {
            MessageBox.Show("Hola Mundo");
        }
    }
}
