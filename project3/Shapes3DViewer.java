import javafx.animation.Animation;
import javafx.animation.RotateTransition;
import javafx.application.Application;
import javafx.scene.*;
import javafx.scene.paint.Color;
import javafx.scene.paint.PhongMaterial;
import javafx.scene.shape.*;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;
import javafx.util.Duration;

public class Shapes3DViewer extends Application {
    @Override public void start(Stage stage) {
        Project3 project3 = new Project3();

        int CIRCLE_NUM = project3.CIRCLE_NUM;
        int PIN_NUM = project3.PIN_NUM;

        project3.PlacePin(PIN_NUM);
        project3.start(CIRCLE_NUM);

        Box bound = new Box(400,400,400);
        bound.setDrawMode(DrawMode.LINE);
        bound.setTranslateX(400);
        bound.setTranslateY(400);
        bound.setTranslateZ(400);
        bound.setMaterial(new PhongMaterial(Color.WHITE));
        PhongMaterial material = new PhongMaterial();
        PhongMaterial pin_material = new PhongMaterial();

        pin_material.setDiffuseColor(Color.RED);
        material.setDiffuseColor(Color.LIGHTGRAY);

        material.setSpecularColor(Color.rgb(30, 30, 30));

        Shape3D[] meshView = new Shape3D[CIRCLE_NUM + PIN_NUM];

        for(int i=0; i<CIRCLE_NUM ; i++) {
            meshView[i] = new Sphere(200*project3.circleList.get(i).radius);
        }


        for(int i=CIRCLE_NUM; i<CIRCLE_NUM + PIN_NUM; i++) {
            meshView[i] = new Sphere(5);
            meshView[i].setTranslateX(400+200*project3.pinList.get(i-CIRCLE_NUM).x);
            meshView[i].setTranslateY(400+200*project3.pinList.get(i-CIRCLE_NUM).y);
            meshView[i].setTranslateZ(400+200*project3.pinList.get(i-CIRCLE_NUM).z);
            meshView[i].setMaterial(pin_material);
        }

        for (int i=0; i<CIRCLE_NUM; ++i) {
            meshView[i].setMaterial(material);
            meshView[i].setTranslateX(400+200*project3.circleList.get(i).center.x);
            meshView[i].setTranslateY(400+200*project3.circleList.get(i).center.y);
            meshView[i].setTranslateZ(400+200*project3.circleList.get(i).center.z);

            //meshView[i].setDrawMode(DrawMode.FILL);
            meshView[i].setCullFace(CullFace.BACK);
        };



        PointLight pointLight = new PointLight(Color.ANTIQUEWHITE);
        pointLight.setTranslateX(800);
        pointLight.setTranslateY(-100);
        pointLight.setTranslateZ(-1000);

        Group root = new Group(meshView);
        root.getChildren().add(pointLight);
        root.getChildren().add(bound);
        Scene scene = new Scene(root, 800, 800, true);
        scene.setFill(Color.rgb(10, 10, 40));

        stage.setScene(scene);
        Camera camera = new PerspectiveCamera(false);

        camera.setTranslateX(0);
        camera.setTranslateY(0);
        camera.setTranslateZ(0);
        camera.getTransforms().addAll (
                new Rotate(-30, Rotate.Y_AXIS),
                new Rotate(-30, Rotate.X_AXIS)
        );

        scene.setCamera(camera);
        stage.show();
    }

    public static void main(String[] args) {launch(args);
    }
}  