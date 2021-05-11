import sys
import logging

def readlog(path): 
    """
    fonction qui lit un fichier et retourne le contenu dans une liste de liste 
    """  
    liste=[]
    with open(path, "r", encoding="utf-8") as f:  
        logging.info("ouverture du fichier par la fonction readlog")  
        line = "a"
        # print(line)
        # liste.append(line.strip().split(" ",1)[::-1])
        
        while line:
            line = f.readline()
            newline = line.strip()            
            if len(newline) != 0:
                l=newline.split(" ",1)[::-1]
                liste.append(l)               
    logging.info(f"stockage du fichier dans la variavle liste {liste}")           
    return liste


def main(path):    
    dico_final=readlog(path)        
    with open("result.txt", "w", encoding="utf-8") as f:  
        for e in readlog(path):
            f.write(str(e))



if __name__ == "__main__":
    path = sys.argv[1]
    logging.basicConfig(filename="prog.log",level=logging.DEBUG)
    sys.exit(main(path))