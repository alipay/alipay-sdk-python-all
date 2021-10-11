#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskTitleInfo(object):

    def __init__(self):
        self._remain_point_amount = None
        self._shop_name = None

    @property
    def remain_point_amount(self):
        return self._remain_point_amount

    @remain_point_amount.setter
    def remain_point_amount(self, value):
        self._remain_point_amount = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.remain_point_amount:
            if hasattr(self.remain_point_amount, 'to_alipay_dict'):
                params['remain_point_amount'] = self.remain_point_amount.to_alipay_dict()
            else:
                params['remain_point_amount'] = self.remain_point_amount
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskTitleInfo()
        if 'remain_point_amount' in d:
            o.remain_point_amount = d['remain_point_amount']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        return o


