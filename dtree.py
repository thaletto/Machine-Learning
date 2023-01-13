from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus
def dtree(model):
    dot_data=StringIO()
    export_graphviz(model,out_file=dot_data,filled=True,rounded=False,special_characters=True)
    graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())
