#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdDfesfDefBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdDfesfDefBatchqueryResponse, self).__init__()
        self._ded = None

    @property
    def ded(self):
        return self._ded

    @ded.setter
    def ded(self, value):
        self._ded = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdDfesfDefBatchqueryResponse, self).parse_response_content(response_content)
        if 'ded' in response:
            self.ded = response['ded']
