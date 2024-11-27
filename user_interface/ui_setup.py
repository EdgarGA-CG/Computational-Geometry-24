from matplotlib import pyplot as plt
import ipywidgets as widgets

def set_ui_elements_solution(idb,sol_edges):
    uid_list = widgets.Dropdown(
        options = [instance.instance_uid for instance in idb],
        value = None,
        layout = widgets.Layout(width='50%', height='60px%'),
        description = 'UID'
    )

    edges_list = widgets.Dropdown(
        options = {str(value):value for value in sol_edges},
        value = None,
        description = 'Edge'
    )
    return uid_list, edges_list


def set_ui_elements_triangulations(idb,triang):
    uid_list = widgets.Dropdown(
        options = [instance.instance_uid for instance in idb],
        value = None,
        layout = widgets.Layout(width='50%', height='60px%'),
        description = 'UID'
    )

    triang_list = widgets.Dropdown(
        options = {str(value):value for value in triang},
        value = None,
        description = 'Triangulation'
    )
    return uid_list, triang_list

def update_edges_list(uid_changed,edges_list,sol_edges,sel_edge):
    if uid_changed:
        edges_list.options = {str(value):value for value in sol_edges} # Set options for new UID selected
        edges_list.value = sol_edges[0] # Set initial value from new solution edges in new selected UID
        sel_edge = sol_edges[0] # Pass first solution edge to selected edge
    return edges_list,sel_edge

def update_triang_list(uid_changed,triang_list,triang,sel_triang):
    if uid_changed:             
        triang_list.options = {str(value):value for value in triang} # Update triangulation list
        triang_list.value = triang[0] # Set initial value to first value on options list
        sel_triang = triang[0] # Update selected triangulation to avoid use triangulation from previous UID
    return triang_list,sel_triang