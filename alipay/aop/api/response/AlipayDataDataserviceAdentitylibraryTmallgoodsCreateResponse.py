#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdentitylibraryTmallgoodsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdentitylibraryTmallgoodsCreateResponse, self).__init__()
        self._goods_id = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdentitylibraryTmallgoodsCreateResponse, self).parse_response_content(response_content)
        if 'goods_id' in response:
            self.goods_id = response['goods_id']
