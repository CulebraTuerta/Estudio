namespace Inventario_de_Objetos
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
            box_list_productos = new ListBox();
            label1 = new Label();
            btn_inventario = new Button();
            btn_comida = new Button();
            btn_herramientas = new Button();
            btn_aseo = new Button();
            btn_agregar = new Button();
            label2 = new Label();
            label3 = new Label();
            etiqueta_descripcion = new Label();
            txt_box_nombreProducto = new TextBox();
            txt_box_precio = new TextBox();
            txt_box_descripcion = new TextBox();
            combo_box_tipoProducto = new ComboBox();
            SuspendLayout();
            // 
            // box_list_productos
            // 
            box_list_productos.FormattingEnabled = true;
            box_list_productos.ItemHeight = 15;
            box_list_productos.Location = new Point(413, 45);
            box_list_productos.Name = "box_list_productos";
            box_list_productos.Size = new Size(414, 364);
            box_list_productos.TabIndex = 0;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 18F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label1.Location = new Point(413, 10);
            label1.Name = "label1";
            label1.Size = new Size(120, 32);
            label1.TabIndex = 1;
            label1.Text = "Productos";
            // 
            // btn_inventario
            // 
            btn_inventario.Location = new Point(271, 45);
            btn_inventario.Name = "btn_inventario";
            btn_inventario.Size = new Size(120, 50);
            btn_inventario.TabIndex = 2;
            btn_inventario.Text = "Inventario";
            btn_inventario.UseVisualStyleBackColor = true;
            btn_inventario.Click += btn_inventario_Click;
            // 
            // btn_comida
            // 
            btn_comida.Location = new Point(271, 148);
            btn_comida.Name = "btn_comida";
            btn_comida.Size = new Size(120, 50);
            btn_comida.TabIndex = 3;
            btn_comida.Text = "Comida";
            btn_comida.UseVisualStyleBackColor = true;
            btn_comida.Click += btn_comida_Click;
            // 
            // btn_herramientas
            // 
            btn_herramientas.Location = new Point(271, 253);
            btn_herramientas.Name = "btn_herramientas";
            btn_herramientas.Size = new Size(120, 50);
            btn_herramientas.TabIndex = 4;
            btn_herramientas.Text = "Herramientas";
            btn_herramientas.UseVisualStyleBackColor = true;
            btn_herramientas.Click += btn_herramientas_Click;
            // 
            // btn_aseo
            // 
            btn_aseo.Location = new Point(271, 359);
            btn_aseo.Name = "btn_aseo";
            btn_aseo.Size = new Size(120, 50);
            btn_aseo.TabIndex = 5;
            btn_aseo.Text = "Aseo";
            btn_aseo.UseVisualStyleBackColor = true;
            btn_aseo.Click += btn_aseo_Click;
            // 
            // btn_agregar
            // 
            btn_agregar.Location = new Point(58, 359);
            btn_agregar.Name = "btn_agregar";
            btn_agregar.Size = new Size(120, 50);
            btn_agregar.TabIndex = 6;
            btn_agregar.Text = "Agregar";
            btn_agregar.UseVisualStyleBackColor = true;
            btn_agregar.Click += btn_agregar_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(44, 73);
            label2.Name = "label2";
            label2.Size = new Size(122, 15);
            label2.TabIndex = 7;
            label2.Text = "Nombre del Producto";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(44, 138);
            label3.Name = "label3";
            label3.Size = new Size(40, 15);
            label3.TabIndex = 8;
            label3.Text = "Precio";
            // 
            // etiqueta_descripcion
            // 
            etiqueta_descripcion.AutoSize = true;
            etiqueta_descripcion.Location = new Point(44, 276);
            etiqueta_descripcion.Name = "etiqueta_descripcion";
            etiqueta_descripcion.Size = new Size(69, 15);
            etiqueta_descripcion.TabIndex = 9;
            etiqueta_descripcion.Text = "Descripcion";
            // 
            // txt_box_nombreProducto
            // 
            txt_box_nombreProducto.Location = new Point(44, 91);
            txt_box_nombreProducto.Name = "txt_box_nombreProducto";
            txt_box_nombreProducto.Size = new Size(150, 23);
            txt_box_nombreProducto.TabIndex = 10;
            // 
            // txt_box_precio
            // 
            txt_box_precio.Location = new Point(44, 156);
            txt_box_precio.Name = "txt_box_precio";
            txt_box_precio.Size = new Size(150, 23);
            txt_box_precio.TabIndex = 11;
            // 
            // txt_box_descripcion
            // 
            txt_box_descripcion.Location = new Point(44, 294);
            txt_box_descripcion.Name = "txt_box_descripcion";
            txt_box_descripcion.Size = new Size(150, 23);
            txt_box_descripcion.TabIndex = 12;
            // 
            // combo_box_tipoProducto
            // 
            combo_box_tipoProducto.FormattingEnabled = true;
            combo_box_tipoProducto.Location = new Point(44, 217);
            combo_box_tipoProducto.Name = "combo_box_tipoProducto";
            combo_box_tipoProducto.Size = new Size(150, 23);
            combo_box_tipoProducto.TabIndex = 13;
            combo_box_tipoProducto.Text = "Tipo de Producto";
            combo_box_tipoProducto.SelectedIndexChanged += seleccion_tipo;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(839, 450);
            Controls.Add(combo_box_tipoProducto);
            Controls.Add(txt_box_descripcion);
            Controls.Add(txt_box_precio);
            Controls.Add(txt_box_nombreProducto);
            Controls.Add(etiqueta_descripcion);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(btn_agregar);
            Controls.Add(btn_aseo);
            Controls.Add(btn_herramientas);
            Controls.Add(btn_comida);
            Controls.Add(btn_inventario);
            Controls.Add(label1);
            Controls.Add(box_list_productos);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ListBox box_list_productos;
        private Label label1;
        private Button btn_inventario;
        private Button btn_comida;
        private Button btn_herramientas;
        private Button btn_aseo;
        private Button btn_agregar;
        private Label label2;
        private Label label3;
        private Label etiqueta_descripcion;
        private TextBox txt_box_nombreProducto;
        private TextBox txt_box_precio;
        private TextBox txt_box_descripcion;
        private ComboBox combo_box_tipoProducto;
    }
}
