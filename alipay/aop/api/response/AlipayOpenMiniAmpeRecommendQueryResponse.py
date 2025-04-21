#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeRecommendQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeRecommendQueryResponse, self).__init__()
        self._card_url = None

    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeRecommendQueryResponse, self).parse_response_content(response_content)
        if 'card_url' in response:
            self.card_url = response['card_url']
