namespace Obtener_Habilidades
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
            btnAprender = new Button();
            listaHabilidades = new ListBox();
            listaAprendidas = new ListBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            txtHabilidad = new TextBox();
            etiquetaPuntos = new Label();
            SuspendLayout();
            // 
            // btnAprender
            // 
            btnAprender.Location = new Point(28, 326);
            btnAprender.Name = "btnAprender";
            btnAprender.Size = new Size(123, 44);
            btnAprender.TabIndex = 0;
            btnAprender.Text = "Aprender";
            btnAprender.UseVisualStyleBackColor = true;
            btnAprender.Click += aprender_Click;
            // 
            // listaHabilidades
            // 
            listaHabilidades.FormattingEnabled = true;
            listaHabilidades.ItemHeight = 15;
            listaHabilidades.Location = new Point(191, 62);
            listaHabilidades.Name = "listaHabilidades";
            listaHabilidades.Size = new Size(193, 319);
            listaHabilidades.TabIndex = 1;
            // 
            // listaAprendidas
            // 
            listaAprendidas.FormattingEnabled = true;
            listaAprendidas.ItemHeight = 15;
            listaAprendidas.Location = new Point(425, 62);
            listaAprendidas.Name = "listaAprendidas";
            listaAprendidas.Size = new Size(193, 319);
            listaAprendidas.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Tahoma", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.Location = new Point(239, 40);
            label1.Name = "label1";
            label1.Size = new Size(104, 19);
            label1.TabIndex = 3;
            label1.Text = "Habilidades";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Tahoma", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label2.Location = new Point(472, 40);
            label2.Name = "label2";
            label2.Size = new Size(101, 19);
            label2.TabIndex = 4;
            label2.Text = "Aprendidas";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(28, 279);
            label3.Name = "label3";
            label3.Size = new Size(117, 15);
            label3.TabIndex = 5;
            label3.Text = "Habilidad a aprender";
            // 
            // txtHabilidad
            // 
            txtHabilidad.Location = new Point(28, 297);
            txtHabilidad.Name = "txtHabilidad";
            txtHabilidad.Size = new Size(123, 23);
            txtHabilidad.TabIndex = 6;
            // 
            // etiquetaPuntos
            // 
            etiquetaPuntos.AutoSize = true;
            etiquetaPuntos.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            etiquetaPuntos.Location = new Point(28, 191);
            etiquetaPuntos.Name = "etiquetaPuntos";
            etiquetaPuntos.Size = new Size(89, 25);
            etiquetaPuntos.TabIndex = 7;
            etiquetaPuntos.Text = "Puntos: 0";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(670, 450);
            Controls.Add(etiquetaPuntos);
            Controls.Add(txtHabilidad);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(listaAprendidas);
            Controls.Add(listaHabilidades);
            Controls.Add(btnAprender);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnAprender;
        private ListBox listaHabilidades;
        private ListBox listaAprendidas;
        private Label label1;
        private Label label2;
        private Label label3;
        private TextBox txtHabilidad;
        private Label etiquetaPuntos;
    }
}
