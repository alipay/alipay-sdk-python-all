#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleAuctionMerchantInfoVO(object):

    def __init__(self):
        self._auction_merchant_name = None
        self._auction_merchant_no = None
        self._auction_merchant_pid = None

    @property
    def auction_merchant_name(self):
        return self._auction_merchant_name

    @auction_merchant_name.setter
    def auction_merchant_name(self, value):
        self._auction_merchant_name = value
    @property
    def auction_merchant_no(self):
        return self._auction_merchant_no

    @auction_merchant_no.setter
    def auction_merchant_no(self, value):
        self._auction_merchant_no = value
    @property
    def auction_merchant_pid(self):
        return self._auction_merchant_pid

    @auction_merchant_pid.setter
    def auction_merchant_pid(self, value):
        self._auction_merchant_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.auction_merchant_name:
            if hasattr(self.auction_merchant_name, 'to_alipay_dict'):
                params['auction_merchant_name'] = self.auction_merchant_name.to_alipay_dict()
            else:
                params['auction_merchant_name'] = self.auction_merchant_name
        if self.auction_merchant_no:
            if hasattr(self.auction_merchant_no, 'to_alipay_dict'):
                params['auction_merchant_no'] = self.auction_merchant_no.to_alipay_dict()
            else:
                params['auction_merchant_no'] = self.auction_merchant_no
        if self.auction_merchant_pid:
            if hasattr(self.auction_merchant_pid, 'to_alipay_dict'):
                params['auction_merchant_pid'] = self.auction_merchant_pid.to_alipay_dict()
            else:
                params['auction_merchant_pid'] = self.auction_merchant_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleAuctionMerchantInfoVO()
        if 'auction_merchant_name' in d:
            o.auction_merchant_name = d['auction_merchant_name']
        if 'auction_merchant_no' in d:
            o.auction_merchant_no = d['auction_merchant_no']
        if 'auction_merchant_pid' in d:
            o.auction_merchant_pid = d['auction_merchant_pid']
        return o


