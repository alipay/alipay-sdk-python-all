#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportAdUserMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdUserMatchResponse, self).__init__()
        self._ad_user_id = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdUserMatchResponse, self).parse_response_content(response_content)
        if 'ad_user_id' in response:
            self.ad_user_id = response['ad_user_id']
