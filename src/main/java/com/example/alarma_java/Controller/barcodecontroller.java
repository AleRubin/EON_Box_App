package com.example.alarma_java.Controller;

import com.example.alarma_java.MainApp;
import com.example.alarma_java.util.WindowConfigurer;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class barcodecontroller {
    @FXML
    protected void gotologin(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("wizard-login.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Wizard");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
}
