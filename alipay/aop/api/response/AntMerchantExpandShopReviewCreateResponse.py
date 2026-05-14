#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandShopReviewCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandShopReviewCreateResponse, self).__init__()
        self._sync_time = None

    @property
    def sync_time(self):
        return self._sync_time

    @sync_time.setter
    def sync_time(self, value):
        self._sync_time = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandShopReviewCreateResponse, self).parse_response_content(response_content)
        if 'sync_time' in response:
            self.sync_time = response['sync_time']
