#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeUsercertMatchResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeUsercertMatchResponse, self).__init__()
        self._cert_no = None
        self._matched = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def matched(self):
        return self._matched

    @matched.setter
    def matched(self, value):
        self._matched = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeUsercertMatchResponse, self).parse_response_content(response_content)
        if 'cert_no' in response:
            self.cert_no = response['cert_no']
        if 'matched' in response:
            self.matched = response['matched']
