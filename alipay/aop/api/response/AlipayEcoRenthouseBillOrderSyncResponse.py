#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoRenthouseBillOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoRenthouseBillOrderSyncResponse, self).__init__()
        self._result_bill_list = None

    @property
    def result_bill_list(self):
        return self._result_bill_list

    @result_bill_list.setter
    def result_bill_list(self, value):
        if isinstance(value, list):
            self._result_bill_list = list()
            for i in value:
                self._result_bill_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayEcoRenthouseBillOrderSyncResponse, self).parse_response_content(response_content)
        if 'result_bill_list' in response:
            self.result_bill_list = response['result_bill_list']
