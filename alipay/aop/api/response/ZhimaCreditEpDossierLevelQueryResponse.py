#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditEpDossierLevelQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierLevelQueryResponse, self).__init__()
        self._credit_level = None
        self._evaluate_time = None
        self._has_authed = None

    @property
    def credit_level(self):
        return self._credit_level

    @credit_level.setter
    def credit_level(self, value):
        self._credit_level = value
    @property
    def evaluate_time(self):
        return self._evaluate_time

    @evaluate_time.setter
    def evaluate_time(self, value):
        self._evaluate_time = value
    @property
    def has_authed(self):
        return self._has_authed

    @has_authed.setter
    def has_authed(self, value):
        self._has_authed = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierLevelQueryResponse, self).parse_response_content(response_content)
        if 'credit_level' in response:
            self.credit_level = response['credit_level']
        if 'evaluate_time' in response:
            self.evaluate_time = response['evaluate_time']
        if 'has_authed' in response:
            self.has_authed = response['has_authed']
