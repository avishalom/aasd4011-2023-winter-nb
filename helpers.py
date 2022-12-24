import sys
import torch

def print_pytorch_version() -> None:
    """
    Prints the pyTorch version.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    print(f'pyTorch version: {torch.__version__}')

def print_python_version() -> None:
    """
    Prints the Python version.
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    print(f'Python version: {sys.version}')

def print_tensor_info(tensor: torch.Tensor, fields: list[str]=None) -> None:
    """
    Prints information about a tensor.
    Parameters
    ----------
    tensor : torch.Tensor
        The tensor to print information about.
    fields : list[str], optional
        A list of fields to print. If None, all fields are printed.
        Valid fields are: 'Tensor', 'Type', 'dtype', 'Dimension', 'Shape'
    Returns
    -------
    None
    """
    # A dictionary of available fields and the corresponding function.
    _fields = {
        'Tensor':    tensor,
        'Type':      type(tensor), 
        'dtype':     tensor.dtype, 
        'Dimension': tensor.dim(), 
        'Shape':     tuple(tensor.shape)
        }
    # type check the input
    if type(tensor) is not torch.Tensor:
        raise TypeError(f"The input must be a <class 'torch.Tensor'>. Instead it is a {type(tensor)}")
    if fields is not None:
        for field in fields:
            if field not in _fields.keys():
                raise ValueError(f"Field {field} is not a valid field. Valid fields are: {_fields.keys()}")
    # set fields to all fields if None
    if fields is None:
        fields = list(_fields.keys())
    # print the fields
    for field in fields:
        print(f'{field:<12} {_fields[field]}')
    return
