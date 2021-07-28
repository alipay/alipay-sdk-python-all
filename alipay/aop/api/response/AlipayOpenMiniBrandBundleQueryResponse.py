#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniBrandBundleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBrandBundleQueryResponse, self).__init__()
        self._brand_certified = None
        self._brand_word = None

    @property
    def brand_certified(self):
        return self._brand_certified

    @brand_certified.setter
    def brand_certified(self, value):
        self._brand_certified = value
    @property
    def brand_word(self):
        return self._brand_word

    @brand_word.setter
    def brand_word(self, value):
        self._brand_word = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBrandBundleQueryResponse, self).parse_response_content(response_content)
        if 'brand_certified' in response:
            self.brand_certified = response['brand_certified']
        if 'brand_word' in response:
            self.brand_word = response['brand_word']
