#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniShopActivityCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniShopActivityCancelResponse, self).__init__()
        self._out_biz_id = None

    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniShopActivityCancelResponse, self).parse_response_content(response_content)
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
