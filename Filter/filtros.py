import math
import numpy as np 
import statistics as sta

def aritmetica(img1):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Si hacemos la ventana de 3x3 al principio de la imagen 0,0 tenemos de vecinos solo 0,1;1,0;1;1 como vemos solo cuantro elementos
            if( i == 0 and j==0):
                img[i][j]= (img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])/4
                continue
            # Igual pasa si estamos en la esquina dereche    
            if(i == 0 and j == img.shape[1]-1):
                img[i][j]= (img[i][j] + img[i][j-1] + img[i+1][j-1] + img[i+1][j])/4
                continue
            # Esquina inferior 
            if(i == img.shape[0]-1 and j== 0):
                img[i][j]= (img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1])/4
                continue
            # Esquina inferior derecha
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                img[i][j]= (img[i][j] + img[i-1][j] + img[i-1][j-1] + img[i][j-1])/4
                continue
            # En la fila 0 los vecinos son 5 y el elemento en total 6
            if(i == 0 ):
                img[i][j]= (img[i][j-1] + img[i][j] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1])/6
                continue
            # En la columno 0 la ventana consta de 6 elementos
            if(j == 0 ):
                img[i][j]= (img[i-1][j] + img[i][j] + img[i+1][j] + img[i-1][j+1] + img[i][j+1] + img[i+1][j+1])/6
                continue
            # En la ultima fila tenemos tambien seis elementos
            if(i == img.shape[0]-1 ):
                img[i][j]= (img[i][j-1] + img[i][j] + img[i][j+1] + img[i-1][j-1] + img[i-1][j] + img[i-1][j+1])/6
                continue
            # En la ultima columna tenemos 6 elementos
            if(j == img.shape[1]-1 ):
                img[i][j]= (img[i-1][j] + img[i][j] + img[i+1][j] + img[i-1][j-1] + img[i][j-1] + img[i+1][j-1])/6
                continue
            # En el resto de casos tenemos nueve elementos    
            img[i][j]= (img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j] + img[i][j+1] + img[i][j-1] + img[i+1][j] + img[i][j+1])/9
    
    return img

def armonica(img1):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if( i == 0 and j==0):
                img[i][j]= 4/(1/img[i][j] + 1/img[i][j+1] + 1/img[i+1][j] + 1/img[i+1][j+1])
                continue
        
            if(i == 0 and j == img.shape[1]-1):
                img[i][j]= 4/(1/img[i][j] + 1/img[i][j-1] + 1/img[i+1][j-1] + 1/img[i+1][j])
                continue
        
            if(i == img.shape[0]-1 and j== 0):
                img[i][j]= 4/(1/img[i][j] + 1/img[i][j+1] + 1/img[i-1][j] + 1/img[i-1][j+1])
                continue
            
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                img[i][j]= 4/(1/img[i][j] + 1/img[i-1][j] + 1/img[i-1][j-1] + 1/img[i][j-1])
                continue
            
            if(i == 0 ):
                img[i][j]= 6/(1/img[i][j-1] + 1/img[i][j] + 1/img[i][j+1] + 1/img[i+1][j-1] + 1/img[i+1][j] + 1/img[i+1][j+1])
                continue
            
            if(j == 0 ):
                img[i][j]= 6/(1/img[i-1][j] + 1/img[i][j] + 1/img[i+1][j] + 1/img[i-1][j+1] + 1/img[i][j+1] + 1/img[i+1][j+1])
                continue
            
            if(i == img.shape[0]-1 ):
                img[i][j]= 6/(1/img[i][j-1] + 1/img[i][j] + 1/img[i][j+1] + 1/img[i-1][j-1] + 1/img[i-1][j] + 1/img[i-1][j+1])
                continue
            
            if(j == img.shape[1]-1 ):
                img[i][j]= 6/(1/img[i-1][j] + 1/img[i][j] + 1/img[i+1][j] + 1/img[i-1][j-1] + 1/img[i][j-1] + 1/img[i+1][j-1])
                continue
                
            img[i][j]= 9/(1/img[i-1][j-1] + 1/img[i-1][j] + 1/img[i-1][j+1] + 1/img[i][j-1] + 1/img[i][j] + 1/img[i][j+1] + 1/img[i][j-1] + 1/img[i+1][j] + 1/img[i][j+1])
    
    return img
     
