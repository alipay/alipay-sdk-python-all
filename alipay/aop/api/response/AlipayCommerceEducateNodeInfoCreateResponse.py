#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateNodeInfoCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateNodeInfoCreateResponse, self).__init__()
        self._node_id = None

    @property
    def node_id(self):
        return self._node_id

    @node_id.setter
    def node_id(self, value):
        self._node_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateNodeInfoCreateResponse, self).parse_response_content(response_content)
        if 'node_id' in response:
            self.node_id = response['node_id']
