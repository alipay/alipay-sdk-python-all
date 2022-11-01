#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTruspleCustomsauthinitSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTruspleCustomsauthinitSubmitResponse, self).__init__()
        self._agreement_no = None
        self._auth_required = None
        self._end_date = None
        self._org_code = None
        self._start_date = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def auth_required(self):
        return self._auth_required

    @auth_required.setter
    def auth_required(self, value):
        self._auth_required = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTruspleCustomsauthinitSubmitResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'auth_required' in response:
            self.auth_required = response['auth_required']
        if 'end_date' in response:
            self.end_date = response['end_date']
        if 'org_code' in response:
            self.org_code = response['org_code']
        if 'start_date' in response:
            self.start_date = response['start_date']
