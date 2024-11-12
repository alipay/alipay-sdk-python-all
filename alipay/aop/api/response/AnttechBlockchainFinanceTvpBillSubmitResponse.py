#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTvpBillSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpBillSubmitResponse, self).__init__()
        self._bill_no = None
        self._status = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpBillSubmitResponse, self).parse_response_content(response_content)
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
        if 'status' in response:
            self.status = response['status']
