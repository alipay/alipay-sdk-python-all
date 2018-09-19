#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeBatchRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchRefundResponse, self).__init__()
        self._batch_no = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchRefundResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
