#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTvpAccountApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTvpAccountApplyResponse, self).__init__()
        self._account_no = None
        self._authorized_link = None

    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def authorized_link(self):
        return self._authorized_link

    @authorized_link.setter
    def authorized_link(self, value):
        self._authorized_link = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTvpAccountApplyResponse, self).parse_response_content(response_content)
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'authorized_link' in response:
            self.authorized_link = response['authorized_link']
