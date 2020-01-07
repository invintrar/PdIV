#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:09:48 2019

@author: Gustavo
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:44:53 2019

@author: Gustavo
"""


import cv2
import numpy as np
from skimage.util import img_as_float,img_as_ubyte
from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
from skimage import exposure
from skimage.segmentation import slic
import maxflow
from scipy.spatial import Delaunay
from scipy import interpolate


import sys
sys.path.insert(0, '/Users/Gustavo/AnacondaProjects/pythonCode/7_Librerias/segmentation/')
path='/Users/Gustavo/AnacondaProjects/pythonCode/0_Database/Varios/'





###########DRAWING FUNCTION##########################################
drawing = False # true if mouse is pressed
mode = True # if True, draw foreground if not draw background
ix,iy = -1,-1
xred=[]
yred=[]
xblue=[]
yblue=[]

# mouse callback function
def draw_line(event,x,y,flags,param):
    global ix,iy,drawing,mode,xred,yred,xblue,yblue

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.line(img,(ix,iy),(x,y),(0,0,255),5)
                ix=x
                iy=y
                xred.append(x)
                yred.append(y)
            else:
                cv2.line(img,(ix,iy),(x,y),(255,0,0),5)
                ix=x
                iy=y
                xblue.append(x)
                yblue.append(y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.line(img,(ix,iy),(x,y),(0,0,255),5)
            ix=x
            iy=y
            xred.append(x)
            yred.append(y)
        else:
            cv2.line(img,(ix,iy),(x,y),(255,0,0),5)
            ix=x
            iy=y
            xblue.append(x)
            yblue.append(y)
#######################################################################

##########GraphCUT###################################################
    # Calculate the SLIC superpixels, their histograms and neighbors
def superpixels_histograms_neighbors(img):
    # SLIC
    segments = slic(img, n_segments=500, compactness=20)
    segments_ids = np.unique(segments)

    # centers
    centers = np.array([np.mean(np.nonzero(segments==i),axis=1) for i in segments_ids])

    # H-S histograms for all superpixels
    hsv = cv2.cvtColor(img.astype('float32'), cv2.COLOR_BGR2HSV)
    bins = [20, 20] # H = S = 20
    ranges = [0, 360, 0, 1] # H: [0, 360], S: [0, 1]
    colors_hists = np.float32([cv2.calcHist([hsv],[0, 1], np.uint8(segments==i), bins, ranges).flatten() for i in segments_ids])

    # neighbors via Delaunay tesselation
    tri = Delaunay(centers)

    return (centers,colors_hists,segments,tri.vertex_neighbor_vertices)

# Get superpixels IDs for FG and BG from marking
def find_superpixels_under_marking(marking, superpixels):
    fg_segments = np.unique(superpixels[marking[:,:,0]!=255])
    bg_segments = np.unique(superpixels[marking[:,:,2]!=255])
    return (fg_segments, bg_segments)

# Sum up the histograms for a given selection of superpixel IDs, normalize
def cumulative_histogram_for_superpixels(ids, histograms):
    h = np.sum(histograms[ids],axis=0)
    return h / h.sum()

# Get a bool mask of the pixels for a given selection of superpixel IDs
def pixels_for_segment_selection(superpixels_labels, selection):
    pixels_mask = np.where(np.isin(superpixels_labels, selection), True, False)
    return pixels_mask

# Get a normalized version of the given histograms (divide by sum)
def normalize_histograms(histograms):
    return np.float32([h / h.sum() for h in histograms])

# Perform graph cut using superpixels histograms
def do_graph_cut(fgbg_hists, fgbg_superpixels, norm_hists, neighbors):
    num_nodes = norm_hists.shape[0]
    # Create a graph of N nodes, and estimate of 5 edges per node
    g = maxflow.Graph[float](num_nodes, num_nodes * 5)
    # Add N nodes
    nodes = g.add_nodes(num_nodes)

    hist_comp_alg = cv2.HISTCMP_KL_DIV

    # Smoothness term: cost between neighbors
    indptr,indices = neighbors
    for i in range(len(indptr)-1):
        N = indices[indptr[i]:indptr[i+1]] # list of neighbor superpixels
        hi = norm_hists[i]                 # histogram for center
        for n in N:
            if (n < 0) or (n > num_nodes):
                continue
            # Create two edges (forwards and backwards) with capacities based on
            # histogram matching
            hn = norm_hists[n]             # histogram for neighbor
            g.add_edge(nodes[i], nodes[n], 20-cv2.compareHist(hi, hn, hist_comp_alg),
                                           20-cv2.compareHist(hn, hi, hist_comp_alg))

    # Match term: cost to FG/BG
    for i,h in enumerate(norm_hists):
        if i in fgbg_superpixels[0]:
            g.add_tedge(nodes[i], 0, 1000) # FG - set high cost to BG
        elif i in fgbg_superpixels[1]:
            g.add_tedge(nodes[i], 1000, 0) # BG - set high cost to FG
        else:
            g.add_tedge(nodes[i], cv2.compareHist(fgbg_hists[0], h, hist_comp_alg),
                                  cv2.compareHist(fgbg_hists[1], h, hist_comp_alg))

    g.maxflow()
    return g.get_grid_segments(nodes)


########################################################################
def interpolacion(x,y):
       i = np.arange(len(x))

       interp_i = np.linspace(0, i.max(), 100 * i.max())

       xi = interpolate.interp1d(i, x, kind='cubic')(interp_i)  
       yi = interpolate.interp1d(i, y, kind='cubic')(interp_i)

       return xi,yi
########################################################################




img = img_as_float(cv2.imread("monito.jpg"))
    #img = img_as_float(cv2.imread(path+"images.jpeg"))
    #img = img_as_float(cv2.imread(path+"mula.jpg"))

img_copy = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_line)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):        
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()


BLUE = [255,0,0]
RED = [0,0,255]
xired,yired=interpolacion(xred,yred)
xiblue,yiblue=interpolacion(xblue,yblue)

img_marking=np.ones(img.shape)*255
img_marking[yred, xred,:]=[RED for i in range(len(xred))]
img_marking[yblue,xblue,:]=[BLUE for i in range(len(xblue))]
img_marking=img_marking.astype('uint8')



centers, colors_hists, segments, neighbors = superpixels_histograms_neighbors(img)
fg_segments, bg_segments = find_superpixels_under_marking(img_marking, segments)

    # get cumulative BG/FG histograms, before normalization
fg_cumulative_hist = cumulative_histogram_for_superpixels(fg_segments, colors_hists)
bg_cumulative_hist = cumulative_histogram_for_superpixels(bg_segments, colors_hists)
    
norm_hists = normalize_histograms(colors_hists)

graph_cut = do_graph_cut((fg_cumulative_hist, bg_cumulative_hist),
                             (fg_segments,        bg_segments),
                             norm_hists,
                             neighbors)



###########################################################################
fig, axes = plt.subplots(2, 2, figsize=(8,8))
ax = axes.flatten()
fig.suptitle('GRAPH CUT', fontsize=26)

img_rescale=cv2.cvtColor(exposure.rescale_intensity(img_copy,out_range=(0,255)).astype('uint8'),cv2.COLOR_BGR2RGB)
ax[0].imshow(img_rescale)
ax[0].set_axis_off()
ax[0].set_title("Original Image", fontsize=8)

ima1 = cv2.cvtColor(img.astype('uint8'),cv2.COLOR_BGR2RGB)
ax[1].imshow(ima1)
ax[1].set_axis_off()
ax[1].set_title("Mask", fontsize=8)

segmask = pixels_for_segment_selection(segments, np.nonzero(graph_cut))
mask=np.ones((segmask.shape[0],segmask.shape[1],3)).astype('uint8')*255
mask[:,:,0]=segmask
mask[:,:,1]=segmask
mask[:,:,2]=segmask
mono = img_rescale*mask
ax[2].imshow(mono)
ax[2].set_axis_off()
ax[2].set_title("Segmentation", fontsize=8)

img2 = mark_boundaries(img, segments)
img2[img_marking[:,:,0]!=255] = (1,0,0)
img2[img_marking[:,:,2]!=255] = (0,0,1)
ax[3].imshow(img2)
ax[3].set_axis_off()
ax[3].set_title("Contour ", fontsize=8)


    
    
    
    
    
    
    
    
    
    
    
    

