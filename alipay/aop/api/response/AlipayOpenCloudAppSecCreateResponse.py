#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenCloudAppSecCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenCloudAppSecCreateResponse, self).__init__()
        self._alipay_public_key = None

    @property
    def alipay_public_key(self):
        return self._alipay_public_key

    @alipay_public_key.setter
    def alipay_public_key(self, value):
        self._alipay_public_key = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenCloudAppSecCreateResponse, self).parse_response_content(response_content)
        if 'alipay_public_key' in response:
            self.alipay_public_key = response['alipay_public_key']
