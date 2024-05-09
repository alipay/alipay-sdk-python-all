#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSettleBatchFinishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSettleBatchFinishResponse, self).__init__()
        self._batch_amount = None
        self._batch_currency = None
        self._batch_id = None
        self._batch_num = None
        self._batch_type = None
        self._dimension = None
        self._out_request_no = None
        self._result_code = None

    @property
    def batch_amount(self):
        return self._batch_amount

    @batch_amount.setter
    def batch_amount(self, value):
        self._batch_amount = value
    @property
    def batch_currency(self):
        return self._batch_currency

    @batch_currency.setter
    def batch_currency(self, value):
        self._batch_currency = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def batch_num(self):
        return self._batch_num

    @batch_num.setter
    def batch_num(self, value):
        self._batch_num = value
    @property
    def batch_type(self):
        return self._batch_type

    @batch_type.setter
    def batch_type(self, value):
        self._batch_type = value
    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        self._dimension = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSettleBatchFinishResponse, self).parse_response_content(response_content)
        if 'batch_amount' in response:
            self.batch_amount = response['batch_amount']
        if 'batch_currency' in response:
            self.batch_currency = response['batch_currency']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'batch_num' in response:
            self.batch_num = response['batch_num']
        if 'batch_type' in response:
            self.batch_type = response['batch_type']
        if 'dimension' in response:
            self.dimension = response['dimension']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
