#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundJointaccountSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundJointaccountSignQueryResponse, self).__init__()
        self._account_id = None
        self._agreement_no = None
        self._status = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundJointaccountSignQueryResponse, self).parse_response_content(response_content)
        if 'account_id' in response:
            self.account_id = response['account_id']
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'status' in response:
            self.status = response['status']
