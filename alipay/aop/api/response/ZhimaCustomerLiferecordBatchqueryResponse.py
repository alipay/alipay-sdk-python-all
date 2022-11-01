#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromiseDetail import PromiseDetail


class ZhimaCustomerLiferecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerLiferecordBatchqueryResponse, self).__init__()
        self._promise_details = None
        self._res_code = None
        self._sub_code_number = None
        self._sub_message = None
        self._sub_success = None

    @property
    def promise_details(self):
        return self._promise_details

    @promise_details.setter
    def promise_details(self, value):
        if isinstance(value, list):
            self._promise_details = list()
            for i in value:
                if isinstance(i, PromiseDetail):
                    self._promise_details.append(i)
                else:
                    self._promise_details.append(PromiseDetail.from_alipay_dict(i))
    @property
    def res_code(self):
        return self._res_code

    @res_code.setter
    def res_code(self, value):
        self._res_code = value
    @property
    def sub_code_number(self):
        return self._sub_code_number

    @sub_code_number.setter
    def sub_code_number(self, value):
        self._sub_code_number = value
    @property
    def sub_message(self):
        return self._sub_message

    @sub_message.setter
    def sub_message(self, value):
        self._sub_message = value
    @property
    def sub_success(self):
        return self._sub_success

    @sub_success.setter
    def sub_success(self, value):
        self._sub_success = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerLiferecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'promise_details' in response:
            self.promise_details = response['promise_details']
        if 'res_code' in response:
            self.res_code = response['res_code']
        if 'sub_code_number' in response:
            self.sub_code_number = response['sub_code_number']
        if 'sub_message' in response:
            self.sub_message = response['sub_message']
        if 'sub_success' in response:
            self.sub_success = response['sub_success']
