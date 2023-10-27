from pycfg.pycfg import PyCFG, CFGNode, slurp 
import argparse

#Acks:
# This file is mostly from:
# https://www.geeksforgeeks.org/draw-control-flow-graph-using-pycfg-python/

if __name__ == '__main__': 
    parser = argparse.ArgumentParser() 
  
    parser.add_argument('pythonfile', help ='The python file to be analyzed') 
    args = parser.parse_args() 
    arcs = [] 
  
    cfg = PyCFG() 
    cfg.gen_cfg(slurp(args.pythonfile).strip()) 
    g = CFGNode.to_graph(arcs) 
    g.draw(args.pythonfile + '.png', prog ='dot')
