#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinancePfPaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinancePfPaymentQueryResponse, self).__init__()
        self._account_in_status = None
        self._parm = None

    @property
    def account_in_status(self):
        return self._account_in_status

    @account_in_status.setter
    def account_in_status(self, value):
        self._account_in_status = value
    @property
    def parm(self):
        return self._parm

    @parm.setter
    def parm(self, value):
        self._parm = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinancePfPaymentQueryResponse, self).parse_response_content(response_content)
        if 'account_in_status' in response:
            self.account_in_status = response['account_in_status']
        if 'parm' in response:
            self.parm = response['parm']
