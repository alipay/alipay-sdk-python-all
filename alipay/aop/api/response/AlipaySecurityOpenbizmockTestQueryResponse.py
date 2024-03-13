#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RegressionPublic import RegressionPublic


class AlipaySecurityOpenbizmockTestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityOpenbizmockTestQueryResponse, self).__init__()
        self._longitude = None
        self._mobile_number = None
        self._out_a = None
        self._para_a = None
        self._test_number = None
        self._test_string = None
        self._uid = None
        self._uid_openid = None

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value
    @property
    def out_a(self):
        return self._out_a

    @out_a.setter
    def out_a(self, value):
        if isinstance(value, RegressionPublic):
            self._out_a = value
        else:
            self._out_a = RegressionPublic.from_alipay_dict(value)
    @property
    def para_a(self):
        return self._para_a

    @para_a.setter
    def para_a(self, value):
        self._para_a = value
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        self._test_number = value
    @property
    def test_string(self):
        return self._test_string

    @test_string.setter
    def test_string(self, value):
        self._test_string = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def uid_openid(self):
        return self._uid_openid

    @uid_openid.setter
    def uid_openid(self, value):
        self._uid_openid = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityOpenbizmockTestQueryResponse, self).parse_response_content(response_content)
        if 'longitude' in response:
            self.longitude = response['longitude']
        if 'mobile_number' in response:
            self.mobile_number = response['mobile_number']
        if 'out_a' in response:
            self.out_a = response['out_a']
        if 'para_a' in response:
            self.para_a = response['para_a']
        if 'test_number' in response:
            self.test_number = response['test_number']
        if 'test_string' in response:
            self.test_string = response['test_string']
        if 'uid' in response:
            self.uid = response['uid']
        if 'uid_openid' in response:
            self.uid_openid = response['uid_openid']
