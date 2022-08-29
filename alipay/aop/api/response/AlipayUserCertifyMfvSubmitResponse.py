#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyMfvSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyMfvSubmitResponse, self).__init__()
        self._ext_info = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyMfvSubmitResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
