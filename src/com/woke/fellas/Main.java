package com.woke.fellas;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main implements ActionListener{

    public Renderer renderer;
    public Main(){
        JFrame jframe = new JFrame();
        Timer timer = new Timer(20,this);

        jframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jframe.setSize(800, 600);
        jframe.setResizable(false);
        jframe.setVisible(true);
    }

    public void repaint(Graphics g){
        System.out.println("Repaint");
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        renderer.repaint();
    }

    public static void main(String[] args){
        Main main = new Main();
        System.out.println("Hello, World!");
    }
}
