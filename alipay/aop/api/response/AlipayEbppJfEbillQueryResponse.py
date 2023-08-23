#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppJfEbillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfEbillQueryResponse, self).__init__()
        self._bill_amount = None
        self._bill_date = None
        self._bill_status = None
        self._billkey = None
        self._biz_type = None
        self._fail_code = None
        self._fail_reason = None
        self._inst_code = None
        self._sub_biz_type = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def fail_code(self):
        return self._fail_code

    @fail_code.setter
    def fail_code(self, value):
        self._fail_code = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfEbillQueryResponse, self).parse_response_content(response_content)
        if 'bill_amount' in response:
            self.bill_amount = response['bill_amount']
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'bill_status' in response:
            self.bill_status = response['bill_status']
        if 'billkey' in response:
            self.billkey = response['billkey']
        if 'biz_type' in response:
            self.biz_type = response['biz_type']
        if 'fail_code' in response:
            self.fail_code = response['fail_code']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'inst_code' in response:
            self.inst_code = response['inst_code']
        if 'sub_biz_type' in response:
            self.sub_biz_type = response['sub_biz_type']
