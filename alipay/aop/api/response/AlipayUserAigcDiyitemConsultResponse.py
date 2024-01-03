#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAigcDiyitemConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAigcDiyitemConsultResponse, self).__init__()
        self._pass = None
        self._unpass_reason = None

    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def unpass_reason(self):
        return self._unpass_reason

    @unpass_reason.setter
    def unpass_reason(self, value):
        self._unpass_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAigcDiyitemConsultResponse, self).parse_response_content(response_content)
        if 'pass' in response:
            self.pass = response['pass']
        if 'unpass_reason' in response:
            self.unpass_reason = response['unpass_reason']
