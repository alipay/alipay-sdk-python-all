#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalSmsShorturlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSmsShorturlGetResponse, self).__init__()
        self._msg_url = None

    @property
    def msg_url(self):
        return self._msg_url

    @msg_url.setter
    def msg_url(self, value):
        self._msg_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSmsShorturlGetResponse, self).parse_response_content(response_content)
        if 'msg_url' in response:
            self.msg_url = response['msg_url']
