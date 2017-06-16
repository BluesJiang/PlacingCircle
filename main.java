
public class Project3{
    public class Point{
        Point(double x, double y){
            this.x = x;
            this.y = y;
        }
        double x; 
        double y;
    }

    public class Circle{
        Point center = new Point(0,0);

    }
    public static void main(String[] args){
        Circle circle = new Circle(1.0, 1.0);
        System.out.print(circle.center.x + circle.center.y);


    }
}