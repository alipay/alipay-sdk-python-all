#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LiveGiftItem import LiveGiftItem


class AlipayContentLivePlatformGiftQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayContentLivePlatformGiftQueryResponse, self).__init__()
        self._biz_trace_id = None
        self._gift_list = None

    @property
    def biz_trace_id(self):
        return self._biz_trace_id

    @biz_trace_id.setter
    def biz_trace_id(self, value):
        self._biz_trace_id = value
    @property
    def gift_list(self):
        return self._gift_list

    @gift_list.setter
    def gift_list(self, value):
        if isinstance(value, list):
            self._gift_list = list()
            for i in value:
                if isinstance(i, LiveGiftItem):
                    self._gift_list.append(i)
                else:
                    self._gift_list.append(LiveGiftItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayContentLivePlatformGiftQueryResponse, self).parse_response_content(response_content)
        if 'biz_trace_id' in response:
            self.biz_trace_id = response['biz_trace_id']
        if 'gift_list' in response:
            self.gift_list = response['gift_list']
