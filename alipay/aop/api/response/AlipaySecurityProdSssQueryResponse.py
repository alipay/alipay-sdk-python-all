#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdSssQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdSssQueryResponse, self).__init__()
        self._ccc = None
        self._ccc_open_id = None

    @property
    def ccc(self):
        return self._ccc

    @ccc.setter
    def ccc(self, value):
        self._ccc = value
    @property
    def ccc_open_id(self):
        return self._ccc_open_id

    @ccc_open_id.setter
    def ccc_open_id(self, value):
        self._ccc_open_id = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdSssQueryResponse, self).parse_response_content(response_content)
        if 'ccc' in response:
            self.ccc = response['ccc']
        if 'ccc_open_id' in response:
            self.ccc_open_id = response['ccc_open_id']
