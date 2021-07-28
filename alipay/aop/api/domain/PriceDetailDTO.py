#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PriceDetailDTO(object):

    def __init__(self):
        self._price_click_url = None
        self._price_title = None

    @property
    def price_click_url(self):
        return self._price_click_url

    @price_click_url.setter
    def price_click_url(self, value):
        self._price_click_url = value
    @property
    def price_title(self):
        return self._price_title

    @price_title.setter
    def price_title(self, value):
        self._price_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.price_click_url:
            if hasattr(self.price_click_url, 'to_alipay_dict'):
                params['price_click_url'] = self.price_click_url.to_alipay_dict()
            else:
                params['price_click_url'] = self.price_click_url
        if self.price_title:
            if hasattr(self.price_title, 'to_alipay_dict'):
                params['price_title'] = self.price_title.to_alipay_dict()
            else:
                params['price_title'] = self.price_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PriceDetailDTO()
        if 'price_click_url' in d:
            o.price_click_url = d['price_click_url']
        if 'price_title' in d:
            o.price_title = d['price_title']
        return o


