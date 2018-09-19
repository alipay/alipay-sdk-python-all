#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileBksigntokenVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileBksigntokenVerifyResponse, self).__init__()
        self._createtimestamp = None
        self._loginid = None
        self._memo = None
        self._resultcode = None
        self._success = None
        self._userid = None

    @property
    def createtimestamp(self):
        return self._createtimestamp

    @createtimestamp.setter
    def createtimestamp(self, value):
        self._createtimestamp = value
    @property
    def loginid(self):
        return self._loginid

    @loginid.setter
    def loginid(self, value):
        self._loginid = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def resultcode(self):
        return self._resultcode

    @resultcode.setter
    def resultcode(self, value):
        self._resultcode = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileBksigntokenVerifyResponse, self).parse_response_content(response_content)
        if 'createtimestamp' in response:
            self.createtimestamp = response['createtimestamp']
        if 'loginid' in response:
            self.loginid = response['loginid']
        if 'memo' in response:
            self.memo = response['memo']
        if 'resultcode' in response:
            self.resultcode = response['resultcode']
        if 'success' in response:
            self.success = response['success']
        if 'userid' in response:
            self.userid = response['userid']
