#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppInstserviceSignresultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInstserviceSignresultQueryResponse, self).__init__()
        self._agreement_id = None
        self._bill_key = None
        self._inst_id = None
        self._login_id = None
        self._out_agreement_id = None
        self._status = None
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInstserviceSignresultQueryResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'bill_key' in response:
            self.bill_key = response['bill_key']
        if 'inst_id' in response:
            self.inst_id = response['inst_id']
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'out_agreement_id' in response:
            self.out_agreement_id = response['out_agreement_id']
        if 'status' in response:
            self.status = response['status']
        if 'user_id' in response:
            self.user_id = response['user_id']
