#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceDeductresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceDeductresultQueryResponse, self).__init__()
        self._deduct_amount = None
        self._order_no = None
        self._order_result_code = None
        self._order_result_msg = None
        self._out_order_no = None
        self._pay_time = None
        self._status = None

    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_result_code(self):
        return self._order_result_code

    @order_result_code.setter
    def order_result_code(self, value):
        self._order_result_code = value
    @property
    def order_result_msg(self):
        return self._order_result_msg

    @order_result_msg.setter
    def order_result_msg(self, value):
        self._order_result_msg = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceDeductresultQueryResponse, self).parse_response_content(response_content)
        if 'deduct_amount' in response:
            self.deduct_amount = response['deduct_amount']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_result_code' in response:
            self.order_result_code = response['order_result_code']
        if 'order_result_msg' in response:
            self.order_result_msg = response['order_result_msg']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'status' in response:
            self.status = response['status']