def geometrica(img1):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if( i == 0 and j==0):
                img[i][j] = pow((img[i][j] * img[i][j+1] * img[i+1][j] * img[i+1][j+1]), 1/4)
                continue
                  
            if(i == 0 and j == img.shape[1]-1):
                img[i][j]= pow((img[i][j] * img[i][j-1] * img[i+1][j-1] * img[i+1][j]),1/4)
                continue
        
            if(i == img.shape[0]-1 and j== 0):
                img[i][j]= pow((img[i][j] * img[i][j+1] * img[i-1][j] * img[i-1][j+1]),1/4)
                continue
            
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                img[i][j]= pow((img[i][j] * img[i-1][j] * img[i-1][j-1] * img[i][j-1]),1/4)
                continue
            
            if(i == 0 ):
                img[i][j]= pow((img[i][j-1] * img[i][j] * img[i][j+1] * img[i+1][j-1] * img[i+1][j] * img[i+1][j+1]),1/6)
                continue
            
            if(j == 0 ):
                img[i][j]= pow((img[i-1][j] * img[i][j] * img[i+1][j] * img[i-1][j+1] * img[i][j+1] * img[i+1][j+1]),1/6)
                continue
            
            if(i == img.shape[0]-1 ):
                img[i][j]= pow((img[i][j-1] * img[i][j] * img[i][j+1] * img[i-1][j-1] * img[i-1][j] * img[i-1][j+1]),1/6)
                continue
            
            if(j == img.shape[1]-1 ):
                img[i][j]= pow((img[i-1][j] * img[i][j] * img[i+1][j] * img[i-1][j-1] * img[i][j-1] * img[i+1][j-1]),1/6)
                continue
                
            img[i][j]= pow((img[i-1][j-1] * img[i-1][j] * img[i-1][j+1] * img[i][j-1] * img[i][j] * img[i][j+1] * img[i][j-1] * img[i+1][j] * img[i][j+1]),1/9)
    
    return img

