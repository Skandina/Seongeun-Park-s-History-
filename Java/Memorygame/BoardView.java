import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.border.LineBorder;
import javax.swing.Timer;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class BoardView implements Runnable {

    static Player p1;
    static Player p2;
    static Card[] cards;
    static int counter = 0;
    static Timer timer;
    int index1;
    int index2;
    JLabel p1Score;
    JPanel p1Panel;
    JLabel p2Score;
    JPanel p2Panel;
  
    public int check (int index1, int index2) {
        
            int i1 = index1;
            int i2 = index2;

            //if the images are same
                if(cards[i1].getImageSorce() == cards[i2].getImageSorce()) {
                    
                    if (p1.isMyTurn()==true) {
                    p1.addScore();
                    p1Score.setText("Score: " + p1.getScore());

                    } else if (p2.isMyTurn()==true) {
                    p2.addScore();
                    p2Score.setText("Score: " + p2.getScore());
                    }
                    
                    //Eliminate the same cards.
                    timer = new Timer(1000, new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            //The cards filp back.
                            cards[i1].button.setVisible(false);
                            cards[i2].button.setVisible(false);
                            timer.stop();
                        }
                    });
                    timer.start();
                    
                //If the images are not the same
                }
                
                 else {//If the images are not the same
                    timer = new Timer(1000, new ActionListener() {
                        @Override
                        public void actionPerformed(ActionEvent e) {
                            //The cards filp back.
                            cards[i1].hideImage();
                            cards[i2].hideImage();
                            timer.stop();
                        }
                    });
                    
                    timer.start();
                    
                    if (p1.isMyTurn()==true) {
                        p1.No();
                        p2.Yes();
                        p1Panel.setBackground(Color.gray);
                        p2Panel.setBackground(Color.yellow);

                    } else if (p2.isMyTurn()==true) {
                        p1.Yes();
                        p2.No();
                        p1Panel.setBackground(Color.yellow);
                        p2Panel.setBackground(Color.gray);
                    }
                    
                } 
            
                counter = 0;
                return 0;
        }

    public int getCardIndex(JButton btn) {
        int index = 0;
        for(int i=0; i<16; i++){
            if (cards[i].button == btn) {
                index = i; 
            }
        }
        return index; 
    }

    public void run() {

        JFrame frame = new JFrame("Memory-game");

        JPanel gridPanel = new JPanel();
        gridPanel.setLayout(new GridLayout(4, 4, 10, 10));
        gridPanel.setBounds(150, 0, 530, 400); //x,y,width,heigth
        gridPanel.setBackground(Color.blue);

        p1 = new Player("Kevenn", true);
        p2 = new Player("Dinaaa", false);

        JLabel spacer = new JLabel("  ");

        p1Panel = new JPanel();
        p1Panel.setBounds(0, 0, 150, 200);
        p1Panel.setBackground(Color.yellow);
        JLabel p1Name = new JLabel(p1.getName());
        p1Score = new JLabel("Score: " + p1.getScore());
        p1Name.setFont(new Font("Verdana", 1, 20));
        p1Score.setFont(new Font("Verdana", 1, 15));
        p1Panel.setBorder(new LineBorder(Color.BLACK));
        p1Panel.add(p1Name);
        p1Panel.add(spacer);
        p1Panel.add(p1Score);

        p2Panel = new JPanel();
        p2Panel.setBounds(0, 200, 150, 200);
        p2Panel.setBackground(Color.gray);
        JLabel p2Name = new JLabel(p2.getName());
        p2Score = new JLabel("Score: " + p2.getScore());

        p2Name.setFont(new Font("Verdana", 1, 20));
        p2Score.setFont(new Font("Verdana", 1, 15));
        p2Panel.setBorder(new LineBorder(Color.BLACK));
        p2Panel.add(p2Name);
        p2Panel.add(spacer);
        p2Panel.add(p2Score);

        JPanel panel2 = new JPanel();
        panel2.setBounds(0, 400, 700, 60); //x,y,width,heigth
        panel2.setBackground(Color.blue);

        JButton new_game = new JButton("New");
        JButton end_game = new JButton("End");
        new_game.setBackground(Color.green);
        end_game.setBackground(Color.red);
        new_game.setForeground(Color.BLACK);
        end_game.setForeground(Color.BLACK);
        new_game.setPreferredSize(new Dimension(75, 25));
        end_game.setPreferredSize(new Dimension(75, 25));
        new_game.setBorder(new LineBorder(Color.BLACK));
        end_game.setBorder(new LineBorder(Color.BLACK));
        
        //Exit game button
        ActionListener al = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        };
        end_game.addActionListener(al);

        // restart game button
        ActionListener a2 = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                
                List<Card> cardsList = Arrays.asList(cards);
                Collections.shuffle(cardsList);
                cardsList.toArray(cards);
                
                for (int i = 0; i < cards.length; i++) {
                    gridPanel.remove(cards[i].button);
                }
                
                for (int i = 0; i < cards.length; i++) {
                    gridPanel.add(cards[i].button);
                }

                //Reset the score. 
                p1.resetScore();
                p2.resetScore();
                p1Score.setText("Score: " + p1.getScore());
                p2Score.setText("Score: " + p2.getScore());

                //Reset the buttons.
                for(int i = 0; i < cards.length; i++) {
                    cards[i].button.setVisible(true);
                    cards[i].hideImage();
                }
                //Reset the players.
                p1.Yes();
                p2.No();
                p1Panel.setBackground(Color.yellow);
                p2Panel.setBackground(Color.gray);
                
                //Reset the panel.
                gridPanel.repaint();

            }
        };
        new_game.addActionListener(a2);

        cards = new Card[16];

        String[] images = {
            "src/img/fruit01.png", "src/img/fruit02.png", "src/img/fruit03.png", "src/img/fruit04.png",
            "src/img/fruit05.png", "src/img/fruit06.png", "src/img/fruit07.png", "src/img/fruit08.png",
            "src/img/fruit01.png", "src/img/fruit02.png", "src/img/fruit03.png", "src/img/fruit04.png",
            "src/img/fruit05.png", "src/img/fruit06.png", "src/img/fruit07.png", "src/img/fruit08.png"
        };

        for (int j = 0; j < cards.length; j++) {
            cards[j] = new Card(new JButton(), images[j]);
        }

        //Shuffle the buttons.
        List<Card> cardsList = Arrays.asList(cards);
        Collections.shuffle(cardsList);
        cardsList.toArray(cards);

        //Matching the shuffled index to the buttons 
        for (int i = 0; i < cards.length; i++) {
              cards[i].setIndex(i);
                cards[i].button.addActionListener(new ActionListener() {

                    public void actionPerformed(ActionEvent e) {

                        JButton btn = (JButton) e.getSource();
                        counter++;

                        //if the card is opened
                        if(!(cards[getCardIndex(btn)].getStatus())) {
                            
                            if (counter == 1) {
                            cards[getCardIndex(btn)].showImage();
                            index1 = getCardIndex(btn);
                            } 
            
                            else if (counter == 2) { 
                            cards[getCardIndex(btn)].showImage();
                            index2 = getCardIndex(btn);
                            
                            check(index1, index2);
                            }

                        }
                    }
                });
        }

        for (int i = 0; i < cards.length; i++) {
            gridPanel.add(cards[i].button);
        }

        panel2.add(new_game);
        panel2.add(end_game);

        frame.add(gridPanel);
        frame.add(panel2);
        frame.add(p1Panel);
        frame.add(p2Panel);
        frame.setSize(700, 500);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }

}
