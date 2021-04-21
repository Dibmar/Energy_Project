import plotly.express as px
import plotly.graph_objects as go
import sys, os

# Save image fucntion
def save_my_image(name, parent_directory, destination, fig):
    """
                        ---What it does---
     This function stores a plotly image as an html file in a given directory. If it finds the directory, uses it and if not, creates it.
     
                        ---What it needs---
        - A name for the plot (name)
        - The parent directories full path (parent_directory).
        - Where to store the file (destination)

                        ---What it returns---
     This function does not return anything
    """      
            
    # Images\ directory check up and creation
    if parent_directory.endswith('\\'):
        pass
    else:
        parent_directory = parent_directory + '\\'

    path = parent_directory + destination
    directory_exists = os.path.isdir(path)
    name = name + '.html'

    if destination.endswith('\\'):
        final_path = path + name
    
    else:
        final_path = path + '\\' + name
    
    
    if directory_exists == False:
        print(f'Creating {destination}')
        os.mkdir(path)

    # csv file stored
    print(f'The file will be stored as "{name}" in {destination}...')
    fig.write_html(final_path)

# Plotting functions
def create_line_plot (data_frame= None, x=None, y=None, 
                line_group=None, color=None, 
                line_dash=None, hover_name=None, 
                hover_data=None, custom_data=None, 
                text=None, facet_row=None, facet_col=None, 
                facet_col_wrap=0, facet_row_spacing=None, 
                facet_col_spacing=None, error_x=None, 
                error_x_minus=None, error_y=None, 
                error_y_minus=None, animation_frame=None, 
                animation_group=None, category_orders=None, 
                labels=None, orientation=None, color_discrete_sequence=None, 
                color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, 
                log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, 
                render_mode='auto', title=None, template=None, width=None, 
                height=None, save= False, destination= 'Images', parent_directory= None, name= None):
    """
                        ---What it does---
    This function creates a line plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
        
    fig = px.line(data_frame= data_frame, x=x, y= y,
                line_group= line_group, color= color, 
                line_dash= line_dash, hover_name= hover_name, 
                hover_data= hover_data, custom_data= custom_data, 
                text= text, facet_row= facet_row, facet_col= facet_col, 
                facet_col_wrap= facet_col_wrap,  error_x= error_x, 
                error_x_minus= error_x_minus, error_y= error_y, 
                error_y_minus= error_y_minus, animation_frame= animation_frame, 
                animation_group= animation_group, category_orders= category_orders, 
                labels= labels, orientation= orientation, 
                color_discrete_sequence=color_discrete_sequence, 
                color_discrete_map=color_discrete_map, line_dash_sequence=line_dash_sequence, 
                line_dash_map= line_dash_map, log_x= log_x, log_y= log_y, 
                range_x= range_x, range_y= range_y, line_shape= line_shape, 
                render_mode= render_mode, title= title, template= template, width= width, 
                height=height)
    fig.show()

    if save == True:
        save_my_image(name= name, parent_directory= parent_directory, destination= destination, fig= fig)


def create_bar_plot(data_frame=None, x=None, y=None, 
                    color=None, facet_row=None, facet_col=None, 
                    facet_col_wrap=0, facet_row_spacing=None, 
                    facet_col_spacing=None, hover_name=None, 
                    hover_data=None, custom_data=None, text=None,
                    error_x=None, error_x_minus=None, 
                    error_y=None, error_y_minus=None, animation_frame=None, 
                    animation_group=None, category_orders=None, 
                    labels=None, color_discrete_sequence=None, 
                    color_discrete_map=None, color_continuous_scale=None, 
                    range_color=None, color_continuous_midpoint=None, 
                    opacity=None, orientation=None, barmode='relative', 
                    log_x=False, log_y=False, range_x=None, range_y=None, 
                    title=None, template=None, width=None, height=None,
                    destination= 'Images', parent_directory= None, name= None):
    """
                        ---What it does---
    This function creates a bar plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
    
    fig = px.bar(data_frame= data_frame, x= x, y= y, 
                    color= color, facet_row= facet_row, facet_col= facet_col, 
                    facet_col_wrap= facet_col_wrap, hover_name= hover_name, 
                    hover_data= hover_data, custom_data= custom_data, text= text, 
                    error_x= error_x, error_x_minus= error_x_minus, 
                    error_y= error_y, error_y_minus= error_y_minus,
                    animation_frame= animation_frame, 
                    animation_group= animation_group, category_orders= category_orders, 
                    labels= labels, color_discrete_sequence= color_discrete_sequence, 
                    color_discrete_map= color_discrete_map, 
                    color_continuous_scale= color_continuous_scale, 
                    range_color= range_color, 
                    color_continuous_midpoint= color_continuous_midpoint, 
                    opacity= opacity, orientation= orientation, barmode= barmode, 
                    log_x= log_x, log_y= log_y, range_x= range_x, range_y= range_y, 
                    title= title, template= template, width= width, height= height)
    
    fig.show()

    if save == True:
        save_my_image(name= name, parent_directory= parent_directory, destination= destination, fig= fig)


def create_pie_plot(data_frame=None, names=None, values=None, 
                    color=None, color_discrete_sequence=None, 
                    color_discrete_map=None, hover_name=None, 
                    hover_data=None, custom_data=None, labels=None, 
                    title=None, template=None, width=None, height=None, 
                    opacity=None, hole=None, save= False, destination= 'Images', 
                    parent_directory= None, name= None):
    """
                        ---What it does---
    This function creates a pie plot. Then stores the plot in html format if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)
        - The standard plotly express argument for this function

                        ---What it returns---
    This function does not return anything
    """
        
    fig = px.pie(data_frame= data_frame, names= names, values= values, 
                    color= color, color_discrete_sequence= color_discrete_sequence, 
                    color_discrete_map= color_discrete_map, hover_name= hover_name, 
                    hover_data= hover_data, custom_data= custom_data, labels= labels, 
                    title= title, template= template, width= width, height= height, 
                    opacity= opacity, hole= hole)

    fig.show()

    if save == True:
        save_my_image(name= name, parent_directory= parent_directory, destination= destination, fig= fig)



def create_heat_map(data = None, save= False, destination= 'Images', 
                    parent_directory= None, name= None):
    """
    TODO lack in function options
                        ---What it does---
    Creates a heat map plot selecting only numerical data.Then writes an htm file with the plot if desired.

                        ---What it needs---
        - Data to plot (data).
        - A save state for saving up your plots (save). Set to False by default
        - A ending path for your html to be stored (path). Set to /Output by default
        - The name of your plot (name)

                        ---What it returns---
    This function does not return anything
    """

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    corr = data.select_dtypes(include= numerics).corr()

    fig = px.imshow(corr)
    fig.show()

    if save == True:
        save_my_image(name= name, parent_directory= parent_directory, destination= destination, fig= fig)


def create_map():
    pass


