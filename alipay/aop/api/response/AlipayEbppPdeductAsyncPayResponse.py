#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductAsyncPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductAsyncPayResponse, self).__init__()
        self._agreement_id = None
        self._out_order_no = None
        self._result_status = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductAsyncPayResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'result_status' in response:
            self.result_status = response['result_status']
