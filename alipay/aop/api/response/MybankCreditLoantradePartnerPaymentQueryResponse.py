#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradePartnerPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePartnerPaymentQueryResponse, self).__init__()
        self._content = None
        self._finish_time = None
        self._in_apply_no = None
        self._status = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def in_apply_no(self):
        return self._in_apply_no

    @in_apply_no.setter
    def in_apply_no(self, value):
        self._in_apply_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePartnerPaymentQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'in_apply_no' in response:
            self.in_apply_no = response['in_apply_no']
        if 'status' in response:
            self.status = response['status']
