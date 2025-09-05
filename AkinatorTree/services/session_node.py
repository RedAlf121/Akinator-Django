from AkinatorTree.models import Question


def save_node_to_session_storage(request,node):
    request.session['current_node_id'] = node.id
    
def get_node_from_session_storage(request):
    node_id = request.session.get('current_node_id')
    current_node = Question.objects.filter(id=node_id).first()
    return current_node