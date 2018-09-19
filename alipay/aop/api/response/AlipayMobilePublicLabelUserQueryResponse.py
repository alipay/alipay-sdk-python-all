#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicLabelUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicLabelUserQueryResponse, self).__init__()
        self._code = None
        self._label_ids = None
        self._msg = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def label_ids(self):
        return self._label_ids

    @label_ids.setter
    def label_ids(self, value):
        self._label_ids = value
    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicLabelUserQueryResponse, self).parse_response_content(response_content)
        if 'code' in response:
            self.code = response['code']
        if 'label_ids' in response:
            self.label_ids = response['label_ids']
        if 'msg' in response:
            self.msg = response['msg']
