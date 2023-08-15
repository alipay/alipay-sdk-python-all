#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TreeNodeInfo import TreeNodeInfo


class AlipayMerchantNetworkNodeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantNetworkNodeBatchqueryResponse, self).__init__()
        self._page_num = None
        self._total_pages = None
        self._total_size = None
        self._tree_node_info_list = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, value):
        self._total_pages = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def tree_node_info_list(self):
        return self._tree_node_info_list

    @tree_node_info_list.setter
    def tree_node_info_list(self, value):
        if isinstance(value, list):
            self._tree_node_info_list = list()
            for i in value:
                if isinstance(i, TreeNodeInfo):
                    self._tree_node_info_list.append(i)
                else:
                    self._tree_node_info_list.append(TreeNodeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantNetworkNodeBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'total_pages' in response:
            self.total_pages = response['total_pages']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'tree_node_info_list' in response:
            self.tree_node_info_list = response['tree_node_info_list']