def charmonic(img1):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if( i == 0 and j==0):
                img[i][j]= ((img[i][j]**2 + img[i][j+1]**2 + img[i+1][j]**2 + img[i+1][j+1]**2)/4) / ((img[i][j] + img[i][j+1] + img[i+1][j] + img[i+1][j+1])/4)
                continue
        
            if(i == 0 and j == img.shape[1]-1):
                img[i][j]= ((img[i][j]**2 + img[i][j-1]**2 + img[i+1][j-1]**2 + img[i+1][j]**2)/4) / ((img[i][j] + img[i][j-1]+ img[i+1][j-1]+ img[i+1][j])/4)
                continue
        
            if(i == img.shape[0]-1 and j== 0):
                img[i][j]= ((img[i][j]**2 + img[i][j+1]**2 + img[i-1][j]**2 + img[i-1][j+1]**2)/4) / ((img[i][j] + img[i][j+1] + img[i-1][j] + img[i-1][j+1])/4)
                continue
            
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                img[i][j]= ((img[i][j]**2 + img[i-1][j]**2 + img[i-1][j-1]**2 + img[i][j-1]**2)/4) / ((img[i][j] + img[i-1][j] + img[i-1][j-1] + img[i][j-1])/4)
                continue
            
            if(i == 0 ):
                img[i][j]= ((img[i][j-1]**2 + img[i][j]**2 + img[i][j+1]**2 + img[i+1][j-1]**2 + img[i+1][j]**2 + img[i+1][j+1]**2)/6) / ((img[i][j-1] + img[i][j] + img[i][j+1] + img[i+1][j-1] + img[i+1][j] + img[i+1][j+1])/6)
                continue
            
            if(j == 0 ):
                img[i][j]= ((img[i-1][j]**2 + img[i][j]**2 + img[i+1][j]**2 + img[i-1][j+1]**2 + img[i][j+1]**2 + img[i+1][j+1]**2)/6) / ((img[i-1][j] + img[i][j] + img[i+1][j] + img[i-1][j+1] + img[i][j+1] + img[i+1][j+1])/6)
                
                continue
            
            if(i == img.shape[0]-1 ):
                img[i][j]= ((img[i][j-1]**2 + img[i][j]**2 + img[i][j+1]**2 + img[i-1][j-1]**2 + img[i-1][j]**2 + img[i-1][j+1]**2)/6) / ((img[i][j-1] + img[i][j] + img[i][j+1] + img[i-1][j-1] + img[i-1][j] + img[i-1][j+1])/6)
                continue
            
            if(j == img.shape[1]-1 ):
                img[i][j]= ((img[i-1][j]**2 + img[i][j]**2 + img[i+1][j]**2 + img[i-1][j-1]**2 + img[i][j-1]**2 + img[i+1][j-1]**2)/6) / ((img[i-1][j] + img[i][j] + img[i+1][j] + img[i-1][j-1] + img[i][j-1] + img[i+1][j-1])/6)
                continue
                
            img[i][j]= ((img[i-1][j-1]**2 + img[i-1][j]**2 + img[i-1][j+1]**2 + img[i][j-1]**2 + img[i][j]**2 + img[i][j+1]**2 + img[i][j-1]**2 + img[i+1][j]**2 + img[i][j+1]**2)/9) / ((img[i-1][j-1] + img[i-1][j] + img[i-1][j+1] + img[i][j-1] + img[i][j] + img[i][j+1] + img[i][j-1] + img[i+1][j] + img[i][j+1])/9)
    
    return img

