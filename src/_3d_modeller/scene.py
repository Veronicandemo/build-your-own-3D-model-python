class Scene(object):

    # the default depth from the camera to place an object at
    PLACE_DEPTH = 15.0

    def __init__(self):
        # The scene keeps a list of nodes that are displayed
        self.node_list = list()
        # Keep track of the currently selected node.
        # Actions may depend on whether or not something is selected
        self.selected_node = None

    def add_node(self, node):
        """ Add a new node to the scene """
        self.node_list.append(node)

    def render(self):
        """ Render the scene. """
        for node in self.node_list:
            node.render()

    def pick(self, start, direction, mat):
        """
        Execute selection.

        start, direction describe a Ray.
        mat is the inverse of the current modelview matrix for the scene.
        """
        if self.selected_node is not None:
            self.selected_node.select(False)
            self.selected_node = None

        # Keep track of the closest hit.
        mindist = sys.maxint
        closest_node = None
        for node in self.node_list:
            hit, distance = node.pick(start, direction, mat)
            if hit and distance < mindist:
                mindist, closest_node = distance, node

        # If we hit something, keep track of it.
        if closest_node is not None:
            closest_node.select()
            closest_node.depth = mindist
            closest_node.selected_loc = start + direction * mindist
            self.selected_node = closest_node

    def rotate_selected_color(self, forwards):
        """ Rotate the color of the currently selected node """
        if self.selected_node is None: return
        self.selected_node.rotate_color(forwards)

    def scale_selected(self, up):
        """ Scale the current selection """
        if self.selected_node is None: return
        self.selected_node.scale(up)

    def move_selected(self, start, direction, inv_modelview):
        """
        Move the selected node, if there is one.

        Consume:
        start, direction describes the Ray to move to
        mat is the modelview matrix for the scene
        """
        if self.selected_node is None: return

        # Find the current depth and location of the selected node
        node = self.selected_node
        depth = node.depth
        oldloc = node.selected_loc

        # The new location of the node is the same depth along the new ray
        newloc = (start + direction * depth)

        # transform the translation with the modelview matrix
        translation = newloc - oldloc
        pre_tran = numpy.array([translation[0], translation[1], translation[2], 0])
        translation = inv_modelview.dot(pre_tran)

        # translate the node and track its location
        node.translate(translation[0], translation[1], translation[2])
        node.selected_loc = newloc