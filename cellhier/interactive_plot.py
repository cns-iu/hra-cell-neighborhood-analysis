import bokeh.io
from bokeh.io import output_notebook, show

from bokeh.layouts import row,column
from bokeh.models import CustomJS, ColumnDataSource,Button,LogColorMapper,LinearColorMapper
from bokeh.plotting import figure
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap
from bokeh.resources import INLINE
bokeh.io.output_notebook(INLINE)
import pandas as pd


def select_points_scatter(data,X = 'X', Y = 'Y', hue = 'hue',factor_type = 'categorical',group = 'group',alpha = .6,plot_width = 400,plot_height = 400,palette = Spectral6,vmin = 0, vmax = 3
              ):
    '''source:  dataframe with required columns for x and y positions as well as group name and color for each group.'''
    #initialize coloring
    if factor_type == 'categorical':
        color = factor_cmap(hue,palette = palette,factors = list(data[hue].unique()))
    elif factor_type == 'continuous':
        color_mapper = LinearColorMapper(palette = palette,low = vmin,high = vmax)
        color  = {'field':hue,'transform':color_mapper}
    else:
        raise ValueError('factor_type must be \'continuous\' or \'categorical\'') 
        

    
    #initialize  main plot
    s1 = ColumnDataSource(data=data)
    
    p1 = figure(plot_width=400, plot_height=400, tools="pan,wheel_zoom,lasso_select,reset", title="Select Here")
    p1.circle(X, Y, source=s1, alpha = alpha,color = color)

    #### initialize selected plot
    s2 = ColumnDataSource(data={X:[],Y:[],group:[],hue:[]})
    p2 = figure(plot_width=400, plot_height=400,
            tools="", title="Watch Here",
           x_range = p1.x_range,y_range = p1.y_range)
    p2.circle(X,Y, source=s2, alpha=alpha,color = color)
    
    #initialize table to show selected points
    columns = [TableColumn(field =X,  title = "X axis"),
           TableColumn(field =Y,  title = "Y axis"),
          TableColumn(field =group,  title = group)]

    table = DataTable(source =s2, columns = columns, width =155, height = plot_height-20)
    
    #define callback when points are selected
    s1.selected.js_on_change('indices', CustomJS(args=dict(s1=s1, s2=s2, table=table,
                                                       X = X, Y = Y,hue = hue,group = group,
                                                      ), code="""
        var inds = cb_obj.indices;
        var d1 = s1.data;
        var d2 = s2.data;
        d2[X] = []
        d2[Y] = []
        d2[hue] = []
        d2[group] = []
        
        for (var i = 0; i < inds.length; i++) {
            d2[X].push(d1[X][inds[i]])
            d2[Y].push(d1[Y][inds[i]])
            d2[hue].push(d1[hue][inds[i]])
            d2[group].push(d1[group][inds[i]])
        }
        s2.change.emit();
        table.change.emit();
    """)
)
    savebutton = Button(label="Save", button_type="success",width =155)

    javaScript="""
    function table_to_csv(source) {
        const columns = Object.keys(source.data)
        const nrows = source.get_length()
        const lines = [columns.join(',')]

        for (let i = 0; i < nrows; i++) {
            let row = [];
            for (let j = 0; j < columns.length; j++) {
                const column = columns[j]
                row.push(source.data[column][i].toString())
            }
            lines.push(row.join(','))
        }
        return lines.join('\\n').concat('\\n')
    }


    const filename = 'data_result.csv'
    filetext = table_to_csv(source)
    const blob = new Blob([filetext], { type: 'text/csv;charset=utf-8;' })

    //addresses IE
    if (navigator.msSaveBlob) {
        navigator.msSaveBlob(blob, filename)
    } else {
        const link = document.createElement('a')
        link.href = URL.createObjectURL(blob)
        link.download = filename
        link.target = '_blank'
        link.style.visibility = 'hidden'
        link.dispatchEvent(new MouseEvent('click'))
    }
    """

    savebutton.callback = CustomJS(
        args=dict(source=s2,index_col = group),
        code=javaScript)

    layout = row(p1, p2, column(table,savebutton))

    show(layout)
    
def show_cells_on_stack(data,stack,X='X',Y='Y',channelNames = None,
                        group = 'group',hue = 'hue',palette = 'Spectral11',
                        default = 0, alpha = .5,
                        stack_dw = None,stack_dh = None,
                        plot_width = 400,plot_height = 400,
                       vmin = 0,vmax = 3,znorm = True):
    
    '''
    stack:  np. array of shape (nchannels,height,width)
    '''
    from bokeh.models import CheckboxGroup,RadioButtonGroup,Legend, LegendItem
    if not channelNames:
        channelNames = ['Channel '+str(i) for i in range(len(stack))]
        print (channelNames)
    
    s1 = ColumnDataSource(data=data)
    p1 = figure(plot_width=plot_width, plot_height=plot_height, tools="pan,wheel_zoom,lasso_select,reset")
    

    channels = {}  
    for i,channel in enumerate(channelNames):
        img = stack[i]
        if znorm:
            img = (img-img.mean())/img.std()
        
        if not stack_dw:
            stack_dw = plot_width
        if not stack_dh:
            stack_dh = plot_height
            
        channels[i] =  p1.image(image = [img],x = [0],y = [0],dw = [stack_dw],dh = [stack_dh],
                                color_mapper = LogColorMapper(palette = palette,low = vmin,high = vmax),
            global_alpha = alpha,visible =(i==default))
        
    plots = {}
    groups = list(data[group].unique())
    for g_id in groups:
        s2 = ColumnDataSource(data = data[data[group]==g_id])
        scatter  = p1.circle(X, Y, source=s2, alpha = 1,color = 'hue')#,legend_label = str(g_id))
        scatter.visible = False
        plots[g_id] = scatter
    


    select_celltype = CheckboxGroup(labels = groups,active = [],
                                 width = 100)
    select_channel = RadioButtonGroup(labels = channelNames,active = default,
                              width = 100,orientation = 'horizontal')

    select_celltype.callback = CustomJS(args = {'plots':plots,'groups':groups,
                                             'msel':select_celltype,'fig':p1},code = """
            //fig.title.text = 'new Title'
            for (var i =0; i<groups.length;i++){
               plots[groups[i]].visible = msel.active.indexOf(i)>-1
            }
               """)

    select_channel.callback = CustomJS(args = {'channels':channels,'sel':select_channel,

                                          'fig':p1},code = """

        //fig.title.text = Object.keys(channels).length.toString()
        for (var i =0; i<Object.keys(channels).length;i++){
            channels[i].visible = false
        }
        var val = sel.active
        channels[val].visible = true


        /**
        if (val==0){
            fig.title.text = 'confirm upper'
            chan1.visible = true
            chan2.visible = false
            //bg_channel = [z[0]]

        }else if (val==1){
            fig.title.text = 'confirm lower'
            chan1.visible = false
            chan2.visible = true
            //bg_channel = [z[1]]

        }
        **/



    """)
    
  

    layout = row(p1,column(select_celltype,select_channel))
    show(layout)

    

    

    