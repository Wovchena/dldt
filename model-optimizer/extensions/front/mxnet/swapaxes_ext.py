"""
 Copyright (c) 2018 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from mo.front.mxnet.extractors.utils import get_mxnet_layer_attrs
from mo.front.extractor import FrontExtractorOp
from extensions.ops.swapaxes import SwapAxes


class SwapAxesFrontExtractor(FrontExtractorOp):
    op = 'SwapAxis'
    enabled = True

    @staticmethod
    def extract(node):
        attrs = get_mxnet_layer_attrs(node.symbol_dict)
        dim1 = attrs.int("dim1", 0)
        dim2 = attrs.int("dim2", 0)

        update_attrs = {
            'dim1': dim1,
            'dim2': dim2,
        }

        # update the attributes of the node
        SwapAxes.update_node_stat(node, update_attrs)
        return __class__.enabled
