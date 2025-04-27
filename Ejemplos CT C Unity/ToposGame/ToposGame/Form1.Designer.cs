namespace ToposGame
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            btn_comenzar = new Button();
            etiqueta_mejor = new Label();
            etiqueta_puntaje = new Label();
            etiqueta_fallos_restantes = new Label();
            timer_topo = new System.Windows.Forms.Timer(components);
            SuspendLayout();
            // 
            // btn_comenzar
            // 
            btn_comenzar.BackColor = Color.Transparent;
            btn_comenzar.BackgroundImage = (Image)resources.GetObject("btn_comenzar.BackgroundImage");
            btn_comenzar.BackgroundImageLayout = ImageLayout.Center;
            btn_comenzar.FlatAppearance.BorderSize = 0;
            btn_comenzar.FlatAppearance.MouseDownBackColor = Color.Transparent;
            btn_comenzar.FlatAppearance.MouseOverBackColor = Color.Transparent;
            btn_comenzar.FlatStyle = FlatStyle.Flat;
            btn_comenzar.Location = new Point(648, 238);
            btn_comenzar.Name = "btn_comenzar";
            btn_comenzar.Size = new Size(228, 72);
            btn_comenzar.TabIndex = 0;
            btn_comenzar.UseVisualStyleBackColor = false;
            btn_comenzar.Click += comenzar_click;
            // 
            // etiqueta_mejor
            // 
            etiqueta_mejor.AutoSize = true;
            etiqueta_mejor.BackColor = Color.Transparent;
            etiqueta_mejor.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            etiqueta_mejor.Location = new Point(661, 319);
            etiqueta_mejor.Name = "etiqueta_mejor";
            etiqueta_mejor.Size = new Size(85, 25);
            etiqueta_mejor.TabIndex = 1;
            etiqueta_mejor.Text = "Mejor: 0";
            // 
            // etiqueta_puntaje
            // 
            etiqueta_puntaje.AutoSize = true;
            etiqueta_puntaje.BackColor = Color.Transparent;
            etiqueta_puntaje.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            etiqueta_puntaje.Location = new Point(661, 366);
            etiqueta_puntaje.Name = "etiqueta_puntaje";
            etiqueta_puntaje.Size = new Size(92, 25);
            etiqueta_puntaje.TabIndex = 1;
            etiqueta_puntaje.Text = "Puntos: 0";
            // 
            // etiqueta_fallos_restantes
            // 
            etiqueta_fallos_restantes.AutoSize = true;
            etiqueta_fallos_restantes.BackColor = Color.Transparent;
            etiqueta_fallos_restantes.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            etiqueta_fallos_restantes.Location = new Point(661, 413);
            etiqueta_fallos_restantes.Name = "etiqueta_fallos_restantes";
            etiqueta_fallos_restantes.Size = new Size(168, 25);
            etiqueta_fallos_restantes.TabIndex = 2;
            etiqueta_fallos_restantes.Text = "Fallos Restantes: 5";
            // 
            // timer_topo
            // 
            timer_topo.Interval = 2000;
            timer_topo.Tick += Timer_topo;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            ClientSize = new Size(904, 601);
            Controls.Add(etiqueta_fallos_restantes);
            Controls.Add(etiqueta_puntaje);
            Controls.Add(etiqueta_mejor);
            Controls.Add(btn_comenzar);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btn_comenzar;
        private Label etiqueta_mejor;
        private Label etiqueta_puntaje;
        private Label etiqueta_fallos_restantes;
        private System.Windows.Forms.Timer timer_topo;
    }
}
