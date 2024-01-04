package com.example.alarma_java.Controller;

import com.example.alarma_java.MainApp;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;
import java.util.Objects;
import java.util.ResourceBundle;

public class HelloController implements Initializable {
    private static final double WINDOW_WIDTH = 1204.0;
    private static final double WINDOW_HEIGHT = 600.0;
    private static final double MIN_WINDOW_WIDTH = 800.0;
    private static final double MIN_WINDOW_HEIGHT = 600.0;
    @Override
    public void initialize(URL location, ResourceBundle resources) {
    }


    @FXML
    private void switchToInicioScreen(MouseEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("pantalla-inicio.fxml")));
            Scene scene = new Scene(root,800,600);

            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }

}