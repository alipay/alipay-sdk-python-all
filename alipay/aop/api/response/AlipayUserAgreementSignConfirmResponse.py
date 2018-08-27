#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementSignConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementSignConfirmResponse, self).__init__()
        self._agreement_no = None
        self._forex_eligible = None
        self._status = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def forex_eligible(self):
        return self._forex_eligible

    @forex_eligible.setter
    def forex_eligible(self, value):
        self._forex_eligible = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementSignConfirmResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'forex_eligible' in response:
            self.forex_eligible = response['forex_eligible']
        if 'status' in response:
            self.status = response['status']
