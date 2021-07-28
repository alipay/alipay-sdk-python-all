#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityOwnercardCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityOwnercardCreateResponse, self).__init__()
        self._alipay_card_id = None

    @property
    def alipay_card_id(self):
        return self._alipay_card_id

    @alipay_card_id.setter
    def alipay_card_id(self, value):
        self._alipay_card_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityOwnercardCreateResponse, self).parse_response_content(response_content)
        if 'alipay_card_id' in response:
            self.alipay_card_id = response['alipay_card_id']
