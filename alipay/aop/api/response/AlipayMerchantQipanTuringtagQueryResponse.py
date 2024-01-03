#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrowdOperationNode import CrowdOperationNode


class AlipayMerchantQipanTuringtagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanTuringtagQueryResponse, self).__init__()
        self._node_list = None

    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, CrowdOperationNode):
                    self._node_list.append(i)
                else:
                    self._node_list.append(CrowdOperationNode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanTuringtagQueryResponse, self).parse_response_content(response_content)
        if 'node_list' in response:
            self.node_list = response['node_list']
