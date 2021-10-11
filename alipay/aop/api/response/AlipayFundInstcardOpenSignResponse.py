#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundInstcardOpenSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundInstcardOpenSignResponse, self).__init__()
        self._account_name = None
        self._account_no = None
        self._account_status = None
        self._inst_id = None
        self._inst_name = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundInstcardOpenSignResponse, self).parse_response_content(response_content)
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'account_no' in response:
            self.account_no = response['account_no']
        if 'account_status' in response:
            self.account_status = response['account_status']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'inst_name' in response:
            self.inst_name = response['inst_name']
