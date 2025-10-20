import java.util.Arrays;
import java.util.Stack;

public class Python {
    public static void main(String[] args) {
        // Массив фиксированной длины
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("Элементы массива: " + Arrays.toString(arr));

        // Стек
        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Верхний элемент стека: " + stack.peek());
        stack.pop();
        System.out.println("Верхний элемент: " + stack.peek());
    }
}