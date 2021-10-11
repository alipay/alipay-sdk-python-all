#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountFundallocCountQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountFundallocCountQueryResponse, self).__init__()
        self._alloc_amount = None
        self._alloc_times = None

    @property
    def alloc_amount(self):
        return self._alloc_amount

    @alloc_amount.setter
    def alloc_amount(self, value):
        self._alloc_amount = value
    @property
    def alloc_times(self):
        return self._alloc_times

    @alloc_times.setter
    def alloc_times(self, value):
        self._alloc_times = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountFundallocCountQueryResponse, self).parse_response_content(response_content)
        if 'alloc_amount' in response:
            self.alloc_amount = response['alloc_amount']
        if 'alloc_times' in response:
            self.alloc_times = response['alloc_times']
