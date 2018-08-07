# File content is auto-generated. Do not modify.
# pylint: skip-file
from ._internal import SymbolBase
from ..base import _Null

def CTCLoss(data=None, label=None, data_lengths=None, label_lengths=None, use_data_lengths=_Null, use_label_lengths=_Null, blank_label=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Connectionist Temporal Classification Loss.

    The shapes of the inputs and outputs:

    - **data**: `(sequence_length, batch_size, alphabet_size)`
    - **label**: `(batch_size, label_sequence_length)`
    - **out**: `(batch_size)`

    The `data` tensor consists of sequences of activation vectors (without applying softmax),
    with i-th channel in the last dimension corresponding to i-th label
    for i between 0 and alphabet_size-1 (i.e always 0-indexed).
    Alphabet size should include one additional value reserved for blank label.
    When `blank_label` is ``"first"``, the ``0``-th channel is be reserved for
    activation of blank label, or otherwise if it is "last", ``(alphabet_size-1)``-th channel should be
    reserved for blank label.

    ``label`` is an index matrix of integers. When `blank_label` is ``"first"``,
    the value 0 is then reserved for blank label, and should not be passed in this matrix. Otherwise,
    when `blank_label` is ``"last"``, the value `(alphabet_size-1)` is reserved for blank label.

    If a sequence of labels is shorter than *label_sequence_length*, use the special
    padding value at the end of the sequence to conform it to the correct
    length. The padding value is `0` when `blank_label` is ``"first"``, and `-1` otherwise.

    For example, suppose the vocabulary is `[a, b, c]`, and in one batch we have three sequences
    'ba', 'cbb', and 'abac'. When `blank_label` is ``"first"``, we can index the labels as
    `{'a': 1, 'b': 2, 'c': 3}`, and we reserve the 0-th channel for blank label in data tensor.
    The resulting `label` tensor should be padded to be::

      [[2, 1, 0, 0], [3, 2, 2, 0], [1, 2, 1, 3]]

    When `blank_label` is ``"last"``, we can index the labels as
    `{'a': 0, 'b': 1, 'c': 2}`, and we reserve the channel index 3 for blank label in data tensor.
    The resulting `label` tensor should be padded to be::

      [[1, 0, -1, -1], [2, 1, 1, -1], [0, 1, 0, 2]]

    ``out`` is a list of CTC loss values, one per example in the batch.

    See *Connectionist Temporal Classification: Labelling Unsegmented
    Sequence Data with Recurrent Neural Networks*, A. Graves *et al*. for more
    information on the definition and the algorithm.



    Defined in src/operator/contrib/ctc_loss.cc:L114

    Parameters
    ----------
    data : Symbol
        Input data to the ctc_loss op.
    label : Symbol
        Ground-truth labels for the loss.
    data_lengths : Symbol
        Lengths of data for each of the samples. Only required when use_data_lengths is true.
    label_lengths : Symbol
        Lengths of labels for each of the samples. Only required when use_label_lengths is true.
    use_data_lengths : boolean, optional, default=0
        Whether the data lenghts are decided by `data_lengths`. If false, the lengths are equal to the max sequence length.
    use_label_lengths : boolean, optional, default=0
        Whether the label lenghts are decided by `label_lengths`, or derived from `padding_mask`. If false, the lengths are derived from the first occurrence of the value of `padding_mask`. The value of `padding_mask` is ``0`` when first CTC label is reserved for blank, and ``-1`` when last label is reserved for blank. See `blank_label`.
    blank_label : {'first', 'last'},optional, default='first'
        Set the label that is reserved for blank label.If "first", 0-th label is reserved, and label values for tokens in the vocabulary are between ``1`` and ``alphabet_size-1``, and the padding mask is ``-1``. If "last", last label value ``alphabet_size-1`` is reserved for blank label instead, and label values for tokens in the vocabulary are between ``0`` and ``alphabet_size-2``, and the padding mask is ``0``.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def DeformableConvolution(data=None, offset=None, weight=None, bias=None, kernel=_Null, stride=_Null, dilate=_Null, pad=_Null, num_filter=_Null, num_group=_Null, num_deformable_group=_Null, workspace=_Null, no_bias=_Null, layout=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Compute 2-D deformable convolution on 4-D input.

    The deformable convolution operation is described in https://arxiv.org/abs/1703.06211

    For 2-D deformable convolution, the shapes are

    - **data**: *(batch_size, channel, height, width)*
    - **offset**: *(batch_size, num_deformable_group * kernel[0] * kernel[1], height, width)*
    - **weight**: *(num_filter, channel, kernel[0], kernel[1])*
    - **bias**: *(num_filter,)*
    - **out**: *(batch_size, num_filter, out_height, out_width)*.

    Define::

      f(x,k,p,s,d) = floor((x+2*p-d*(k-1)-1)/s)+1

    then we have::

      out_height=f(height, kernel[0], pad[0], stride[0], dilate[0])
      out_width=f(width, kernel[1], pad[1], stride[1], dilate[1])

    If ``no_bias`` is set to be true, then the ``bias`` term is ignored.

    The default data ``layout`` is *NCHW*, namely *(batch_size, channle, height,
    width)*.

    If ``num_group`` is larger than 1, denoted by *g*, then split the input ``data``
    evenly into *g* parts along the channel axis, and also evenly split ``weight``
    along the first dimension. Next compute the convolution on the *i*-th part of
    the data with the *i*-th weight part. The output is obtained by concating all
    the *g* results.

    If ``num_deformable_group`` is larger than 1, denoted by *dg*, then split the
    input ``offset`` evenly into *dg* parts along the channel axis, and also evenly
    split ``out`` evenly into *dg* parts along the channel axis. Next compute the
    deformable convolution, apply the *i*-th part of the offset part on the *i*-th
    out.


    Both ``weight`` and ``bias`` are learnable parameters.




    Defined in src/operator/contrib/deformable_convolution.cc:L100

    Parameters
    ----------
    data : Symbol
        Input data to the DeformableConvolutionOp.
    offset : Symbol
        Input offset to the DeformableConvolutionOp.
    weight : Symbol
        Weight matrix.
    bias : Symbol
        Bias parameter.
    kernel : Shape(tuple), required
        convolution kernel size: (h, w) or (d, h, w)
    stride : Shape(tuple), optional, default=()
        convolution stride: (h, w) or (d, h, w)
    dilate : Shape(tuple), optional, default=()
        convolution dilate: (h, w) or (d, h, w)
    pad : Shape(tuple), optional, default=()
        pad for convolution: (h, w) or (d, h, w)
    num_filter : int (non-negative), required
        convolution filter(channel) number
    num_group : int (non-negative), optional, default=1
        Number of group partitions.
    num_deformable_group : int (non-negative), optional, default=1
        Number of deformable group partitions.
    workspace : long (non-negative), optional, default=1024
        Maximum temperal workspace allowed for convolution (MB).
    no_bias : boolean, optional, default=0
        Whether to disable bias parameter.
    layout : {None, 'NCDHW', 'NCHW', 'NCW'},optional, default='None'
        Set layout for input, output and weight. Empty for
        default layout: NCW for 1d, NCHW for 2d and NCDHW for 3d.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def DeformablePSROIPooling(data=None, rois=None, trans=None, spatial_scale=_Null, output_dim=_Null, group_size=_Null, pooled_size=_Null, part_size=_Null, sample_per_part=_Null, trans_std=_Null, no_trans=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Performs deformable position-sensitive region-of-interest pooling on inputs.
    The DeformablePSROIPooling operation is described in https://arxiv.org/abs/1703.06211 .batch_size will change to the number of region bounding boxes after DeformablePSROIPooling

    Parameters
    ----------
    data : Symbol
        Input data to the pooling operator, a 4D Feature maps
    rois : Symbol
        Bounding box coordinates, a 2D array of [[batch_index, x1, y1, x2, y2]]. (x1, y1) and (x2, y2) are top left and down right corners of designated region of interest. batch_index indicates the index of corresponding image in the input data
    trans : Symbol
        transition parameter
    spatial_scale : float, required
        Ratio of input feature map height (or w) to raw image height (or w). Equals the reciprocal of total stride in convolutional layers
    output_dim : int, required
        fix output dim
    group_size : int, required
        fix group size
    pooled_size : int, required
        fix pooled size
    part_size : int, optional, default='0'
        fix part size
    sample_per_part : int, optional, default='1'
        fix samples per part
    trans_std : float, optional, default=0
        fix transition std
    no_trans : boolean, optional, default=0
        Whether to disable trans parameter.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def MultiBoxDetection(cls_prob=None, loc_pred=None, anchor=None, clip=_Null, threshold=_Null, background_id=_Null, nms_threshold=_Null, force_suppress=_Null, variances=_Null, nms_topk=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Convert multibox detection predictions.

    Parameters
    ----------
    cls_prob : Symbol
        Class probabilities.
    loc_pred : Symbol
        Location regression predictions.
    anchor : Symbol
        Multibox prior anchor boxes
    clip : boolean, optional, default=1
        Clip out-of-boundary boxes.
    threshold : float, optional, default=0.01
        Threshold to be a positive prediction.
    background_id : int, optional, default='0'
        Background id.
    nms_threshold : float, optional, default=0.5
        Non-maximum suppression threshold.
    force_suppress : boolean, optional, default=0
        Suppress all detections regardless of class_id.
    variances : , optional, default=(0.1,0.1,0.2,0.2)
        Variances to be decoded from box regression output.
    nms_topk : int, optional, default='-1'
        Keep maximum top k detections before nms, -1 for no limit.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def MultiBoxPrior(data=None, sizes=_Null, ratios=_Null, clip=_Null, steps=_Null, offsets=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Generate prior(anchor) boxes from data, sizes and ratios.

    Parameters
    ----------
    data : Symbol
        Input data.
    sizes : , optional, default=(1,)
        List of sizes of generated MultiBoxPriores.
    ratios : , optional, default=(1,)
        List of aspect ratios of generated MultiBoxPriores.
    clip : boolean, optional, default=0
        Whether to clip out-of-boundary boxes.
    steps : , optional, default=(-1,-1)
        Priorbox step across y and x, -1 for auto calculation.
    offsets : , optional, default=(0.5,0.5)
        Priorbox center offsets, y and x respectively

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def MultiBoxTarget(anchor=None, label=None, cls_pred=None, overlap_threshold=_Null, ignore_label=_Null, negative_mining_ratio=_Null, negative_mining_thresh=_Null, minimum_negative_samples=_Null, variances=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Compute Multibox training targets

    Parameters
    ----------
    anchor : Symbol
        Generated anchor boxes.
    label : Symbol
        Object detection labels.
    cls_pred : Symbol
        Class predictions.
    overlap_threshold : float, optional, default=0.5
        Anchor-GT overlap threshold to be regarded as a positive match.
    ignore_label : float, optional, default=-1
        Label for ignored anchors.
    negative_mining_ratio : float, optional, default=-1
        Max negative to positive samples ratio, use -1 to disable mining
    negative_mining_thresh : float, optional, default=0.5
        Threshold used for negative mining.
    minimum_negative_samples : int, optional, default='0'
        Minimum number of negative samples.
    variances : , optional, default=(0.1,0.1,0.2,0.2)
        Variances to be encoded in box regression target.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def MultiProposal(cls_score=None, bbox_pred=None, im_info=None, rpn_pre_nms_top_n=_Null, rpn_post_nms_top_n=_Null, threshold=_Null, rpn_min_size=_Null, scales=_Null, ratios=_Null, feature_stride=_Null, output_score=_Null, iou_loss=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Generate region proposals via RPN

    Parameters
    ----------
    cls_score : Symbol
        Score of how likely proposal is object.
    bbox_pred : Symbol
        BBox Predicted deltas from anchors for proposals
    im_info : Symbol
        Image size and scale.
    rpn_pre_nms_top_n : int, optional, default='6000'
        Number of top scoring boxes to keep after applying NMS to RPN proposals
    rpn_post_nms_top_n : int, optional, default='300'
        Overlap threshold used for non-maximumsuppresion(suppress boxes with IoU >= this threshold
    threshold : float, optional, default=0.7
        NMS value, below which to suppress.
    rpn_min_size : int, optional, default='16'
        Minimum height or width in proposal
    scales : , optional, default=(4,8,16,32)
        Used to generate anchor windows by enumerating scales
    ratios : , optional, default=(0.5,1,2)
        Used to generate anchor windows by enumerating ratios
    feature_stride : int, optional, default='16'
        The size of the receptive field each unit in the convolution layer of the rpn,for example the product of all stride's prior to this layer.
    output_score : boolean, optional, default=0
        Add score to outputs
    iou_loss : boolean, optional, default=0
        Usage of IoU Loss

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def PSROIPooling(data=None, rois=None, spatial_scale=_Null, output_dim=_Null, pooled_size=_Null, group_size=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Performs region-of-interest pooling on inputs. Resize bounding box coordinates by spatial_scale and crop input feature maps accordingly. The cropped feature maps are pooled by max pooling to a fixed size output indicated by pooled_size. batch_size will change to the number of region bounding boxes after PSROIPooling

    Parameters
    ----------
    data : Symbol
        Input data to the pooling operator, a 4D Feature maps
    rois : Symbol
        Bounding box coordinates, a 2D array of [[batch_index, x1, y1, x2, y2]]. (x1, y1) and (x2, y2) are top left and down right corners of designated region of interest. batch_index indicates the index of corresponding image in the input data
    spatial_scale : float, required
        Ratio of input feature map height (or w) to raw image height (or w). Equals the reciprocal of total stride in convolutional layers
    output_dim : int, required
        fix output dim
    pooled_size : int, required
        fix pooled size
    group_size : int, optional, default='0'
        fix group size

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def Proposal(cls_score=None, bbox_pred=None, im_info=None, rpn_pre_nms_top_n=_Null, rpn_post_nms_top_n=_Null, threshold=_Null, rpn_min_size=_Null, scales=_Null, ratios=_Null, feature_stride=_Null, output_score=_Null, iou_loss=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Generate region proposals via RPN

    Parameters
    ----------
    cls_score : Symbol
        Score of how likely proposal is object.
    bbox_pred : Symbol
        BBox Predicted deltas from anchors for proposals
    im_info : Symbol
        Image size and scale.
    rpn_pre_nms_top_n : int, optional, default='6000'
        Number of top scoring boxes to keep after applying NMS to RPN proposals
    rpn_post_nms_top_n : int, optional, default='300'
        Overlap threshold used for non-maximumsuppresion(suppress boxes with IoU >= this threshold
    threshold : float, optional, default=0.7
        NMS value, below which to suppress.
    rpn_min_size : int, optional, default='16'
        Minimum height or width in proposal
    scales : , optional, default=(4,8,16,32)
        Used to generate anchor windows by enumerating scales
    ratios : , optional, default=(0.5,1,2)
        Used to generate anchor windows by enumerating ratios
    feature_stride : int, optional, default='16'
        The size of the receptive field each unit in the convolution layer of the rpn,for example the product of all stride's prior to this layer.
    output_score : boolean, optional, default=0
        Add score to outputs
    iou_loss : boolean, optional, default=0
        Usage of IoU Loss

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def count_sketch(data=None, h=None, s=None, out_dim=_Null, processing_batch_size=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Apply CountSketch to input: map a d-dimension data to k-dimension data"

    .. note:: `count_sketch` is only available on GPU.

    Assume input data has shape (N, d), sign hash table s has shape (N, d),
    index hash table h has shape (N, d) and mapping dimension out_dim = k,
    each element in s is either +1 or -1, each element in h is random integer from 0 to k-1.
    Then the operator computs:

    .. math::
       out[h[i]] += data[i] * s[i]

    Example::

       out_dim = 5
       x = [[1.2, 2.5, 3.4],[3.2, 5.7, 6.6]]
       h = [[0, 3, 4]]
       s = [[1, -1, 1]]
       mx.contrib.ndarray.count_sketch(data=x, h=h, s=s, out_dim = 5) = [[1.2, 0, 0, -2.5, 3.4],
                                                                         [3.2, 0, 0, -5.7, 6.6]]



    Defined in src/operator/contrib/count_sketch.cc:L66

    Parameters
    ----------
    data : Symbol
        Input data to the CountSketchOp.
    h : Symbol
        The index vector
    s : Symbol
        The sign vector
    out_dim : int, required
        The output dimension.
    processing_batch_size : int, optional, default='32'
        How many sketch vectors to process at one time.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def ctc_loss(data=None, label=None, data_lengths=None, label_lengths=None, use_data_lengths=_Null, use_label_lengths=_Null, blank_label=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Connectionist Temporal Classification Loss.

    The shapes of the inputs and outputs:

    - **data**: `(sequence_length, batch_size, alphabet_size)`
    - **label**: `(batch_size, label_sequence_length)`
    - **out**: `(batch_size)`

    The `data` tensor consists of sequences of activation vectors (without applying softmax),
    with i-th channel in the last dimension corresponding to i-th label
    for i between 0 and alphabet_size-1 (i.e always 0-indexed).
    Alphabet size should include one additional value reserved for blank label.
    When `blank_label` is ``"first"``, the ``0``-th channel is be reserved for
    activation of blank label, or otherwise if it is "last", ``(alphabet_size-1)``-th channel should be
    reserved for blank label.

    ``label`` is an index matrix of integers. When `blank_label` is ``"first"``,
    the value 0 is then reserved for blank label, and should not be passed in this matrix. Otherwise,
    when `blank_label` is ``"last"``, the value `(alphabet_size-1)` is reserved for blank label.

    If a sequence of labels is shorter than *label_sequence_length*, use the special
    padding value at the end of the sequence to conform it to the correct
    length. The padding value is `0` when `blank_label` is ``"first"``, and `-1` otherwise.

    For example, suppose the vocabulary is `[a, b, c]`, and in one batch we have three sequences
    'ba', 'cbb', and 'abac'. When `blank_label` is ``"first"``, we can index the labels as
    `{'a': 1, 'b': 2, 'c': 3}`, and we reserve the 0-th channel for blank label in data tensor.
    The resulting `label` tensor should be padded to be::

      [[2, 1, 0, 0], [3, 2, 2, 0], [1, 2, 1, 3]]

    When `blank_label` is ``"last"``, we can index the labels as
    `{'a': 0, 'b': 1, 'c': 2}`, and we reserve the channel index 3 for blank label in data tensor.
    The resulting `label` tensor should be padded to be::

      [[1, 0, -1, -1], [2, 1, 1, -1], [0, 1, 0, 2]]

    ``out`` is a list of CTC loss values, one per example in the batch.

    See *Connectionist Temporal Classification: Labelling Unsegmented
    Sequence Data with Recurrent Neural Networks*, A. Graves *et al*. for more
    information on the definition and the algorithm.



    Defined in src/operator/contrib/ctc_loss.cc:L114

    Parameters
    ----------
    data : Symbol
        Input data to the ctc_loss op.
    label : Symbol
        Ground-truth labels for the loss.
    data_lengths : Symbol
        Lengths of data for each of the samples. Only required when use_data_lengths is true.
    label_lengths : Symbol
        Lengths of labels for each of the samples. Only required when use_label_lengths is true.
    use_data_lengths : boolean, optional, default=0
        Whether the data lenghts are decided by `data_lengths`. If false, the lengths are equal to the max sequence length.
    use_label_lengths : boolean, optional, default=0
        Whether the label lenghts are decided by `label_lengths`, or derived from `padding_mask`. If false, the lengths are derived from the first occurrence of the value of `padding_mask`. The value of `padding_mask` is ``0`` when first CTC label is reserved for blank, and ``-1`` when last label is reserved for blank. See `blank_label`.
    blank_label : {'first', 'last'},optional, default='first'
        Set the label that is reserved for blank label.If "first", 0-th label is reserved, and label values for tokens in the vocabulary are between ``1`` and ``alphabet_size-1``, and the padding mask is ``-1``. If "last", last label value ``alphabet_size-1`` is reserved for blank label instead, and label values for tokens in the vocabulary are between ``0`` and ``alphabet_size-2``, and the padding mask is ``0``.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def dequantize(input=None, min_range=None, max_range=None, out_type=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Dequantize the input tensor into a float tensor.
    [min_range, max_range] are scalar floats that spcify the range for
    the output data.

    Each value of the tensor will undergo the following:

    `out[i] = min_range + (in[i] * (max_range - min_range) / range(INPUT_TYPE))`

    here `range(T) = numeric_limits<T>::max() - numeric_limits<T>::min()`


    Defined in src/operator/contrib/dequantize.cc:L40

    Parameters
    ----------
    input : Symbol
        A ndarray/symbol of type `uint8`
    min_range : Symbol
        The minimum scalar value possibly produced for the input
    max_range : Symbol
        The maximum scalar value possibly produced for the input
    out_type : {'float32'}, required
        Output data type.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def fft(data=None, compute_size=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Apply 1D FFT to input"

    .. note:: `fft` is only available on GPU.

    Currently accept 2 input data shapes: (N, d) or (N1, N2, N3, d), data can only be real numbers.
    The output data has shape: (N, 2*d) or (N1, N2, N3, 2*d). The format is: [real0, imag0, real1, imag1, ...].

    Example::

       data = np.random.normal(0,1,(3,4))
       out = mx.contrib.ndarray.fft(data = mx.nd.array(data,ctx = mx.gpu(0)))



    Defined in src/operator/contrib/fft.cc:L55

    Parameters
    ----------
    data : Symbol
        Input data to the FFTOp.
    compute_size : int, optional, default='128'
        Maximum size of sub-batch to be forwarded at one time

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def ifft(data=None, compute_size=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Apply 1D ifft to input"

    .. note:: `ifft` is only available on GPU.

    Currently accept 2 input data shapes: (N, d) or (N1, N2, N3, d). Data is in format: [real0, imag0, real1, imag1, ...].
    Last dimension must be an even number.
    The output data has shape: (N, d/2) or (N1, N2, N3, d/2). It is only the real part of the result.

    Example::

       data = np.random.normal(0,1,(3,4))
       out = mx.contrib.ndarray.ifft(data = mx.nd.array(data,ctx = mx.gpu(0)))



    Defined in src/operator/contrib/ifft.cc:L57

    Parameters
    ----------
    data : Symbol
        Input data to the IFFTOp.
    compute_size : int, optional, default='128'
        Maximum size of sub-batch to be forwarded at one time

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def quantize(input=None, min_range=None, max_range=None, out_type=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Quantize a input tensor from float to `out_type`,
    with user-specified `min_range` and `max_range`.

    [min_range, max_range] are scalar floats that spcify the range for
    the input data. Each value of the tensor will undergo the following:

    `out[i] = (in[i] - min_range) * range(OUTPUT_TYPE) / (max_range - min_range)`

    here `range(T) = numeric_limits<T>::max() - numeric_limits<T>::min()`


    Defined in src/operator/contrib/quantize.cc:L40

    Parameters
    ----------
    input : Symbol
        A ndarray/symbol of type `float32`
    min_range : Symbol
        The minimum scalar value possibly produced for the input
    max_range : Symbol
        The maximum scalar value possibly produced for the input
    out_type : {'uint8'},optional, default='uint8'
        Output data type.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

__all__ = ['CTCLoss', 'DeformableConvolution', 'DeformablePSROIPooling', 'MultiBoxDetection', 'MultiBoxPrior', 'MultiBoxTarget', 'MultiProposal', 'PSROIPooling', 'Proposal', 'count_sketch', 'ctc_loss', 'dequantize', 'fft', 'ifft', 'quantize']