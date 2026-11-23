#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCareerOpenbaseEsignConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerOpenbaseEsignConsultResponse, self).__init__()
        self._check_passed = None
        self._order_no = None
        self._out_biz_no = None
        self._reason_code = None

    @property
    def check_passed(self):
        return self._check_passed

    @check_passed.setter
    def check_passed(self, value):
        self._check_passed = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerOpenbaseEsignConsultResponse, self).parse_response_content(response_content)
        if 'check_passed' in response:
            self.check_passed = response['check_passed']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
