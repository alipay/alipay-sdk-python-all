#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAipayNowpayProductModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAipayNowpayProductModifyResponse, self).__init__()
        self._product_description = None
        self._product_icon_url = None
        self._product_name = None
        self._product_url = None

    @property
    def product_description(self):
        return self._product_description

    @product_description.setter
    def product_description(self, value):
        self._product_description = value
    @property
    def product_icon_url(self):
        return self._product_icon_url

    @product_icon_url.setter
    def product_icon_url(self, value):
        self._product_icon_url = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def product_url(self):
        return self._product_url

    @product_url.setter
    def product_url(self, value):
        self._product_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayAipayNowpayProductModifyResponse, self).parse_response_content(response_content)
        if 'product_description' in response:
            self.product_description = response['product_description']
        if 'product_icon_url' in response:
            self.product_icon_url = response['product_icon_url']
        if 'product_name' in response:
            self.product_name = response['product_name']
        if 'product_url' in response:
            self.product_url = response['product_url']
