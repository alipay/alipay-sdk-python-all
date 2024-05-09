#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbasePassportHuaweimpCreateResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbasePassportHuaweimpCreateResponse, self).__init__()
        self._account_name = None
        self._idempotent = None
        self._passport_id = None

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def idempotent(self):
        return self._idempotent

    @idempotent.setter
    def idempotent(self, value):
        self._idempotent = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbasePassportHuaweimpCreateResponse, self).parse_response_content(response_content)
        if 'account_name' in response:
            self.account_name = response['account_name']
        if 'idempotent' in response:
            self.idempotent = response['idempotent']
        if 'passport_id' in response:
            self.passport_id = response['passport_id']
