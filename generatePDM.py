def generate_pdm_file(m_cells):
    # Initial part of the file
    pdm_content = """Coupled
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
    
    # Adding controller
    controller_content = """    
        Atomic
            {
            Name = Controller
            Ports = 1 ; 1
            Path = celulas/controller.h
            Description = Atomic DEVS model
            Graphic
                {
                Position = -11355 ; 45
                Dimension = 675 ; 675
                Direction = Right
                Color = 15
                Icon = None
                }
            Parameters
                {
                cellId = Val; 0 ; cell id
                value = Val; 1.33512e-306 ; value of the cell. 1 = on 0 = off
                }
            }"""
    pdm_content += controller_content

    x = 0;
    y = 0;
    # Generating cells
    for i in range(m_cells):
        cell_content =f"""
        Atomic
            {{
            Name = Cell_{i}
            Ports = 1 ; 1
            Path = celulas/celula.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = -13080 ; -2010  // Adjust position as needed
                Dimension = 675 ; 720
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
        pdm_content += cell_content
        x += 1 
        y += 1
    # Write to a .pdm file
    pdm_content +=  """
        }
    }"""

    with open('model.pdm', 'w') as file:
        file.write(pdm_content)

# Specify the number of cells you want
m_cells = 10  # Change this to your desired number of cells
generate_pdm_file(m_cells)