import matplotlib.pyplot as plt
import networkx as nx

sequence = [4, 1, 13, 7, 0, 2, 8, 11, 3]


def find_lis_paths(current_index, current_val, path):
    all_paths = [path]
    found_next = False
    for i in range(current_index + 1, len(sequence)):
        next_val = sequence[i]
        if next_val > current_val:
            found_next = True
            all_paths.extend(find_lis_paths(i, next_val, path + [next_val]))
    return all_paths


def build_graph(graph, parent_id, current_idx, current_val, pos, level, width):
    children = []
    for i in range(current_idx + 1, len(sequence)):
        if sequence[i] > current_val:
            children.append(i)

    if not children:
        return

    shift = width / (len(children) + 1)
    start_x = pos[parent_id][0] - (width / 2)
    
    for idx, child_idx in enumerate(children):
        val = sequence[child_idx]
        node_id = f"{child_idx}_{val}_{parent_id}"
        
        graph.add_node(node_id, label=str(val))
        graph.add_edge(parent_id, node_id)
        
        new_x = start_x + (idx + 1) * shift
        pos[node_id] = (new_x, level - 1)
        
        build_graph(graph, node_id, child_idx, val, pos, level - 1, shift/1.1)

def visualize_lis_tree():
    G = nx.DiGraph()
    pos = {}
    
    root_id = "root"
    G.add_node(root_id, label="Start")
    pos[root_id] = (0, 0)
    
    build_graph(G, root_id, -1, -1, pos, 0, width=150)
    
    plt.figure(figsize=(25, 10)) 
    
    labels = nx.get_node_attributes(G, 'label')
    
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='white', edgecolors='black')
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10)
    nx.draw_networkx_edges(G, pos, arrows=True, edge_color='gray')
    
    plt.title("Tree: Largest Monotonically Increasing Subsequence", fontsize=15)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"Urutan Bilangan: {sequence}")
    print("-" * 40)
    
    all_possible_paths = find_lis_paths(-1, -1, [])
    all_possible_paths = [p for p in all_possible_paths if len(p) > 0]
    
    if not all_possible_paths:
        print("Tidak ada increasing subsequence.")
    else:
        longest_path = max(all_possible_paths, key=len)
        max_len = len(longest_path)
        
        print(f"Panjang Subsequence Terbesar: {max_len}")
        print(f"Urutan Tersebut adalah: {longest_path}")

    print("-" * 40)
    print("Menampilkan grafik...")
    visualize_lis_tree()