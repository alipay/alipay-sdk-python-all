#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementExecutionplanModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementExecutionplanModifyResponse, self).__init__()
        self._agreement_no = None
        self._deduct_time = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def deduct_time(self):
        return self._deduct_time

    @deduct_time.setter
    def deduct_time(self, value):
        self._deduct_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementExecutionplanModifyResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'deduct_time' in response:
            self.deduct_time = response['deduct_time']