def alnr(img1,varn):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Si hacemos la ventana de 3x3 al principio de la imagen 0,0 tenemos de vecinos solo 0,1;1,0;1;1 como vemos solo cuantro elementos
            if( i == 0 and j==0):
                lista = np.array([img[i][j] , img[i][j+1] , img[i+1][j] , img[i+1][j+1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media  
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # Igual pasa si estamos en la esquina dereche    
            if(i == 0 and j == img.shape[1]-1):
                lista = np.array([img[i][j], img[i][j-1], img[i+1][j-1], img[i+1][j]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = varianza
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # Esquina inferior 
            if(i == img.shape[0]-1 and j== 0):
                lista = np.array([img[i][j], img[i][j+1], img[i-1][j], img[i-1][j+1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # Esquina inferior derecha
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                lista = np.array([img[i][j], img[i-1][j], img[i-1][j-1], img[i][j-1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # En la fila 0 los vecinos son 5 y el elemento en total 6
            if(i == 0 ):
                lista = np.array([img[i][j-1], img[i][j], img[i][j+1], img[i+1][j-1], img[i+1][j], img[i+1][j+1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # En la columno 0 la ventana consta de 6 elementos
            if(j == 0 ):
                lista = np.array([img[i-1][j], img[i][j], img[i+1][j], img[i-1][j+1], img[i][j+1], img[i+1][j+1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue
            # En la ultima fila tenemos tambien seis elementos
            if(i == img.shape[0]-1 ):
                lista = np.array([img[i][j-1], img[i][j], img[i][j+1], img[i-1][j-1], img[i-1][j], img[i-1][j+1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue                
            # En la ultima columna tenemos 6 elementos
            if(j == img.shape[1]-1 ):
                lista = np.array([img[i-1][j], img[i][j], img[i+1][j], img[i-1][j-1], img[i][j-1], img[i+1][j-1]])
                media = lista.mean()
                varianza = lista.var()
                if(varn == 0):
                    img[i][j]= img[i][j]
                    continue
                elif(varianza > varn):
                    img[i][j] = varn
                    continue
                elif(varianza == varn):
                    img[i][j] = media
                    continue
                elif(varianza == 0):
                    img[i][j]=media
                else:
                    img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue 
            # En el resto de casos tenemos nueve elementos
            lista = np.array([img[i-1][j-1], img[i-1][j], img[i-1][j+1], img[i][j-1], img[i][j], img[i][j+1], img[i][j-1], img[i+1][j], img[i][j+1]])    
            media = lista.mean()
            varianza = lista.var()
            if(varn == 0):
                img[i][j]= img[i][j]
                continue
            elif(varianza > varn):
                img[i][j] = varn
                continue
            elif(varianza == varn):
                img[i][j] = varianza
                continue
            elif(varianza == 0):
                img[i][j]=media
            else:
                img[i][j]= img[i][j]-(varn/varianza)*(img[i][j]-media) 
                continue 
    
    return img

def am(img1):
    img = img1.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # Si hacemos la ventana de 3x3 al principio de la imagen 0,0 tenemos de vecinos solo 0,1;1,0;1;1 como vemos solo cuantro elementos
            if( i == 0 and j==0):
                lista = np.array([img[i][j], img[i][j+1], img[i+1][j], img[i+1][j+1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # Igual pasa si estamos en la esquina dereche    
            if(i == 0 and j == img.shape[1]-1):
                lista = np.array([img[i][j], img[i][j-1], img[i+1][j-1] + img[i+1][j]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # Esquina inferior 
            if(i == img.shape[0]-1 and j== 0):
                lista = np.array([img[i][j], img[i][j+1], img[i-1][j], img[i-1][j+1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # Esquina inferior derecha
            if(i == img.shape[0]-1 and j== img.shape[1]-1):
                lista = np.array([img[i][j], img[i-1][j], img[i-1][j-1], img[i][j-1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # En la fila 0 los vecinos son 5 y el elemento en total 6
            if(i == 0 ):
                lista = np.array([img[i][j-1], img[i][j], img[i][j+1], img[i+1][j-1], img[i+1][j], img[i+1][j+1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
                
            # En la columno 0 la ventana consta de 6 elementos
            if(j == 0 ):
                lista = np.array([img[i-1][j], img[i][j], img[i+1][j], img[i-1][j+1], img[i][j+1], img[i+1][j+1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # En la ultima fila tenemos tambien seis elementos
            if(i == img.shape[0]-1 ):
                lista = np.array([img[i][j-1], img[i][j], img[i][j+1], img[i-1][j-1], img[i-1][j], img[i-1][j+1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # En la ultima columna tenemos 6 elementos
            if(j == img.shape[1]-1 ):
                lista = np.array([img[i-1][j], img[i][j], img[i+1][j], img[i-1][j-1], img[i][j-1], img[i+1][j-1]])
                vmax = lista.max()
                vmed = sta.median(lista)
                vmin = lista.min()
                A1 = vmed - vmin
                A2 = vmed - vmax
                if(A1 > 0 and A2 < 0):
                    B1 = img[i][j] - vmin
                    B2 = img[i][j] -vmax
                    if(B1 > 0 and B2 < 0):
                        img[i][j]= img[i][j]
                        continue
                    else:
                        img[i][j] = vmed
                        continue
                else:
                    img[i][j] = vmed     
                continue
            # En el resto de casos tenemos nueve elementos    
            lista = np.array([img[i-1][j-1], img[i-1][j], img[i-1][j+1], img[i][j-1], img[i][j], img[i][j+1], img[i][j-1], img[i+1][j], img[i][j+1]])
            vmax = lista.max()
            vmed = sta.median(lista)
            vmin = lista.min()
            A1 = vmed - vmin
            A2 = vmed - vmax
            if(A1 > 0 and A2 < 0):
                B1 = img[i][j] - vmin
                B2 = img[i][j] -vmax
                if(B1 > 0 and B2 < 0):
                    img[i][j]= img[i][j]
                    continue
                else:
                    img[i][j] = vmed
                    continue
            else:
                img[i][j] = vmed     
                continue
    
    return img