# 🌳 Minimum Spanning Tree (MST) Visualizer
Using Prim’s and Kruskal’s Algorithm (Django Project)
# 📌 Project Overview

This project is a Django-based web application that implements and demonstrates Minimum Spanning Tree (MST) using:

## ✅ Prim’s Algorithm

## ✅ Kruskal’s Algorithm

The system allows users to input a weighted graph and compute the MST along with the total minimum cost.

This project is built using Django (Python) without using a virtual environment.

# 🎯 Objective

To understand the concept of Minimum Spanning Tree.

To compare Prim’s and Kruskal’s algorithms.

To visualize MST generation step-by-step.

To analyze total minimum cost of spanning tree.

# 🧠 What is Minimum Spanning Tree?

A Minimum Spanning Tree (MST) is a subset of edges of a connected, weighted graph that:

Connects all vertices

Has no cycles

Has minimum possible total edge weight

# ⚙️ Algorithms Used
## 🔹 Prim’s Algorithm

Greedy approach.

Starts from any vertex.

Expands tree by selecting minimum weight edge.

Uses Priority Queue (or adjacency matrix).

## 🔹 Kruskal’s Algorithm

Greedy approach.

Sorts all edges by weight.

Selects smallest edge that does not form a cycle.

Uses Disjoint Set (Union-Find).

# 💻 Technologies Used

Python

Django

HTML

CSS

Bootstrap (optional)

JavaScript (optional)

# 🚀 Features

User input for:

Number of vertices

Edge list with weights

Compute MST using:

Prim’s Algorithm

Kruskal’s Algorithm

Displays:

Selected edges

Total cost of MST

Clean and simple UI

# 📂 Project Structure

Django Project

App for MST logic

Views for algorithm implementation

Templates for user interface

# ▶️ How to Run the Project (Without Virtual Environment)

Install Django globally:

pip install django


Navigate to project directory:

cd mst_project


Run migrations:

python manage.py migrate


Start the server:

python manage.py runserver


Open browser:

http://127.0.0.1:8000/

# 📊 Time Complexity

Prim’s Algorithm

Using Priority Queue → O(E log V)

Using Adjacency Matrix → O(V²)

Kruskal’s Algorithm

Sorting edges → O(E log E)

Union-Find operations → Nearly O(E)

# 📌 Comparison Between Prim’s and Kruskal’s

Prim’s is better for dense graphs.

Kruskal’s is better for sparse graphs.

Both produce same MST cost (for connected graph).

# 📈 Applications of MST

Network design (LAN, cable connections)

Road construction planning

Electrical wiring layout

Water pipeline systems

Minimum cost network design

# 🔮 Future Improvements

Graph visualization using matplotlib or NetworkX

Step-by-step animation

Upload graph from file

Performance comparison chart

Support for large graphs

# 🏁 Conclusion

This project demonstrates how greedy algorithms efficiently solve the Minimum Spanning Tree problem. By implementing both Prim’s and Kruskal’s algorithms in Django, users can understand algorithm behavior, compare performance, and analyze results interactively.

# 👨‍💻 Developed By

Satasiya Daksh Maheshbhai

# Sample Output :
<img width="877" height="710" alt="image" src="https://github.com/user-attachments/assets/c1205fda-1d52-42ce-903c-d12ec7f1bedc" />
<img width="8086" height="3816" alt="127 0 0 1_8000_" src="https://github.com/user-attachments/assets/70818a6b-ff2d-4d7e-9bd9-c3a9cc12bae8" />
<img width="698" height="905" alt="image" src="https://github.com/user-attachments/assets/8a6265a5-73e2-46b2-ab88-05676f1ee56b" />
