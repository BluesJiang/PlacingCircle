/**
 * Created by yangchen on 2017/6/9.
 */
import java.util.*;
import java.math.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class Project3 {
    public double step = 0.01;
    public final int CIRCLE_NUM = 50;
    public final int PIN_NUM = 4;
    public ArrayList<Circle> circleList;
    public ArrayList<Point> centerList;
    public ArrayList<Point> pinList;
    //构造方法


    Project3() {
        circleList = new ArrayList<>();
        centerList = new ArrayList<>();
        pinList = new ArrayList<>();
        for (double x = -1; x < 1; x += step) {
            for (double y = -1; y < 1; y += step) {
                for (double z = -1; z < 1; z += step) {
                    centerList.add(new Point(x, y, z));
                }
            }
        }
    }


    public class Point {
        double x;
        double y;
        double z;

        Point(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;

        }
        Point(Point point) {
            x = point.x;
            y = point.y;
            z = point.z;
        }
    }

    public class Circle {
        Point center = new Point(0, 0, 0);
        double radius;

        Circle(Point center, double radius) {
            this.center = center;
            this.radius = radius;
        }
    }

    public class JobThread extends Thread {
        List<Point> centerList = null;
        Circle maxCircle = null;
        JobThread(List<Point> list) {
            centerList = list;
        }
        
        @Override
        public void run() {
            Point center = null;
            double maxRadius = 0;
            for (Point point: centerList) {
                double tmp = MaxValidRadius(point);
                if (maxRadius < tmp) {
                    maxRadius = tmp;
                    center = new Point(point);
                }
            }
            maxCircle = new Circle(center, maxRadius);

        }


    }


    public double distance(Circle c1, Circle c2) {

        return Math.sqrt(Math.pow(c1.center.x - c2.center.x, 2) + Math.pow(c1.center.y - c2.center.y, 2) + Math.pow(c1.center.z - c2.center.z, 2));
    }

    public double distance(Circle c, Point p) {

        return Math.sqrt(Math.pow(c.center.x - p.x, 2) + Math.pow(c.center.y - p.y, 2) + Math.pow(c.center.z - p.z, 2));
    }

    public void PlacePin(int num) {
        Random random = new Random();
        for (int i = 0; i < num; i++) {
            pinList.add(new Point(-1 + 2 * random.nextDouble(), -1 + 2 * random.nextDouble(), -1 + 2 * random.nextDouble()));
            System.out.println(pinList.get(i).x + "," + pinList.get(i).y + "," + pinList.get(i).z);
        }
    }

    public double MaxValidRadius(Point point) {//找出(x,y,z)点处的最大半径
        double x = point.x;
        double y = point.y;
        double z = point.z;
        ArrayList<Double> radiusList = new ArrayList<>();
        radiusList.add(Math.abs(x + 1));
        radiusList.add(Math.abs(x - 1));
        radiusList.add(Math.abs(y + 1));
        radiusList.add(Math.abs(y - 1));
        radiusList.add(Math.abs(z + 1));
        radiusList.add(Math.abs(z - 1));

        Point p = new Point(x, y, z);

        Circle tmp = new Circle(p, 0);

        for (Circle circle : circleList) {
            radiusList.add(distance(tmp, circle) - circle.radius);
        }


        for (Point pin : pinList) {
            Circle _pin = new Circle(pin, 0);
            radiusList.add(distance(tmp, _pin));
        }


        double max_radius = radiusList.get(0);
        for (double radius : radiusList) {
            if (radius < max_radius) {
                max_radius = radius;
            }
        }

        return max_radius;


    }

    public void PlaceCircle() {
        final int THREAD_COUNT = 4;
        double radius = 0;
        double max_radius = 0;
        Point point = new Point(0, 0, 0);
        
        ArrayList<JobThread> threads = new ArrayList<>();
        
        int len = centerList.size();
        int subLen = len/THREAD_COUNT;
        
        for (int i = 0; i < THREAD_COUNT; i++) {
            JobThread thread = new JobThread(centerList.subList(i*subLen,i*subLen+subLen >= len ? len-1 : i*subLen+subLen-1 ));
            threads.add(thread);
            thread.start();
        }

        for (JobThread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        }
        for (JobThread thread : threads) {
            if (max_radius < thread.maxCircle.radius) {
                max_radius = thread.maxCircle.radius;
                point = new Point(thread.maxCircle.center);
            }
        }

//        for (Point center : centerList) {
//            radius = MaxValidRadius(center);
//            if (radius > max_radius) {
//
//                max_radius = radius;
//                point.x = center.x;
//                point.y = center.y;
//                point.z = center.z;
//            }
//
//        }
        Circle current = new Circle(point, max_radius);
        circleList.add(current);
        ArrayList<Point> filterdlist = centerList.stream()
                .filter(p -> distance(current, p) > current.radius)
                .collect(Collectors.toCollection(ArrayList::new));
        centerList = filterdlist;
//        System.out.println("x:" + point.x);
//        System.out.println("y:" + point.y);
//        System.out.println("z:" + point.z);
//        System.out.println(max_radius);

//        for(Point center : centerList) {
//            if(distance(new Circle(center, 0), new Circle(point, 0)) < max_radius){
//                centerList.remove(center);
//            }
//        }

    }

    public void start(int num) {
        for (int i = 0; i < num; i++) {
            PlaceCircle();
            System.out.println(i);
        }
    }


}


