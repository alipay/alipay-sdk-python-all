#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsserviceprodSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsserviceprodSyncResponse, self).__init__()
        self._node_desc = None
        self._node_name = None

    @property
    def node_desc(self):
        return self._node_desc

    @node_desc.setter
    def node_desc(self, value):
        self._node_desc = value
    @property
    def node_name(self):
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        self._node_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsserviceprodSyncResponse, self).parse_response_content(response_content)
        if 'node_desc' in response:
            self.node_desc = response['node_desc']
        if 'node_name' in response:
            self.node_name = response['node_name']
