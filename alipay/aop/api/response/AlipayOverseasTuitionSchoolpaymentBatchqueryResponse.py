#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionInremitOrder import TuitionInremitOrder
from alipay.aop.api.domain.SchoolBatchQueryResult import SchoolBatchQueryResult


class AlipayOverseasTuitionSchoolpaymentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasTuitionSchoolpaymentBatchqueryResponse, self).__init__()
        self._isv_pid = None
        self._pass_through_info = None
        self._payment_order_count = None
        self._payment_orders = None
        self._result = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def payment_order_count(self):
        return self._payment_order_count

    @payment_order_count.setter
    def payment_order_count(self, value):
        self._payment_order_count = value
    @property
    def payment_orders(self):
        return self._payment_orders

    @payment_orders.setter
    def payment_orders(self, value):
        if isinstance(value, list):
            self._payment_orders = list()
            for i in value:
                if isinstance(i, TuitionInremitOrder):
                    self._payment_orders.append(i)
                else:
                    self._payment_orders.append(TuitionInremitOrder.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, SchoolBatchQueryResult):
            self._result = value
        else:
            self._result = SchoolBatchQueryResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasTuitionSchoolpaymentBatchqueryResponse, self).parse_response_content(response_content)
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'payment_order_count' in response:
            self.payment_order_count = response['payment_order_count']
        if 'payment_orders' in response:
            self.payment_orders = response['payment_orders']
        if 'result' in response:
            self.result = response['result']
