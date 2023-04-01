#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMaplineinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMaplineinfoQueryResponse, self).__init__()
        self._line_map = None

    @property
    def line_map(self):
        return self._line_map

    @line_map.setter
    def line_map(self, value):
        self._line_map = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMaplineinfoQueryResponse, self).parse_response_content(response_content)
        if 'line_map' in response:
            self.line_map = response['line_map']
