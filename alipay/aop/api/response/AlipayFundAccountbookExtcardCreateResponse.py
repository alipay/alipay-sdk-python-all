#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundAccountbookExtcardCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundAccountbookExtcardCreateResponse, self).__init__()
        self._biz_scene = None
        self._card_create_time = None
        self._card_no = None
        self._product_code = None
        self._status = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def card_create_time(self):
        return self._card_create_time

    @card_create_time.setter
    def card_create_time(self, value):
        self._card_create_time = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundAccountbookExtcardCreateResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'card_create_time' in response:
            self.card_create_time = response['card_create_time']
        if 'card_no' in response:
            self.card_no = response['card_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'status' in response:
            self.status = response['status']
