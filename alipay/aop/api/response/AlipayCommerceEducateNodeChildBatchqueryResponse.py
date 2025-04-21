#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduNodeInfo import EduNodeInfo


class AlipayCommerceEducateNodeChildBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateNodeChildBatchqueryResponse, self).__init__()
        self._node_list = None

    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, EduNodeInfo):
                    self._node_list.append(i)
                else:
                    self._node_list.append(EduNodeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateNodeChildBatchqueryResponse, self).parse_response_content(response_content)
        if 'node_list' in response:
            self.node_list = response['node_list']
