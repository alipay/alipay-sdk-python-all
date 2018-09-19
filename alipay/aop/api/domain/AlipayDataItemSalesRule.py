#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataItemSalesRule(object):

    def __init__(self):
        self._buyer_crowd_limit = None
        self._daily_sales_limit = None
        self._user_sales_limit = None

    @property
    def buyer_crowd_limit(self):
        return self._buyer_crowd_limit

    @buyer_crowd_limit.setter
    def buyer_crowd_limit(self, value):
        self._buyer_crowd_limit = value
    @property
    def daily_sales_limit(self):
        return self._daily_sales_limit

    @daily_sales_limit.setter
    def daily_sales_limit(self, value):
        self._daily_sales_limit = value
    @property
    def user_sales_limit(self):
        return self._user_sales_limit

    @user_sales_limit.setter
    def user_sales_limit(self, value):
        if isinstance(value, list):
            self._user_sales_limit = list()
            for i in value:
                self._user_sales_limit.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_crowd_limit:
            if hasattr(self.buyer_crowd_limit, 'to_alipay_dict'):
                params['buyer_crowd_limit'] = self.buyer_crowd_limit.to_alipay_dict()
            else:
                params['buyer_crowd_limit'] = self.buyer_crowd_limit
        if self.daily_sales_limit:
            if hasattr(self.daily_sales_limit, 'to_alipay_dict'):
                params['daily_sales_limit'] = self.daily_sales_limit.to_alipay_dict()
            else:
                params['daily_sales_limit'] = self.daily_sales_limit
        if self.user_sales_limit:
            if isinstance(self.user_sales_limit, list):
                for i in range(0, len(self.user_sales_limit)):
                    element = self.user_sales_limit[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_sales_limit[i] = element.to_alipay_dict()
            if hasattr(self.user_sales_limit, 'to_alipay_dict'):
                params['user_sales_limit'] = self.user_sales_limit.to_alipay_dict()
            else:
                params['user_sales_limit'] = self.user_sales_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataItemSalesRule()
        if 'buyer_crowd_limit' in d:
            o.buyer_crowd_limit = d['buyer_crowd_limit']
        if 'daily_sales_limit' in d:
            o.daily_sales_limit = d['daily_sales_limit']
        if 'user_sales_limit' in d:
            o.user_sales_limit = d['user_sales_limit']
        return o


