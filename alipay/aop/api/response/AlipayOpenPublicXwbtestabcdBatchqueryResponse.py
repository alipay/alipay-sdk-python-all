#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicXwbtestabcdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicXwbtestabcdBatchqueryResponse, self).__init__()
        self._b = None

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicXwbtestabcdBatchqueryResponse, self).parse_response_content(response_content)
        if 'b' in response:
            self.b = response['b']
