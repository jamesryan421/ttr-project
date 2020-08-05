"""
Python class for functionalities of graphs, as pertaining to Ticket To Ride
Code adapted from: https://www.python-course.eu/graphs_python.php
"""

class Graph(object):
    
    def __init__(self,graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.__graph_dict=graph_dict
    
    def vertices(self):
        return list(self.__graph_dict.keys())
    
    def edges(self):
        return self.__generate_edges()
    
    def add_vertex(self,vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex]=[]
    
    def add_edge(self,edge):
        edge=set(edge)
        vertex1=edge.pop()
        if edge:
            #Not a loop
            vertex2=edge.pop()
        else:
            #Loop
            vertex2=vertex1
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1]=[vertex2]
    
    def __generate_edges(self):
        edges=[]
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor,vertex} not in edges:
                    edges.append({vertex,neighbor})
        return edges
    
    def __str__(self):
        res="Vertices: "
        for k in self.__graph_dict:
            res+=str(k)+" "
        res+="\nedges: "
        for edge in self.__generate_edges():
            res+=str(edge)+" "
        return res
    
    def find_path(self,start_vertex,end_vertex,path=[]):
        graph=self.__graph_dict
        path=path+[start_vertex]
        if start_vertex==end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path=self.find_path(vertex,end_vertex,path)
            if extended_path:
                return extended_path
        return None
    
    def find_all_paths(self,start_vertex,end_vertex,path=[]):
        graph=self.__graph_dict
        path=path+[start_vertex]
        if start_vertex==end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths=[]
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths=self.find_all_paths(vertex,end_vertex,path)
                for p in extended_paths:
                    paths.append(p)
        return paths
