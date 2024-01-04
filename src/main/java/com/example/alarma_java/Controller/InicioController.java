package com.example.alarma_java.Controller;

import com.example.alarma_java.MainApp;
import com.example.alarma_java.util.WindowConfigurer;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;
import java.util.Objects;
import java.util.ResourceBundle;

public class InicioController implements Initializable {
    @Override
    public void initialize(URL location, ResourceBundle resources) {}
    @FXML
    protected void onHelloButtonClick(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("wizard.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Wizard");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    protected void gotobarcode(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("wizard-barcode.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Wizard");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    protected void gotoInfo(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.setMinHeight(600);
        stage.setMinWidth(1200);
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("informacion.fxml")));
            Scene scene = new Scene(root, 1200,600);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }

}