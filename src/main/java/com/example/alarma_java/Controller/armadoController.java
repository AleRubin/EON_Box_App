package com.example.alarma_java.Controller;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class armadoController {

    @FXML
    private Label timeLabel;

    @FXML
    private Label ampmLabel;

    private SimpleDateFormat timeFormat = new SimpleDateFormat("hh:mm a");

    // Método para inicializar el reloj
    @FXML
    private void initialize() {
        updateClock();
        // Configura un temporizador para actualizar el reloj cada minuto
        javafx.animation.Timeline clock = new javafx.animation.Timeline(new javafx.animation.KeyFrame(javafx.util.Duration.seconds(60), e -> updateClock()));
        clock.setCycleCount(javafx.animation.Animation.INDEFINITE);
        clock.play();
    }

    private void updateClock() {
        Calendar now = Calendar.getInstance();
        timeLabel.setText(timeFormat.format(now.getTime()).split(" ")[0]);
        ampmLabel.setText(timeFormat.format(now.getTime()).split(" ")[1]);
    }
}
