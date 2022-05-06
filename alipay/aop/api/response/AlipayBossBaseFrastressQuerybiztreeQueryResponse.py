#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BizTreeNodeWithNoRecursive import BizTreeNodeWithNoRecursive


class AlipayBossBaseFrastressQuerybiztreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseFrastressQuerybiztreeQueryResponse, self).__init__()
        self._biz_tree_node_result = None
        self._node_id = None
        self._tnt_inst_id = None
        self._tree_id = None

    @property
    def biz_tree_node_result(self):
        return self._biz_tree_node_result

    @biz_tree_node_result.setter
    def biz_tree_node_result(self, value):
        if isinstance(value, list):
            self._biz_tree_node_result = list()
            for i in value:
                if isinstance(i, BizTreeNodeWithNoRecursive):
                    self._biz_tree_node_result.append(i)
                else:
                    self._biz_tree_node_result.append(BizTreeNodeWithNoRecursive.from_alipay_dict(i))
    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def tree_id(self):
        return self._tree_id

    @tree_id.setter
    def tree_id(self, value):
        self._tree_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseFrastressQuerybiztreeQueryResponse, self).parse_response_content(response_content)
        if 'biz_tree_node_result' in response:
            self.biz_tree_node_result = response['biz_tree_node_result']
        if 'node_id' in response:
            self.node_id = response['node_id']
        if 'tnt_inst_id' in response:
            self.tnt_inst_id = response['tnt_inst_id']
        if 'tree_id' in response:
            self.tree_id = response['tree_id']
