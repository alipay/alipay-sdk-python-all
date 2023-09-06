#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyRarenameMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyRarenameMatchResponse, self).__init__()
        self._ret_code = None

    @property
    def ret_code(self):
        return self._ret_code

    @ret_code.setter
    def ret_code(self, value):
        self._ret_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyRarenameMatchResponse, self).parse_response_content(response_content)
        if 'ret_code' in response:
            self.ret_code = response['ret_code']
