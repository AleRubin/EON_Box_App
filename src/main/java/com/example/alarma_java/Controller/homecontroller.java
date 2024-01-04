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

public class homecontroller {
    @FXML
    private void gotoArmadoDesarmado(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.setWidth(800);
        stage.setHeight(500);

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("armado_desarmado.fxml")));
            Scene scene = new Scene(root,800,500);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    private void gotoAlertas(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();

        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("alertas.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    private void gotoMonitor(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.setMinWidth(1200);
        stage.setMinHeight(600);
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("monitor.fxml")));
            Scene scene = new Scene(root,1200,600);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    private void gotoSOS(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("alerta-sos.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Pantalla de Inicio");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }
    @FXML
    private void gotoConfiguracion(ActionEvent event){
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.setWidth(800);
        stage.setHeight(500);


        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("configuracionsistema.fxml")));
            Scene scene = new Scene(root,800,500);
            stage.setTitle("Pantalla de Inicio");
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
