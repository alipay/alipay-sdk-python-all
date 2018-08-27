#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobileRecommendGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobileRecommendGetResponse, self).__init__()
        self._ext_info = None
        self._items = None
        self._recommend_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobileRecommendGetResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'items' in response:
            self.items = response['items']
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
