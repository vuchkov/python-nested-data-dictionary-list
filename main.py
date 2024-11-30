root = {
    'value': 10,
    'nodes': [{
        'value': 20,
        'nodes': [{
            'value': 30
        },{
            'value': 20,
            'nodes': [{
                'value': 25
            }]
        }]
    }]
}

def sum_root(root):
    current_sum = 0
    if 'value' in root:
        current_sum += root['value']
    if 'nodes' in root:
        for node in root['nodes']:
            current_sum += sum_root(node)
    return current_sum

print(sum_root(root))