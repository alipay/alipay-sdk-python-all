#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogMmtcaftscvTemplateVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvTemplateVerifyResponse, self).__init__()
        self._accuracy = None
        self._pass = None
        self._remark = None

    @property
    def accuracy(self):
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value):
        self._accuracy = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvTemplateVerifyResponse, self).parse_response_content(response_content)
        if 'accuracy' in response:
            self.accuracy = response['accuracy']
        if 'pass' in response:
            self.pass = response['pass']
        if 'remark' in response:
            self.remark = response['remark']
