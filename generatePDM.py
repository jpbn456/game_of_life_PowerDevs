def initialize_pdm():
        # Initial part of the file
    return """Coupled
    {
    Type = Root
    Name = proyecto_simulacion
    Ports = 0; 0
    Description = 
    Graphic
        {
        Position = 0; 0
        Dimension = 600; 600
        Direction = Right
        Color = 15
        Icon = 
        Window = 5000; 5000; 5000; 5000
        }
    Parameters
        {
        }
    System
        {"""

x_controller = -2000
y_controller = 45
atoms_size = 200

def define_controller():
    # Adding controller
    return f"""    
        Atomic
            {{
            Name = Controller
            Ports = 1 ; 1
            Path = celulas/controller.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = {x_controller} ; {y_controller}
                Dimension = {atoms_size} ; {atoms_size}
                Direction = Right
                Color = 15
                Icon = None
                }}
            Parameters
                {{
                cellId = Val; 0 ; cell id
                value = Val; 1.33512e-306 ; value of the cell. 1 = on 0 = off
                }}
            }}"""

x_cells = -16000 
y_cells = -2010
# cells_amount #start in 2 because "1" is controller
def define_cells(m, n):
    # Generating cells
    pdm_content = ""
    x = 0;
    y = 0;
    cells_amount = 2
    for i in range(m):
        for j in range(n):
            pdm_content += define_single_cell(i, j, cells_amount)
            cells_amount += 1
    return pdm_content

def define_single_cell(x, y, cell_id):
    return f"""
        Atomic
            {{
            Name = Cell_{cell_id}
            Ports = 1 ; 1
            Path = celulas/celula.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = {x_cells + (atoms_size + 200) * x } ; {y_cells + (atoms_size + 200) * y }  // Adjust position as needed
                Dimension = {atoms_size} ; {atoms_size}
                Direction = Right
                Color = 15
                Icon = None
                }}
            Parameters
                {{
                x_pos = Str;{x}; Cell Identity Number, Position x
                y_pos = Str;{y}; Cell Identity Number, Position y
                Alive = Str;{0}; Cell alive status
                }}
            }}"""

def define_lines(m, n):
    # Generating cells
    pdm_content = ""
    x = 0;
    y = 0;
    cells_amount = 2
    for i in range(m):
        for j in range(n):
            pdm_content += define_single_line(i, j, cells_amount)
            cells_amount += 1
    return pdm_content

def define_single_line(x, y, cell_id):
    return f"""
        Line
            {{
            Source = Cmp ;  {cell_id} ;  1 ; 0
            Sink = Cmp ;  1 ;  1 ; -1
            PointX = {x_cells + (atoms_size + 200) * x + atoms_size}; {x_controller}
            PointY = {y_cells + (atoms_size + 200) * y + atoms_size // 2} ; {y_controller + atoms_size//2} 
            }}
        Line
            {{
            Source = Cmp ; 1 ;  1 ; {cell_id - 2}
            Sink = Cmp ; {cell_id} ;  1 ; -1
            PointX = {x_controller + atoms_size}; {x_cells + (atoms_size + 200) * x}
            PointY = {y_controller + atoms_size // 2} ; {y_cells + (atoms_size + 200) * y + atoms_size//2} 
            }}"""

def generate_pdm_file(m, n):

    pdm_content = initialize_pdm()
    pdm_content += define_controller()
    pdm_content += define_cells(m, n)
    pdm_content += define_lines(m, n)
    # Write to a .pdm file
    pdm_content +=  """
        }
    }"""

    with open('model.pdm', 'w') as file:
        file.write(pdm_content)

# Specify the number of cells you want
m = 8  # Change this to your desired number of cells
n = 8
generate_pdm_file(m, n)