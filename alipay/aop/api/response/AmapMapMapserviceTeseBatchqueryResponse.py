#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AmapMapMapserviceTeseBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AmapMapMapserviceTeseBatchqueryResponse, self).__init__()
        self._es = None

    @property
    def es(self):
        return self._es

    @es.setter
    def es(self, value):
        self._es = value

    def parse_response_content(self, response_content):
        response = super(AmapMapMapserviceTeseBatchqueryResponse, self).parse_response_content(response_content)
        if 'es' in response:
            self.es = response['es']
