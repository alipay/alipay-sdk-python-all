#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicLabelQueryResponse, self).__init__()
        self._code = None
        self._labels = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        if isinstance(value, list):
            self._labels = list()
            for i in value:
                self._labels.append(i)
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicLabelQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'labels' in response:
            self.labels = response['labels']
        if 'msg' in response:
            self.msg = response['msg']
