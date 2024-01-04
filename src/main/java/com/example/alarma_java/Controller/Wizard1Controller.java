package com.example.alarma_java.Controller;

import com.example.alarma_java.MainApp;
import com.example.alarma_java.util.WindowConfigurer;
import javafx.collections.FXCollections;
        import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.NetworkInterface;
        import java.net.SocketException;
        import java.net.URL;
import java.util.*;

public class Wizard1Controller {

    @FXML
    private ChoiceBox<String> wifiNetworksChoiceBox, wifiSecurity, banda;
    @FXML
    private TextField password;
    @FXML
    private CheckBox mostrar_password;

    //@Override
    //public void initialize(URL location, ResourceBundle resources) {
      //  populateWiFiNetworks();
    //}


    @FXML
    private void gotoConfiguracion(ActionEvent event)
    {
            Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("configuracion.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Configuracion avanzada");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }

    @FXML
    private void gotoSiguiente(ActionEvent event)
    {
        Node node = (Node) event.getSource();
        Stage stage = (Stage) node.getScene().getWindow();
        stage.close();

        try {
            Parent root = FXMLLoader.load(Objects.requireNonNull(MainApp.class.getResource("wizard-usuario.fxml")));
            Scene scene = new Scene(root,800,600);
            stage.setTitle("Configuracion de usuario");
            stage.setScene(scene);
            stage.show();
        } catch (IOException e) {
            System.err.printf("Error creando ventana: %s%n", e.getMessage());
        }
    }

    @FXML
    private void cancelar()
    {

    }
    @FXML
    protected void gotowizard(ActionEvent event){
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
    private void populateWiFiNetworks() {
        ObservableList<String> wifiNetworks = FXCollections.observableArrayList();
        List<String> networkNames = getAvailableNetworks();

        wifiNetworks.addAll(networkNames);
        wifiNetworksChoiceBox.setItems(wifiNetworks);
    }
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
    private List<String> getAvailableNetworks() {
        List<String> networkNames = new ArrayList<>();

        try {
            Enumeration<NetworkInterface> networkInterfaces = NetworkInterface.getNetworkInterfaces();
            while (networkInterfaces.hasMoreElements()) {
                NetworkInterface networkInterface = networkInterfaces.nextElement();
                if (networkInterface.isUp() && !networkInterface.isLoopback()) {
                    System.out.println(networkInterface.toString());
                    networkNames.add(networkInterface.getDisplayName());
                }
            }
        } catch (SocketException e) {
            e.printStackTrace();
        }

        return networkNames;
    }
}
