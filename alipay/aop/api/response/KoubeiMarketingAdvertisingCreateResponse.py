#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingAdvertisingCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingAdvertisingCreateResponse, self).__init__()
        self._ad_id = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingAdvertisingCreateResponse, self).parse_response_content(response_content)
        if 'ad_id' in response:
            self.ad_id = response['ad_id']
