#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataMdaMaptorchrouteQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataMdaMaptorchrouteQueryResponse, self).__init__()
        self._torch_path = None

    @property
    def torch_path(self):
        return self._torch_path

    @torch_path.setter
    def torch_path(self, value):
        self._torch_path = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataMdaMaptorchrouteQueryResponse, self).parse_response_content(response_content)
        if 'torch_path' in response:
            self.torch_path = response['torch_path']
