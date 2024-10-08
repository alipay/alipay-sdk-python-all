#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyOrderSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyOrderSubmitResponse, self).__init__()
        self._materials_num = None
        self._shop_num = None

    @property
    def materials_num(self):
        return self._materials_num

    @materials_num.setter
    def materials_num(self, value):
        self._materials_num = value
    @property
    def shop_num(self):
        return self._shop_num

    @shop_num.setter
    def shop_num(self, value):
        self._shop_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyOrderSubmitResponse, self).parse_response_content(response_content)
        if 'materials_num' in response:
            self.materials_num = response['materials_num']
        if 'shop_num' in response:
            self.shop_num = response['shop_num']
