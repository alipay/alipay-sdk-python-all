#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataZbdmLineageQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataZbdmLineageQueryResponse, self).__init__()
        self._edges = None
        self._vertices = None

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value):
        if isinstance(value, list):
            self._edges = list()
            for i in value:
                self._edges.append(i)
    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        if isinstance(value, list):
            self._vertices = list()
            for i in value:
                self._vertices.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataZbdmLineageQueryResponse, self).parse_response_content(response_content)
        if 'edges' in response:
            self.edges = response['edges']
        if 'vertices' in response:
            self.vertices = response['vertices']
