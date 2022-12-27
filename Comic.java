import java.util.*;

public class Comic {
    public static void main(String[] args) {
        try 
        {
            Scanner scanner = new Scanner(System.in);
            int N = scanner.nextInt();
            int X = scanner.nextInt();
            scanner.nextLine();
            
    
            List<ComicBook> comicBooks = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                String name = scanner.nextLine();
                comicBooks.add(new ComicBook(name, 0));
            }
    
            for (int i = 0; i < N; i++) {
                int price = scanner.nextInt();
                comicBooks.get(i).price = price;
            }
            
            scanner.close();
            
            comicBooks.sort(Comparator.comparingInt((ComicBook cb) -> cb.price).thenComparing(cb -> cb.name));
            List<ComicBook> purchasedComics = new ArrayList<>();
            int sum = 0;
            for (int i = 0; i < N; i++) {
                if (sum + comicBooks.get(i).price <= X) {
                    sum += comicBooks.get(i).price;
                    purchasedComics.add(comicBooks.get(i));
                }
            }
            if (purchasedComics.size() < 2) {
                System.out.println("NONE");
                return;
            }
            if (purchasedComics.size() % 2 != 0) {
                purchasedComics.remove(purchasedComics.size() - 1);
            }
            for (ComicBook cb : purchasedComics) {
                System.out.println(cb.name + " - " + cb.price);
            } 
        } catch (Exception e) {
            System.out.println("NONE");
        }
    }
    static class ComicBook {
        String name;
        int price;
        ComicBook(String name, int price) {
            this.name = name;
            this.price = price;
        
        }
    }
}
