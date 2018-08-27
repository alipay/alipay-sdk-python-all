#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiShopMallPageQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiShopMallPageQueryResponse, self).__init__()
        self._mall_url = None

    @property
    def mall_url(self):
        return self._mall_url

    @mall_url.setter
    def mall_url(self, value):
        self._mall_url = value

    def parse_response_content(self, response_content):
        response = super(KoubeiShopMallPageQueryResponse, self).parse_response_content(response_content)
        if 'mall_url' in response:
            self.mall_url = response['mall_url']
