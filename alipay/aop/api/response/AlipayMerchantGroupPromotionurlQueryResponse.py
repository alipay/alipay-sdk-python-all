#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupPromotionurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupPromotionurlQueryResponse, self).__init__()
        self._group_name = None
        self._promotion_url = None

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def promotion_url(self):
        return self._promotion_url

    @promotion_url.setter
    def promotion_url(self, value):
        self._promotion_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupPromotionurlQueryResponse, self).parse_response_content(response_content)
        if 'group_name' in response:
            self.group_name = response['group_name']
        if 'promotion_url' in response:
            self.promotion_url = response['promotion_url']
