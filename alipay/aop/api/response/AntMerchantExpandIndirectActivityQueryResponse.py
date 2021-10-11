#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityMerchantOrder import ActivityMerchantOrder


class AntMerchantExpandIndirectActivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectActivityQueryResponse, self).__init__()
        self._multi_result = None
        self._rate = None
        self._status = None

    @property
    def multi_result(self):
        return self._multi_result

    @multi_result.setter
    def multi_result(self, value):
        if isinstance(value, list):
            self._multi_result = list()
            for i in value:
                if isinstance(i, ActivityMerchantOrder):
                    self._multi_result.append(i)
                else:
                    self._multi_result.append(ActivityMerchantOrder.from_alipay_dict(i))
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectActivityQueryResponse, self).parse_response_content(response_content)
        if 'multi_result' in response:
            self.multi_result = response['multi_result']
        if 'rate' in response:
            self.rate = response['rate']
        if 'status' in response:
            self.status = response['status']
