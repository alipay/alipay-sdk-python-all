#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMicropayOrderFreezepayurlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMicropayOrderFreezepayurlGetResponse, self).__init__()
        self._pay_freeze_url = None

    @property
    def pay_freeze_url(self):
        return self._pay_freeze_url

    @pay_freeze_url.setter
    def pay_freeze_url(self, value):
        self._pay_freeze_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMicropayOrderFreezepayurlGetResponse, self).parse_response_content(response_content)
        if 'pay_freeze_url' in response:
            self.pay_freeze_url = response['pay_freeze_url']
