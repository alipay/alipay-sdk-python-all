#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAliyunbenefitReceiveModel(object):

    def __init__(self):
        self._biz_date = None
        self._item_id = None
        self._out_biz_no = None
        self._price_strategy = None
        self._user_id = None
        self._verify_point = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def price_strategy(self):
        return self._price_strategy

    @price_strategy.setter
    def price_strategy(self, value):
        self._price_strategy = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_point(self):
        return self._verify_point

    @verify_point.setter
    def verify_point(self, value):
        self._verify_point = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.price_strategy:
            if hasattr(self.price_strategy, 'to_alipay_dict'):
                params['price_strategy'] = self.price_strategy.to_alipay_dict()
            else:
                params['price_strategy'] = self.price_strategy
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify_point:
            if hasattr(self.verify_point, 'to_alipay_dict'):
                params['verify_point'] = self.verify_point.to_alipay_dict()
            else:
                params['verify_point'] = self.verify_point
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAliyunbenefitReceiveModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'price_strategy' in d:
            o.price_strategy = d['price_strategy']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify_point' in d:
            o.verify_point = d['verify_point']
        return o


