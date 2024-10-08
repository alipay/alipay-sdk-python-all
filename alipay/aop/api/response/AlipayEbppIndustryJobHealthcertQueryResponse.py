#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobHealthcertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobHealthcertQueryResponse, self).__init__()
        self._has_cert = None
        self._open_id = None
        self._scope = None
        self._uid = None
        self._valid_period = None

    @property
    def has_cert(self):
        return self._has_cert

    @has_cert.setter
    def has_cert(self, value):
        self._has_cert = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobHealthcertQueryResponse, self).parse_response_content(response_content)
        if 'has_cert' in response:
            self.has_cert = response['has_cert']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'scope' in response:
            self.scope = response['scope']
        if 'uid' in response:
            self.uid = response['uid']
        if 'valid_period' in response:
            self.valid_period = response['valid_period']
