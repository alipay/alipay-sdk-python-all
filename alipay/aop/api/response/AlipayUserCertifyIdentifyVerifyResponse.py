#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyIdentifyVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyIdentifyVerifyResponse, self).__init__()
        self._biz_code_status = None

    @property
    def biz_code_status(self):
        return self._biz_code_status

    @biz_code_status.setter
    def biz_code_status(self, value):
        self._biz_code_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyIdentifyVerifyResponse, self).parse_response_content(response_content)
        if 'biz_code_status' in response:
            self.biz_code_status = response['biz_code_status']
