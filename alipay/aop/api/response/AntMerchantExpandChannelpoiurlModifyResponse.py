#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandChannelpoiurlModifyResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandChannelpoiurlModifyResponse, self).__init__()
        self._progress = None
        self._shop_app_id = None

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
    @property
    def shop_app_id(self):
        return self._shop_app_id

    @shop_app_id.setter
    def shop_app_id(self, value):
        self._shop_app_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandChannelpoiurlModifyResponse, self).parse_response_content(response_content)
        if 'progress' in response:
            self.progress = response['progress']
        if 'shop_app_id' in response:
            self.shop_app_id = response['shop_app_id']
