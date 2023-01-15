#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InquiryChannel(object):

    def __init__(self):
        self._inquiry_mode = None
        self._inquiry_price = None
        self._inquiry_type = None
        self._inquiry_url = None

    @property
    def inquiry_mode(self):
        return self._inquiry_mode

    @inquiry_mode.setter
    def inquiry_mode(self, value):
        self._inquiry_mode = value
    @property
    def inquiry_price(self):
        return self._inquiry_price

    @inquiry_price.setter
    def inquiry_price(self, value):
        self._inquiry_price = value
    @property
    def inquiry_type(self):
        return self._inquiry_type

    @inquiry_type.setter
    def inquiry_type(self, value):
        self._inquiry_type = value
    @property
    def inquiry_url(self):
        return self._inquiry_url

    @inquiry_url.setter
    def inquiry_url(self, value):
        self._inquiry_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.inquiry_mode:
            if hasattr(self.inquiry_mode, 'to_alipay_dict'):
                params['inquiry_mode'] = self.inquiry_mode.to_alipay_dict()
            else:
                params['inquiry_mode'] = self.inquiry_mode
        if self.inquiry_price:
            if hasattr(self.inquiry_price, 'to_alipay_dict'):
                params['inquiry_price'] = self.inquiry_price.to_alipay_dict()
            else:
                params['inquiry_price'] = self.inquiry_price
        if self.inquiry_type:
            if hasattr(self.inquiry_type, 'to_alipay_dict'):
                params['inquiry_type'] = self.inquiry_type.to_alipay_dict()
            else:
                params['inquiry_type'] = self.inquiry_type
        if self.inquiry_url:
            if hasattr(self.inquiry_url, 'to_alipay_dict'):
                params['inquiry_url'] = self.inquiry_url.to_alipay_dict()
            else:
                params['inquiry_url'] = self.inquiry_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InquiryChannel()
        if 'inquiry_mode' in d:
            o.inquiry_mode = d['inquiry_mode']
        if 'inquiry_price' in d:
            o.inquiry_price = d['inquiry_price']
        if 'inquiry_type' in d:
            o.inquiry_type = d['inquiry_type']
        if 'inquiry_url' in d:
            o.inquiry_url = d['inquiry_url']
        return o


