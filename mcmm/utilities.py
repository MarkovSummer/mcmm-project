import numpy as np

def p(m):
    print("m: ", m )

def visit(active_vertex, Visited,ordered_vertices,T):
    """
    Recursive subfunction for kosarajus
    
    INPUT:
        
        - active_vertex     = An integer, which represents a vertex (in our numeration).
        - visited_vertices  = A list of the vertices already visited.
        - ordered_vertices  = an ordered list of graph vertices, that will grow to contain each vertex once.
        - T                 = A transition matrix (which is the adjacency matrix of a graph).
    
    OUTPUT:
        
        - It just adds in order vertices to the list ordered_vertices.
    
    """
    out=T[active_vertex,:]
    if not(active_vertex in visited_vertices):
        visited_vertices.append(active_vertex)
        for i in range(len(out)):
            if not(out[i]==0):
                visit(i, visited_vertices, ordered_vertices, T)
        ordered_vertices.insert(0,active_vertex)
    return



#Using Assign2 / kosarajus2 from pablo_testcode
def assign(active_vertex, root, vertexlist, components, T):
    """
    Recursive subfunction for kosarajus
    Strong components are to be represented by appointing a separate root vertex for each component,
    and assigning to each vertex the root vertex of its component.

    INPUT:

        - active_vertex = An integer, which represents a vertex (in our numeration) that has to be
                        assigned to some component.
        - root          = An integer, which represents a component.
        - vertexlist    = A list of vertices that are not yet introduced in the dictionary.

        - components    = A dictionary containing the vertices (numerated from 0 to n-1),
        each vertex associated to the root representing its component.
        - T             = A transition matrix (which is the adjacency matrix of a graph).

    OUTPUT:

        - It just changes the dictionary components, assigning to each vertex its root.

    """

    in_ = [i for i in T[:, active_vertex]]

    if active_vertex in vertexlist:

        if not root in components:
            components[root] = [active_vertex]
        elif root in components:
            components[root].append(active_vertex)
        LIST.remove(active_vertex)

        for i in range(len(in_)):
            if not (in_[i] == 0):
                assign(i, root, LIST, components, T)
    return



def kosarajus_algo(T):
    """
    Returns a dictionary containing the vertices and their inclusion in strong components.
    Strong components are to be represented by appointing a separate root vertex for each component,
    and assigning to each root the list of vertices inside that component.
    If the graph is represented as an adjacency matrix, the algorithm requires Ο(V^2) time.

    INPUT:

        - T = A transition matrix (which is the adjacency matrix of a graph).

    OUTPUT:

        - components = A dictionary containing the components (numerated from 0 to ..),
        each root associated to a list of vertices that are part of that component.

    """

    visited_vertices = []
    ordered_vertices = []

    components = {}

    vertices = [i for i in range(len(T[:, 1]))]
    vertexlist = list(vertices)

    for i in vertices:
        visit(i, visited_vertices, ordered_vertices, T)
    for vertex in ordered_vertices:
        assign(vertex, vertex, vertexlist, components, T)
    return components



def obtain_active_set(T):
    """
    Function for other parts of the project. It gets the biggest connected component of the matrix
    that we are given.

    INPUT:
        - T = The probability transition matrix of the markov model.

    OUTPUT:
        - C = A square matrix. The biggest connected component of the matrix.
        - vertexlist = A list of vertices. The states of T that correspond to the biggest component.

    """

    b = 0
    j = 0
    components = kosarajus_algo(T)
    for i in components:
        a = len(components[i])
        if a > b:
            b = a
            j = i
    vertexlist = list(components[j])
    C = np.array([T[i, :] for i in vertexlist])
    C = np.array([C[:, i] for i in vertexlist])
    return (C, vertexlist)