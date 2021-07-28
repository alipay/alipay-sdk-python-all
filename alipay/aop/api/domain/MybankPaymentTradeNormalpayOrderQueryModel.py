#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeNormalpayOrderQueryModel(object):

    def __init__(self):
        self._biz_channel = None
        self._buyer_info = None
        self._order_no = None
        self._request_no = None
        self._seller_info = None

    @property
    def biz_channel(self):
        return self._biz_channel

    @biz_channel.setter
    def biz_channel(self, value):
        self._biz_channel = value
    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        self._buyer_info = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def seller_info(self):
        return self._seller_info

    @seller_info.setter
    def seller_info(self, value):
        self._seller_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_channel:
            if hasattr(self.biz_channel, 'to_alipay_dict'):
                params['biz_channel'] = self.biz_channel.to_alipay_dict()
            else:
                params['biz_channel'] = self.biz_channel
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.seller_info:
            if hasattr(self.seller_info, 'to_alipay_dict'):
                params['seller_info'] = self.seller_info.to_alipay_dict()
            else:
                params['seller_info'] = self.seller_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeNormalpayOrderQueryModel()
        if 'biz_channel' in d:
            o.biz_channel = d['biz_channel']
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'seller_info' in d:
            o.seller_info = d['seller_info']
        return o


