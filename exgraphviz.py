import graphviz
from sklearn.datasets import load_iris
from sklearn import tree

# dot_data = tree.export_graphviz(clf,out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")