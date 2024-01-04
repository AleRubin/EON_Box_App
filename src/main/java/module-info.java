module com.example.alarma_java {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;

    opens com.example.alarma_java to javafx.fxml;
    exports com.example.alarma_java;
    exports com.example.alarma_java.Controller;
    opens com.example.alarma_java.Controller to javafx.fxml;
}