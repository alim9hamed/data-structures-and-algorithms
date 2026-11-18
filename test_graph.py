import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.g = Graph()

    # ------------------------
    # Vertex Tests
    # ------------------------

    def test_insert_vertex(self):
        self.g.insert_vertex("A")

        self.assertTrue(self.g.has_vertex("A"))
        self.assertEqual(self.g.vertex_count(), 1)

    def test_insert_duplicate_vertex(self):
        self.g.insert_vertex("A")

        with self.assertRaises(ValueError):
            self.g.insert_vertex("A")

    def test_get_vertex(self):
        self.g.insert_vertex("A")

        v = self.g.get_vertex("A")

        self.assertEqual(v.id, "A")

    def test_get_non_existing_vertex(self):
        with self.assertRaises(ValueError):
            self.g.get_vertex("A")

    # ------------------------
    # Edge Tests
    # ------------------------

    def test_insert_edge(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.g.insert_edge("A", "B")

        self.assertTrue(
            self.g.has_edge("A", "B")
        )

    def test_insert_duplicate_edge(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.g.insert_edge("A", "B")

        with self.assertRaises(ValueError):
            self.g.insert_edge("A", "B")

    def test_has_edge_false(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.assertFalse(
            self.g.has_edge("A", "B")
        )

    def test_delete_edge(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.g.insert_edge("A", "B")
        self.g.delete_edge("A", "B")

        self.assertFalse(
            self.g.has_edge("A", "B")
        )

    def test_delete_non_existing_edge(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        with self.assertRaises(ValueError):
            self.g.delete_edge("A", "B")

    # ------------------------
    # Graph Statistics
    # ------------------------

    def test_vertex_count(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")
        self.g.insert_vertex("C")

        self.assertEqual(
            self.g.vertex_count(),
            3
        )

    def test_edge_count(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")
        self.g.insert_vertex("C")

        self.g.insert_edge("A", "B")
        self.g.insert_edge("A", "C")

        self.assertEqual(
            self.g.edges_count(),
            2
        )

    # ------------------------
    # Get Vertices / Edges
    # ------------------------

    def test_get_vertices(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.assertEqual(
            self.g.get_vertices(),
            {"A", "B"}
        )

    def test_get_edges(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.g.insert_edge("A", "B")

        self.assertEqual(
            self.g.get_edges(),
            {("A", "B")}
        )

    # ------------------------
    # Delete Vertex
    # ------------------------

    def test_delete_vertex(self):
        self.g.insert_vertex("A")
        self.g.insert_vertex("B")

        self.g.insert_edge("A", "B")

        self.g.delete_vertex("B")

        self.assertFalse(
            self.g.has_vertex("B")
        )

        self.assertEqual(
            self.g.vertex_count(),
            1
        )

    def test_delete_non_existing_vertex(self):
        with self.assertRaises(ValueError):
            self.g.delete_vertex("X")


if __name__ == "__main__":
    unittest.main()