#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdNopidBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdNopidBatchqueryResponse, self).__init__()
        self._rthreemcc = None

    @property
    def rthreemcc(self):
        return self._rthreemcc

    @rthreemcc.setter
    def rthreemcc(self, value):
        self._rthreemcc = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdNopidBatchqueryResponse, self).parse_response_content(response_content)
        if 'rthreemcc' in response:
            self.rthreemcc = response['rthreemcc']
