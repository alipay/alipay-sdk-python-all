#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NetFlowOfferInfo(object):

    def __init__(self):
        self._effective_time = None
        self._expire_time = None
        self._offer_name = None
        self._order_time = None

    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def offer_name(self):
        return self._offer_name

    @offer_name.setter
    def offer_name(self, value):
        self._offer_name = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.offer_name:
            if hasattr(self.offer_name, 'to_alipay_dict'):
                params['offer_name'] = self.offer_name.to_alipay_dict()
            else:
                params['offer_name'] = self.offer_name
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NetFlowOfferInfo()
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'offer_name' in d:
            o.offer_name = d['offer_name']
        if 'order_time' in d:
            o.order_time = d['order_time']
        return o


