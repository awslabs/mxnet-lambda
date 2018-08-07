# File content is auto-generated. Do not modify.
# pylint: skip-file
from ._internal import NDArrayBase
from ..base import _Null

def ElementWiseSum(*args, **kwargs):
    r"""Adds all input arguments element-wise.

    .. math::
       add\_n(a_1, a_2, ..., a_n) = a_1 + a_2 + ... + a_n

    ``add_n`` is potentially more efficient than calling ``add`` by `n` times.

    The storage type of ``add_n`` output depends on storage types of inputs

    - add_n(row_sparse, row_sparse, ..) = row_sparse
    - otherwise, ``add_n`` generates output with default storage



    Defined in src/operator/tensor/elemwise_sum.cc:L122

    Parameters
    ----------
    args : NDArray[]
        Positional input arguments

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def abs(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise absolute value of the input.

    Example::

       abs([-2, 0, 3]) = [2, 0, 3]

    The storage type of ``abs`` output depends upon the input storage type:

       - abs(default) = default
       - abs(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L387

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def add_n(*args, **kwargs):
    r"""Adds all input arguments element-wise.

    .. math::
       add\_n(a_1, a_2, ..., a_n) = a_1 + a_2 + ... + a_n

    ``add_n`` is potentially more efficient than calling ``add`` by `n` times.

    The storage type of ``add_n`` output depends on storage types of inputs

    - add_n(row_sparse, row_sparse, ..) = row_sparse
    - otherwise, ``add_n`` generates output with default storage



    Defined in src/operator/tensor/elemwise_sum.cc:L122

    Parameters
    ----------
    args : NDArray[]
        Positional input arguments

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arccos(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise inverse cosine of the input array.

    The input should be in range `[-1, 1]`.
    The output is in the closed interval :math:`[0, \pi]`

    .. math::
       arccos([-1, -.707, 0, .707, 1]) = [\pi, 3\pi/4, \pi/2, \pi/4, 0]

    The storage type of ``arccos`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L123

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arccosh(data=None, out=None, name=None, **kwargs):
    r"""Returns the element-wise inverse hyperbolic cosine of the input array, \
    computed element-wise.

    The storage type of ``arccosh`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L264

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arcsin(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise inverse sine of the input array.

    The input should be in the range `[-1, 1]`.
    The output is in the closed interval of [:math:`-\pi/2`, :math:`\pi/2`].

    .. math::
       arcsin([-1, -.707, 0, .707, 1]) = [-\pi/2, -\pi/4, 0, \pi/4, \pi/2]

    The storage type of ``arcsin`` output depends upon the input storage type:

       - arcsin(default) = default
       - arcsin(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L104

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arcsinh(data=None, out=None, name=None, **kwargs):
    r"""Returns the element-wise inverse hyperbolic sine of the input array, \
    computed element-wise.

    The storage type of ``arcsinh`` output depends upon the input storage type:

       - arcsinh(default) = default
       - arcsinh(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L250

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arctan(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise inverse tangent of the input array.

    The output is in the closed interval :math:`[-\pi/2, \pi/2]`

    .. math::
       arctan([-1, 0, 1]) = [-\pi/4, 0, \pi/4]

    The storage type of ``arctan`` output depends upon the input storage type:

       - arctan(default) = default
       - arctan(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L144

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def arctanh(data=None, out=None, name=None, **kwargs):
    r"""Returns the element-wise inverse hyperbolic tangent of the input array, \
    computed element-wise.

    The storage type of ``arctanh`` output depends upon the input storage type:

       - arctanh(default) = default
       - arctanh(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L281

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def cast_storage(data=None, stype=_Null, out=None, name=None, **kwargs):
    r"""Casts tensor storage type to the new type.

    When an NDArray with default storage type is cast to csr or row_sparse storage,
    the result is compact, which means:

    - for csr, zero values will not be retained
    - for row_sparse, row slices of all zeros will not be retained

    The storage type of ``cast_storage`` output depends on stype parameter:

    - cast_storage(csr, 'default') = default
    - cast_storage(row_sparse, 'default') = default
    - cast_storage(default, 'csr') = csr
    - cast_storage(default, 'row_sparse') = row_sparse

    Example::

        dense = [[ 0.,  1.,  0.],
                 [ 2.,  0.,  3.],
                 [ 0.,  0.,  0.],
                 [ 0.,  0.,  0.]]

        # cast to row_sparse storage type
        rsp = cast_storage(dense, 'row_sparse')
        rsp.indices = [0, 1]
        rsp.values = [[ 0.,  1.,  0.],
                      [ 2.,  0.,  3.]]

        # cast to csr storage type
        csr = cast_storage(dense, 'csr')
        csr.indices = [1, 0, 2]
        csr.values = [ 1.,  2.,  3.]
        csr.indptr = [0, 1, 3, 3, 3]



    Defined in src/operator/tensor/cast_storage.cc:L69

    Parameters
    ----------
    data : NDArray
        The input.
    stype : {'csr', 'default', 'row_sparse'}, required
        Output storage type.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def ceil(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise ceiling of the input.

    The ceil of the scalar x is the smallest integer i, such that i >= x.

    Example::

       ceil([-2.1, -1.9, 1.5, 1.9, 2.1]) = [-2., -1.,  2.,  2.,  3.]

    The storage type of ``ceil`` output depends upon the input storage type:

       - ceil(default) = default
       - ceil(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L464

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def cos(data=None, out=None, name=None, **kwargs):
    r"""Computes the element-wise cosine of the input array.

    The input should be in radians (:math:`2\pi` rad equals 360 degrees).

    .. math::
       cos([0, \pi/4, \pi/2]) = [1, 0.707, 0]

    The storage type of ``cos`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L63

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def cosh(data=None, out=None, name=None, **kwargs):
    r"""Returns the hyperbolic cosine  of the input array, computed element-wise.

    .. math::
       cosh(x) = 0.5\times(exp(x) + exp(-x))

    The storage type of ``cosh`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L216

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def degrees(data=None, out=None, name=None, **kwargs):
    r"""Converts each element of the input array from radians to degrees.

    .. math::
       degrees([0, \pi/2, \pi, 3\pi/2, 2\pi]) = [0, 90, 180, 270, 360]

    The storage type of ``degrees`` output depends upon the input storage type:

       - degrees(default) = default
       - degrees(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L163

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def dot(lhs=None, rhs=None, transpose_a=_Null, transpose_b=_Null, out=None, name=None, **kwargs):
    r"""Dot product of two arrays.

    ``dot``'s behavior depends on the input array dimensions:

    - 1-D arrays: inner product of vectors
    - 2-D arrays: matrix multiplication
    - N-D arrays: a sum product over the last axis of the first input and the first
      axis of the second input

      For example, given 3-D ``x`` with shape `(n,m,k)` and ``y`` with shape `(k,r,s)`, the
      result array will have shape `(n,m,r,s)`. It is computed by::

        dot(x,y)[i,j,a,b] = sum(x[i,j,:]*y[:,a,b])

      Example::

        x = reshape([0,1,2,3,4,5,6,7], shape=(2,2,2))
        y = reshape([7,6,5,4,3,2,1,0], shape=(2,2,2))
        dot(x,y)[0,0,1,1] = 0
        sum(x[0,0,:]*y[:,1,1]) = 0

    The storage type of ``dot`` output depends on storage types of inputs and transpose options:

    - dot(csr, default) = default
    - dot(csr.T, default) = row_sparse
    - dot(csr, row_sparse) = default
    - otherwise, ``dot`` generates output with default storage



    Defined in src/operator/tensor/dot.cc:L61

    Parameters
    ----------
    lhs : NDArray
        The first input
    rhs : NDArray
        The second input
    transpose_a : boolean, optional, default=0
        If true then transpose the first input before dot.
    transpose_b : boolean, optional, default=0
        If true then transpose the second input before dot.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def elemwise_add(lhs=None, rhs=None, out=None, name=None, **kwargs):
    r"""Adds arguments element-wise.

    The storage type of ``elemwise_add`` output depends on storage types of inputs

       - elemwise_add(row_sparse, row_sparse) = row_sparse
       - otherwise, ``elemwise_add`` generates output with default storage



    Parameters
    ----------
    lhs : NDArray
        first input
    rhs : NDArray
        second input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def elemwise_div(lhs=None, rhs=None, out=None, name=None, **kwargs):
    r"""Divides arguments element-wise.

    The storage type of ``elemwise_dev`` output is always dense



    Parameters
    ----------
    lhs : NDArray
        first input
    rhs : NDArray
        second input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def elemwise_mul(lhs=None, rhs=None, out=None, name=None, **kwargs):
    r"""Multiplies arguments element-wise.

    The storage type of ``elemwise_mul`` output depends on storage types of inputs

       - elemwise_mul(default, default) = default
       - elemwise_mul(row_sparse, row_sparse) = row_sparse
       - elemwise_mul(default, row_sparse) = row_sparse
       - elemwise_mul(row_sparse, default) = row_sparse
       - otherwise, ``elemwise_mul`` generates output with default storage



    Parameters
    ----------
    lhs : NDArray
        first input
    rhs : NDArray
        second input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def elemwise_sub(lhs=None, rhs=None, out=None, name=None, **kwargs):
    r"""Subtracts arguments element-wise.

    The storage type of ``elemwise_sub`` output depends on storage types of inputs

       - elemwise_sub(row_sparse, row_sparse) = row_sparse
       - otherwise, ``elemwise_add`` generates output with default storage



    Parameters
    ----------
    lhs : NDArray
        first input
    rhs : NDArray
        second input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def exp(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise exponential value of the input.

    .. math::
       exp(x) = e^x \approx 2.718^x

    Example::

       exp([0, 1, 2]) = [1., 2.71828175, 7.38905621]

    The storage type of ``exp`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L638

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def expm1(data=None, out=None, name=None, **kwargs):
    r"""Returns ``exp(x) - 1`` computed element-wise on the input.

    This function provides greater precision than ``exp(x) - 1`` for small values of ``x``.

    The storage type of ``expm1`` output depends upon the input storage type:

       - expm1(default) = default
       - expm1(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L717

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def fix(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise rounded value to the nearest \
    integer towards zero of the input.

    Example::

       fix([-2.1, -1.9, 1.9, 2.1]) = [-2., -1.,  1., 2.]

    The storage type of ``fix`` output depends upon the input storage type:

       - fix(default) = default
       - fix(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L518

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def floor(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise floor of the input.

    The floor of the scalar x is the largest integer i, such that i <= x.

    Example::

       floor([-2.1, -1.9, 1.5, 1.9, 2.1]) = [-3., -2.,  1.,  1.,  2.]

    The storage type of ``floor`` output depends upon the input storage type:

       - floor(default) = default
       - floor(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L482

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gamma(data=None, out=None, name=None, **kwargs):
    r"""Returns the gamma function (extension of the factorial function \
    to the reals), computed element-wise on the input array.

    The storage type of ``gamma`` output is always dense



    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def gammaln(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise log of the absolute value of the gamma function \
    of the input.

    The storage type of ``gammaln`` output is always dense



    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def log(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise Natural logarithmic value of the input.

    The natural logarithm is logarithm in base *e*, so that ``log(exp(x)) = x``

    The storage type of ``log`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L650

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def log10(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise Base-10 logarithmic value of the input.

    ``10**log10(x) = x``

    The storage type of ``log10`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L662

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def log1p(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise ``log(1 + x)`` value of the input.

    This function is more accurate than ``log(1 + x)``  for small ``x`` so that
    :math:`1+x\approx 1`

    The storage type of ``log1p`` output depends upon the input storage type:

       - log1p(default) = default
       - log1p(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L699

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def log2(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise Base-2 logarithmic value of the input.

    ``2**log2(x) = x``

    The storage type of ``log2`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L674

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def make_loss(data=None, out=None, name=None, **kwargs):
    r"""Make your own loss function in network construction.

    This operator accepts a customized loss function symbol as a terminal loss and
    the symbol should be an operator with no backward dependency.
    The output of this function is the gradient of loss with respect to the input data.

    For example, if you are a making a cross entropy loss function. Assume ``out`` is the
    predicted output and ``label`` is the true label, then the cross entropy can be defined as::

      cross_entropy = label * log(out) + (1 - label) * log(1 - out)
      loss = make_loss(cross_entropy)

    We will need to use ``make_loss`` when we are creating our own loss function or we want to
    combine multiple loss functions. Also we may want to stop some variables' gradients
    from backpropagation. See more detail in ``BlockGrad`` or ``stop_gradient``.

    The storage type of ``make_loss`` output depends upon the input storage type:

       - make_loss(default) = default
       - make_loss(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L201

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def negative(data=None, out=None, name=None, **kwargs):
    r"""Numerical negative of the argument, element-wise.

    The storage type of ``negative`` output depends upon the input storage type:

       - negative(default) = default
       - negative(row_sparse) = row_sparse
       - negative(csr) = csr



    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def radians(data=None, out=None, name=None, **kwargs):
    r"""Converts each element of the input array from degrees to radians.

    .. math::
       radians([0, 90, 180, 270, 360]) = [0, \pi/2, \pi, 3\pi/2, 2\pi]

    The storage type of ``radians`` output depends upon the input storage type:

       - radians(default) = default
       - radians(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L182

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def relu(data=None, out=None, name=None, **kwargs):
    r"""Computes rectified linear.

    .. math::
       max(features, 0)

    The storage type of ``relu`` output depends upon the input storage type:

       - relu(default) = default
       - relu(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L84

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def retain(data=None, indices=None, out=None, name=None, **kwargs):
    r"""pick rows specified by user input index array from a row sparse matrix
    and save them in the output sparse matrix.

    Example::

      data = [[1, 2], [3, 4], [5, 6]]
      indices = [0, 1, 3]
      shape = (4, 2)
      rsp_in = row_sparse(data, indices)
      to_retain = [0, 3]
      rsp_out = retain(rsp_in, to_retain)
      rsp_out.values = [[1, 2], [5, 6]]
      rsp_out.indices = [0, 3]

    The storage type of ``retain`` output depends on storage types of inputs

    - retain(row_sparse, default) = row_sparse
    - otherwise, ``retain`` is not supported



    Defined in src/operator/tensor/sparse_retain.cc:L53

    Parameters
    ----------
    data : NDArray
        The input array for sparse_retain operator.
    indices : NDArray
        The index array of rows ids that will be retained.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def rint(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise rounded value to the nearest integer of the input.

    .. note::
       - For input ``n.5`` ``rint`` returns ``n`` while ``round`` returns ``n+1``.
       - For input ``-n.5`` both ``rint`` and ``round`` returns ``-n-1``.

    Example::

       rint([-1.5, 1.5, -1.9, 1.9, 2.1]) = [-2.,  1., -2.,  2.,  2.]

    The storage type of ``rint`` output depends upon the input storage type:

       - rint(default) = default
       - rint(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L446

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def round(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise rounded value to the nearest integer of the input.

    Example::

       round([-1.5, 1.5, -1.9, 1.9, 2.1]) = [-2.,  2., -2.,  2.,  2.]

    The storage type of ``round`` output depends upon the input storage type:

      - round(default) = default
      - round(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L425

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def rsqrt(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise inverse square-root value of the input.

    .. math::
       rsqrt(x) = 1/\sqrt{x}

    Example::

       rsqrt([4,9,16]) = [0.5, 0.33333334, 0.25]

    The storage type of ``rsqrt`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L581

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sigmoid(data=None, out=None, name=None, **kwargs):
    r"""Computes sigmoid of x element-wise.

    .. math::
       y = 1 / (1 + exp(-x))

    The storage type of ``sigmoid`` output is always dense



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L104

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sign(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise sign of the input.

    Example::

       sign([-2, 0, 3]) = [-1, 0, 1]

    The storage type of ``sign`` output depends upon the input storage type:

       - sign(default) = default
       - sign(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L406

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sin(data=None, out=None, name=None, **kwargs):
    r"""Computes the element-wise sine of the input array.

    The input should be in radians (:math:`2\pi` rad equals 360 degrees).

    .. math::
       sin([0, \pi/4, \pi/2]) = [0, 0.707, 1]

    The storage type of ``sin`` output depends upon the input storage type:

       - sin(default) = default
       - sin(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L46

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sinh(data=None, out=None, name=None, **kwargs):
    r"""Returns the hyperbolic sine of the input array, computed element-wise.

    .. math::
       sinh(x) = 0.5\times(exp(x) - exp(-x))

    The storage type of ``sinh`` output depends upon the input storage type:

       - sinh(default) = default
       - sinh(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L201

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def slice(data=None, begin=_Null, end=_Null, out=None, name=None, **kwargs):
    r"""Slices a contiguous region of the array.

    .. note:: ``crop`` is deprecated. Use ``slice`` instead.

    This function returns a sliced continuous region of the array between the indices given
    by `begin` and `end`.

    For an input array of `n` dimensions, slice operation with ``begin=(b_0, b_1...b_n-1)`` indices
    and ``end=(e_1, e_2, ... e_n)`` indices will result in an array with the shape
    ``(e_1-b_0, ..., e_n-b_n-1)``.

    The resulting array's *k*-th dimension contains elements
    from the *k*-th dimension of the input array with the open range ``[b_k, e_k)``.

    For an input array of non-default storage type(e.g. `csr` or `row_sparse`), it only supports
    slicing on the first dimension.

    Example::

      x = [[  1.,   2.,   3.,   4.],
           [  5.,   6.,   7.,   8.],
           [  9.,  10.,  11.,  12.]]

      slice(x, begin=(0,1), end=(2,4)) = [[ 2.,  3.,  4.],
                                         [ 6.,  7.,  8.]]



    Defined in src/operator/tensor/matrix_op.cc:L278

    Parameters
    ----------
    data : NDArray
        Source input
    begin : Shape(tuple), required
        starting indices for the slice operation, supports negative indices.
    end : Shape(tuple), required
        ending indices for the slice operation, supports negative indices.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sqrt(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise square-root value of the input.

    .. math::
       \textrm{sqrt}(x) = \sqrt{x}

    Example::

       sqrt([4, 9, 16]) = [2, 3, 4]

    The storage type of ``sqrt`` output depends upon the input storage type:

       - sqrt(default) = default
       - sqrt(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L561

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def square(data=None, out=None, name=None, **kwargs):
    r"""Returns element-wise squared value of the input.

    .. math::
       square(x) = x^2

    Example::

       square([2, 3, 4]) = [4, 9, 16]

    The storage type of ``square`` output depends upon the input storage type:

       - square(default) = default
       - square(row_sparse) = row_sparse
       - square(csr) = csr



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L538

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def stop_gradient(data=None, out=None, name=None, **kwargs):
    r"""Stops gradient computation.

    Stops the accumulated gradient of the inputs from flowing through this operator
    in the backward direction. In other words, this operator prevents the contribution
    of its inputs to be taken into account for computing gradients.

    Example::

      v1 = [1, 2]
      v2 = [0, 1]
      a = Variable('a')
      b = Variable('b')
      b_stop_grad = stop_gradient(3 * b)
      loss = MakeLoss(b_stop_grad + a)

      executor = loss.simple_bind(ctx=cpu(), a=(1,2), b=(1,2))
      executor.forward(is_train=True, a=v1, b=v2)
      executor.outputs
      [ 1.  5.]

      executor.backward()
      executor.grad_arrays
      [ 0.  0.]
      [ 1.  1.]



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L168

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def sum(data=None, axis=_Null, keepdims=_Null, exclude=_Null, out=None, name=None, **kwargs):
    r"""Computes the sum of array elements over given axes.

    .. Note::

      `sum` and `sum_axis` are equivalent.
      For ndarray of csr storage type summation along axis 0 and axis 1 is supported.
      Setting keepdims or exclude to True will cause a fallback to dense operator.

    Example::

      data = [[[1,2],[2,3],[1,3]],
              [[1,4],[4,3],[5,2]],
              [[7,1],[7,2],[7,3]]]

      sum(data, axis=1)
      [[  4.   8.]
       [ 10.   9.]
       [ 21.   6.]]

      sum(data, axis=[1,2])
      [ 12.  19.  27.]

      data = [[1,2,0],
              [3,0,1],
              [4,1,0]]
 
      csr = cast_storage(data, 'csr')

      sum(csr, axis=0)
      [ 8.  2.  2.]

      sum(csr, axis=1)
      [ 3.  4.  5.]



    Defined in src/operator/tensor/broadcast_reduce_op_value.cc:L84

    Parameters
    ----------
    data : NDArray
        The input
    axis : Shape(tuple), optional, default=()
        The axis or axes along which to perform the reduction.

          The default, `axis=()`, will compute over all elements into a
          scalar array with shape `(1,)`.

          If `axis` is int, a reduction is performed on a particular axis.

          If `axis` is a tuple of ints, a reduction is performed on all the axes
          specified in the tuple.

          If `exclude` is true, reduction will be performed on the axes that are
          NOT in axis instead.

          Negative values means indexing from right to left.
    keepdims : boolean, optional, default=0
        If this is set to `True`, the reduced axes are left in the result as dimension with size one.
    exclude : boolean, optional, default=0
        Whether to perform reduction on axis that are NOT in axis instead.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def tan(data=None, out=None, name=None, **kwargs):
    r"""Computes the element-wise tangent of the input array.

    The input should be in radians (:math:`2\pi` rad equals 360 degrees).

    .. math::
       tan([0, \pi/4, \pi/2]) = [0, 1, -inf]

    The storage type of ``tan`` output depends upon the input storage type:

       - tan(default) = default
       - tan(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L83

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def tanh(data=None, out=None, name=None, **kwargs):
    r"""Returns the hyperbolic tangent of the input array, computed element-wise.

    .. math::
       tanh(x) = sinh(x) / cosh(x)

    The storage type of ``tanh`` output depends upon the input storage type:

       - tanh(default) = default
       - tanh(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_trig.cc:L234

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def trunc(data=None, out=None, name=None, **kwargs):
    r"""Return the element-wise truncated value of the input.

    The truncated value of the scalar x is the nearest integer i which is closer to
    zero than x is. In short, the fractional part of the signed number x is discarded.

    Example::

       trunc([-2.1, -1.9, 1.5, 1.9, 2.1]) = [-2., -1.,  1.,  1.,  2.]

    The storage type of ``trunc`` output depends upon the input storage type:

       - trunc(default) = default
       - trunc(row_sparse) = row_sparse



    Defined in src/operator/tensor/elemwise_unary_op_basic.cc:L501

    Parameters
    ----------
    data : NDArray
        The input array.

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

def zeros_like(data=None, out=None, name=None, **kwargs):
    r"""Return an array of zeros with the same shape and type
    as the input array.

    The storage type of ``zeros_like`` output depends on the storage type of the input

    - zeros_like(row_sparse) = row_sparse
    - zeros_like(csr) = csr
    - zeros_like(default) = default

    Examples::

      x = [[ 1.,  1.,  1.],
           [ 1.,  1.,  1.]]

      zeros_like(x) = [[ 0.,  0.,  0.],
                       [ 0.,  0.,  0.]]



    Parameters
    ----------
    data : NDArray
        The input

    out : NDArray, optional
        The output NDArray to hold the result.

    Returns
    -------
    out : NDArray or list of NDArrays
        The output of this function.
    """
    return (0,)

__all__ = ['ElementWiseSum', 'abs', 'add_n', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctanh', 'cast_storage', 'ceil', 'cos', 'cosh', 'degrees', 'dot', 'elemwise_add', 'elemwise_div', 'elemwise_mul', 'elemwise_sub', 'exp', 'expm1', 'fix', 'floor', 'gamma', 'gammaln', 'log', 'log10', 'log1p', 'log2', 'make_loss', 'negative', 'radians', 'relu', 'retain', 'rint', 'round', 'rsqrt', 'sigmoid', 'sign', 'sin', 'sinh', 'slice', 'sqrt', 'square', 'stop_gradient', 'sum', 'tan', 'tanh', 'trunc', 'zeros_like']