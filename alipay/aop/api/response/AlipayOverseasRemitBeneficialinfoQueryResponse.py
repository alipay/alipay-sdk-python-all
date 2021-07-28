#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasRemitBeneficialinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasRemitBeneficialinfoQueryResponse, self).__init__()
        self._bank_account = None
        self._bank_english_name = None
        self._bank_inst_id = None
        self._bank_name = None
        self._extend_info = None
        self._has_sync_result = None

    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_english_name(self):
        return self._bank_english_name

    @bank_english_name.setter
    def bank_english_name(self, value):
        self._bank_english_name = value
    @property
    def bank_inst_id(self):
        return self._bank_inst_id

    @bank_inst_id.setter
    def bank_inst_id(self, value):
        self._bank_inst_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def has_sync_result(self):
        return self._has_sync_result

    @has_sync_result.setter
    def has_sync_result(self, value):
        self._has_sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasRemitBeneficialinfoQueryResponse, self).parse_response_content(response_content)
        if 'bank_account' in response:
            self.bank_account = response['bank_account']
        if 'bank_english_name' in response:
            self.bank_english_name = response['bank_english_name']
        if 'bank_inst_id' in response:
            self.bank_inst_id = response['bank_inst_id']
        if 'bank_name' in response:
            self.bank_name = response['bank_name']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'has_sync_result' in response:
            self.has_sync_result = response['has_sync_result']
