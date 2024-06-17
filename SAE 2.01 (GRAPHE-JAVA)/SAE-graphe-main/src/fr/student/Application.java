package fr.student;

import fr.student.algo.GrapheList;
import fr.student.views.Interface;

public class Application {
    public static void main(String[] args){
        GrapheList graphe = new GrapheList();
        Interface ihm = new Interface(graphe);
        ihm.setVisible(true);
    }


}
