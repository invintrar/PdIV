def drawWayOnImage(way, color, im, pc, image_scale, thickness=-1, x_offset=0.0, y_offset=0.0):
    # Get the shape of this way and draw it as a poly
    nds = []
    for node in way.get_nodes(resolve_missing=True): # Allow automatically resolving missing nodes, but this is VERY slow with the API requests, try to request them above instead
        nds.append(pc.latlonToCV2(node.lat, node.lon, image_scale, x_offset, y_offset))
    # Uses points and not image pixels, so flip the x and y
    nds = np.array(nds)
    nds[:,[0, 1]] = nds[:,[1, 0]]
    nds = np.int32([nds]) # Bug with fillPoly, needs explict cast to 32bit
    cv2.fillPoly(im, nds, color) 

    # Add option to draw shape again, but with thick line
    # Use this to automatically expand some shapes, for example water
    # For better masking
    if thickness > 0:
        # Need to draw again since fillPoly has no line thickness options that I've found
        cv2.polylines(im, nds, True, color, thickness, lineType=cv2.LINE_AA) 