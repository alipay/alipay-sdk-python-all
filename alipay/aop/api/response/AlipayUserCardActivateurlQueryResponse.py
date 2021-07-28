#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCardActivateurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCardActivateurlQueryResponse, self).__init__()
        self._apply_card_url = None
        self._callback = None

    @property
    def apply_card_url(self):
        return self._apply_card_url

    @apply_card_url.setter
    def apply_card_url(self, value):
        self._apply_card_url = value
    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCardActivateurlQueryResponse, self).parse_response_content(response_content)
        if 'apply_card_url' in response:
            self.apply_card_url = response['apply_card_url']
        if 'callback' in response:
            self.callback = response['callback']
