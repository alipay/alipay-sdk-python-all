#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductPayResponse, self).__init__()
        self._agreement_id = None
        self._bill_no = None
        self._extend_field = None
        self._out_order_no = None
        self._result_code = None
        self._result_msg = None
        self._result_status = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_msg(self):
        return self._result_msg

    @result_msg.setter
    def result_msg(self, value):
        self._result_msg = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductPayResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_msg' in response:
            self.result_msg = response['result_msg']
        if 'result_status' in response:
            self.result_status = response['result_status']
