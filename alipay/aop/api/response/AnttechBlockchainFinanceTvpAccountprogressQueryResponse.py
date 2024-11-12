#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTvpAccountprogressQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpAccountprogressQueryResponse, self).__init__()
        self._account_no = None
        self._status = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpAccountprogressQueryResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'status' in response:
            self.status = response['status']
