#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAqUserinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAqUserinfoQueryResponse, self).__init__()
        self._has_quick_account = None
        self._random_key = None

    @property
    def has_quick_account(self):
        return self._has_quick_account

    @has_quick_account.setter
    def has_quick_account(self, value):
        self._has_quick_account = value
    @property
    def random_key(self):
        return self._random_key

    @random_key.setter
    def random_key(self, value):
        self._random_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAqUserinfoQueryResponse, self).parse_response_content(response_content)
        if 'has_quick_account' in response:
            self.has_quick_account = response['has_quick_account']
        if 'random_key' in response:
            self.random_key = response['random_key']
