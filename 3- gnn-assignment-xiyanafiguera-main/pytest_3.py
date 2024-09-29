import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import typing

def is_float(element: typing.Any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def execute_notebook(notebook_filename):
	with open(notebook_filename) as ff:
		nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
		
	ep = ExecutePreprocessor(timeout=600, kernel_name='python')
	nb_out = ep.preprocess(nb_in)
	return nb_out

def test_gnn():
	nb_out = execute_notebook('gnn_node_classification_assignment.ipynb')
	# load the last cell's output
	if 'outputs' in nb_out[0]['cells'][-1] and len(nb_out[0]['cells'][-1]['outputs']) > 0 and \
		is_float(nb_out[0]['cells'][-1]['outputs'][-1]['text']) == True:
		print(float(nb_out[0]['cells'][-1]['outputs'][-1]['text']))
		assert float(nb_out[0]['cells'][-1]['outputs'][-1]['text']) > 0.5
		return
	if 'outputs' in nb_out[0]['cells'][-2] and len(nb_out[0]['cells'][-2]['outputs']) > 0 and \
		is_float(nb_out[0]['cells'][-2]['outputs'][-1]['text']) == True:
		print(float(nb_out[0]['cells'][-2]['outputs'][-1]['text']))
		assert float(nb_out[0]['cells'][-2]['outputs'][-1]['text']) > 0.5
		return
	assert False, 'Wrong test cell'

if __name__ == '__main__':
	test_gnn()