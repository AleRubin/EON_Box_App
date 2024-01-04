package com.example.alarma_java.Controller;

import com.example.alarma_java.MainApp;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Accordion;
import javafx.scene.control.TitledPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class informacionController {

    @FXML
    protected void gotoHome(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.setMinHeight(600);
        stage.setMinWidth(1200);
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("home.fxml")));
            Scene scene = new Scene(root, 1200,600);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
}
