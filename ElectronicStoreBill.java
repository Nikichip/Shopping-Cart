import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ElectronicStoreBill extends JFrame implements ActionListener {

    JCheckBox laptop, phone, headphones, tablet, smartwatch, speaker, camera, charger, mouse, keyboard;
    JButton generateBill;
    JTextArea billArea;

    public ElectronicStoreBill() {
        setTitle("Electronic Store - Billing System");
        setSize(500, 550);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout(10, 10));
        getContentPane().setBackground(new Color(245, 245, 245));

        JLabel header = new JLabel("Select Items to Purchase", JLabel.CENTER);
        header.setFont(new Font("Segoe UI", Font.BOLD, 20));
        header.setForeground(new Color(30, 30, 30));
        add(header, BorderLayout.NORTH);

        JPanel itemPanel = new JPanel();
        itemPanel.setLayout(new GridLayout(5, 2, 10, 10));
        itemPanel.setBackground(Color.WHITE);
        itemPanel.setBorder(BorderFactory.createEmptyBorder(10, 30, 10, 30));

        laptop = new JCheckBox("Laptop - ₹60,000");
        phone = new JCheckBox("Smartphone - ₹25,000");
        headphones = new JCheckBox("Headphones - ₹2,000");
        tablet = new JCheckBox("Tablet - ₹18,000");
        smartwatch = new JCheckBox("Smartwatch - ₹5,000");
        speaker = new JCheckBox("Bluetooth Speaker - ₹3,500");
        camera = new JCheckBox("Digital Camera - ₹15,000");
        charger = new JCheckBox("Fast Charger - ₹1,200");
        mouse = new JCheckBox("Wireless Mouse - ₹800");
        keyboard = new JCheckBox("Mechanical Keyboard - ₹2,500");

        itemPanel.add(laptop);
        itemPanel.add(phone);
        itemPanel.add(headphones);
        itemPanel.add(tablet);
        itemPanel.add(smartwatch);
        itemPanel.add(speaker);
        itemPanel.add(camera);
        itemPanel.add(charger);
        itemPanel.add(mouse);
        itemPanel.add(keyboard);

        add(itemPanel, BorderLayout.CENTER);

        // Generate Bill button
        generateBill = new JButton("Generate Bill");
        generateBill.setFont(new Font("Segoe UI", Font.BOLD, 16));
        generateBill.setBackground(new Color(0, 153, 76));
        generateBill.setForeground(Color.WHITE);
        generateBill.setFocusPainted(false);
        generateBill.addActionListener(this);

        add(generateBill, BorderLayout.SOUTH);

        // Bill Area
        billArea = new JTextArea();
        billArea.setEditable(false);
        billArea.setFont(new Font("Consolas", Font.PLAIN, 14));
        billArea.setBorder(BorderFactory.createTitledBorder("Bill Details"));
        billArea.setBackground(new Color(250, 250, 250));
        add(new JScrollPane(billArea), BorderLayout.EAST);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        int total = 0;
        StringBuilder bill = new StringBuilder();
        bill.append("=========== ELECTRONIC STORE BILL ===========\n");
        bill.append(String.format("%-25s %10s\n", "Item", "Price"));
        bill.append("=============================================\n");

        if (laptop.isSelected()) { bill.append(String.format("%-25s %10s\n", "Laptop", "₹60,000")); total += 60000; }
        if (phone.isSelected()) { bill.append(String.format("%-25s %10s\n", "Smartphone", "₹25,000")); total += 25000; }
        if (headphones.isSelected()) { bill.append(String.format("%-25s %10s\n", "Headphones", "₹2,000")); total += 2000; }
        if (tablet.isSelected()) { bill.append(String.format("%-25s %10s\n", "Tablet", "₹18,000")); total += 18000; }
        if (smartwatch.isSelected()) { bill.append(String.format("%-25s %10s\n", "Smartwatch", "₹5,000")); total += 5000; }
        if (speaker.isSelected()) { bill.append(String.format("%-25s %10s\n", "Bluetooth Speaker", "₹3,500")); total += 3500; }
        if (camera.isSelected()) { bill.append(String.format("%-25s %10s\n", "Digital Camera", "₹15,000")); total += 15000; }
        if (charger.isSelected()) { bill.append(String.format("%-25s %10s\n", "Fast Charger", "₹1,200")); total += 1200; }
        if (mouse.isSelected()) { bill.append(String.format("%-25s %10s\n", "Wireless Mouse", "₹800")); total += 800; }
        if (keyboard.isSelected()) { bill.append(String.format("%-25s %10s\n", "Mechanical Keyboard", "₹2,500")); total += 2500; }

        bill.append("---------------------------------------------\n");
        bill.append(String.format("%-25s %10s\n", "Total", "₹" + total));
        bill.append("=============================================\n");
        bill.append("Thank you for shopping with us!\n");

        billArea.setText(bill.toString());
    }

    public static void main(String[] args) {
        new ElectronicStoreBill();
    }
}
