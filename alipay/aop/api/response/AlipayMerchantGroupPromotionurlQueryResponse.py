#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupPromotionurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupPromotionurlQueryResponse, self).__init__()
        self._promotion_url = None

    @property
    def promotion_url(self):
        return self._promotion_url

    @promotion_url.setter
    def promotion_url(self, value):
        self._promotion_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupPromotionurlQueryResponse, self).parse_response_content(response_content)
        if 'promotion_url' in response:
            self.promotion_url = response['promotion_url']
