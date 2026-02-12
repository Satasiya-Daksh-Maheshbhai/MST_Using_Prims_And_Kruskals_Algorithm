from django.shortcuts import render
import matplotlib.pyplot as plt
import networkx as nx
import base64
from io import BytesIO

def mst_view(request):
    result = None
    graph_image = None
    error_message = None
    user_input_display = None

    if request.method == "POST":
        try:
            # ---------- Parse vertices ----------
            vertices_input = request.POST.get("vertices", "")
            vertices = [v.strip() for v in vertices_input.split(',') if v.strip()]
            if not vertices:
                raise ValueError("Please enter at least one vertex.")

            # ---------- Parse edges ----------
            edges_input = request.POST.get("edges", "")
            edges_raw = edges_input.split(';')

            raw_edges = []
            for e in edges_raw:
                parts = [p.strip() for p in e.split(',')]
                if len(parts) != 3:
                    continue
                u, v, w = parts[0], parts[1], int(parts[2])
                raw_edges.append((u, v, w))

            if not raw_edges:
                raise ValueError("Please enter at least one valid edge.")

            # ---------- IMPORTANT FIX ----------
            # Remove parallel edges → keep minimum weight edge only
            edge_map = {}
            for u, v, w in raw_edges:
                key = tuple(sorted((u, v)))  # undirected
                if key not in edge_map or w < edge_map[key]:
                    edge_map[key] = w

            edges = [(u, v, w) for (u, v), w in edge_map.items()]

            user_input_display = {
                "vertices": vertices_input,
                "edges": edges_input
            }

            algo = request.POST.get("algorithm")

            # ---------- Prim's Algorithm ----------
            def prims(vertices, edges):
                graph = {v: [] for v in vertices}
                for u, v, w in edges:
                    graph[u].append((v, w))
                    graph[v].append((u, w))

                visited = set([vertices[0]])
                mst = []
                cost = 0

                while len(visited) < len(vertices):
                    min_edge = None
                    for u in visited:
                        for v, w in graph[u]:
                            if v not in visited:
                                if min_edge is None or w < min_edge[2]:
                                    min_edge = (u, v, w)

                    if min_edge is None:
                        break

                    mst.append(min_edge)
                    cost += min_edge[2]
                    visited.add(min_edge[1])

                return mst, cost

            # ---------- Kruskal's Algorithm ----------
            def kruskal(vertices, edges):
                parent = {v: v for v in vertices}

                def find(v):
                    if parent[v] != v:
                        parent[v] = find(parent[v])
                    return parent[v]

                def union(u, v):
                    parent[find(u)] = find(v)

                mst = []
                cost = 0
                edges.sort(key=lambda x: x[2])

                for u, v, w in edges:
                    if find(u) != find(v):
                        union(u, v)
                        mst.append((u, v, w))
                        cost += w

                return mst, cost

            # ---------- Run Algorithm ----------
            if algo == "prims":
                mst, cost = prims(vertices, edges)
            else:
                mst, cost = kruskal(vertices, edges)

            result = {"mst": mst, "cost": cost}

            # ---------- Draw Graph ----------
            G = nx.Graph()
            G.add_nodes_from(vertices)

            for u, v, w in edges:
                G.add_edge(u, v, weight=w)

            mst_edges = [(u, v) for u, v, _ in mst]

            pos = nx.spring_layout(G, seed=42)
            plt.figure(figsize=(6, 6))

            nx.draw(G, pos, with_labels=True,
                    node_color='skyblue',
                    node_size=1500,
                    font_size=14)

            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

            nx.draw_networkx_edges(
                G, pos,
                edgelist=mst_edges,
                edge_color='red',
                width=3
            )

            buf = BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight')
            plt.close()
            buf.seek(0)

            graph_image = base64.b64encode(buf.read()).decode('utf-8')

        except Exception as e:
            error_message = str(e)

    return render(request, "mst.html", {
        "result": result,
        "graph_image": graph_image,
        "error_message": error_message,
        "user_input": user_input_display
    })
