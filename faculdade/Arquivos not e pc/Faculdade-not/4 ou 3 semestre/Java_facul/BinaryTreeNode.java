public class BinaryTreeNode {
    int key;
    BinaryTreeNode left;
    BinaryTreeNode right;

    public BinaryTreeNode(int key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }

    public static boolean compareTreeNode(BinaryTreeNode root1, BinaryTreeNode root2) {
        // Se ambos os nós forem nulos, eles são idênticos.
        if (root1 == null && root2 == null) {
            return true;
        }

        // Se apenas um dos nós for nulo, eles não são idênticos.
        if (root1 == null || root2 == null) {
            return false;
        }

        // Verifica se os valores dos nós são iguais.
        if (root1.key != root2.key) {
            return false;
        }

        // Verifica recursivamente os nós à esquerda e à direita.
        boolean leftIdentical = compareTreeNode(root1.left, root2.left);
        boolean rightIdentical = compareTreeNode(root1.right, root2.right);

        // A árvore é idêntica somente se ambas as subárvores à esquerda e à direita forem idênticas.
        return leftIdentical && rightIdentical;
    }

    public static void main(String[] args) {
        // Exemplo de uso:
        BinaryTreeNode tree1 = new BinaryTreeNode(1);
        tree1.left = new BinaryTreeNode(2);
        tree1.right = new BinaryTreeNode(3);

        BinaryTreeNode tree2 = new BinaryTreeNode(1);
        tree2.left = new BinaryTreeNode(2);
        tree2.right = new BinaryTreeNode(3);

        boolean result = compareTreeNode(tree1, tree2);
        System.out.println("As árvores são idênticas? " + result);
    }
}
