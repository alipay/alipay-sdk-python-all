#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductSignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductSignQueryResponse, self).__init__()
        self._agreement_id = None
        self._bill_key = None
        self._charge_inst = None
        self._out_agreement_id = None
        self._sign_date = None
        self._user_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductSignQueryResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'charge_inst' in response:
            self.charge_inst = response['charge_inst']
        if 'out_agreement_id' in response:
            self.out_agreement_id = response['out_agreement_id']
        if 'sign_date' in response:
            self.sign_date = response['sign_date']
        if 'user_id' in response:
            self.user_id = response['user_id']
