namespace Ejercicios_CSharp
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
            btnAmarillo = new Button();
            btnRojo = new Button();
            btnNegro = new Button();
            btnReiniciar = new Button();
            SuspendLayout();
            // 
            // btnAmarillo
            // 
            btnAmarillo.Location = new Point(372, 94);
            btnAmarillo.Name = "btnAmarillo";
            btnAmarillo.Size = new Size(94, 38);
            btnAmarillo.TabIndex = 0;
            btnAmarillo.Text = "Amarillo";
            btnAmarillo.UseVisualStyleBackColor = true;
            btnAmarillo.Click += Color_Amarillo;
            // 
            // btnRojo
            // 
            btnRojo.Location = new Point(372, 138);
            btnRojo.Name = "btnRojo";
            btnRojo.Size = new Size(94, 38);
            btnRojo.TabIndex = 1;
            btnRojo.Text = "Rojo";
            btnRojo.UseVisualStyleBackColor = true;
            btnRojo.Click += Color_Rojo;
            // 
            // btnNegro
            // 
            btnNegro.Location = new Point(372, 182);
            btnNegro.Name = "btnNegro";
            btnNegro.Size = new Size(94, 38);
            btnNegro.TabIndex = 2;
            btnNegro.Text = "Negro";
            btnNegro.UseVisualStyleBackColor = true;
            btnNegro.Click += Color_Negro;
            // 
            // btnReiniciar
            // 
            btnReiniciar.Location = new Point(372, 226);
            btnReiniciar.Name = "btnReiniciar";
            btnReiniciar.Size = new Size(94, 38);
            btnReiniciar.TabIndex = 3;
            btnReiniciar.Text = "Reiniciar";
            btnReiniciar.UseVisualStyleBackColor = true;
            btnReiniciar.Click += Reiniciar_Color;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(826, 377);
            Controls.Add(btnReiniciar);
            Controls.Add(btnNegro);
            Controls.Add(btnRojo);
            Controls.Add(btnAmarillo);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button btnAmarillo;
        private Button btnRojo;
        private Button btnNegro;
        private Button btnReiniciar;
    }
}
