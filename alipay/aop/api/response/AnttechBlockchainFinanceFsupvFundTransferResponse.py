#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceFsupvFundTransferResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceFsupvFundTransferResponse, self).__init__()
        self._accepted_no = None
        self._mark = None
        self._status = None

    @property
    def accepted_no(self):
        return self._accepted_no

    @accepted_no.setter
    def accepted_no(self, value):
        self._accepted_no = value
    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        self._mark = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceFsupvFundTransferResponse, self).parse_response_content(response_content)
        if 'accepted_no' in response:
            self.accepted_no = response['accepted_no']
        if 'mark' in response:
            self.mark = response['mark']
        if 'status' in response:
            self.status = response['status']
