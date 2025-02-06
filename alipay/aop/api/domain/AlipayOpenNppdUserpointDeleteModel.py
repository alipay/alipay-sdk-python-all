#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenNppdUserpointDeleteModel(object):

    def __init__(self):
        self._benefit_id = None
        self._deducted_date = None
        self._item_list = None
        self._lm_order_id = None
        self._merchant_code = None
        self._merchant_exts = None
        self._open_id = None
        self._point = None
        self._request_id = None
        self._user_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def deducted_date(self):
        return self._deducted_date

    @deducted_date.setter
    def deducted_date(self, value):
        self._deducted_date = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        self._item_list = value
    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def merchant_code(self):
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, value):
        self._merchant_code = value
    @property
    def merchant_exts(self):
        return self._merchant_exts

    @merchant_exts.setter
    def merchant_exts(self, value):
        self._merchant_exts = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.deducted_date:
            if hasattr(self.deducted_date, 'to_alipay_dict'):
                params['deducted_date'] = self.deducted_date.to_alipay_dict()
            else:
                params['deducted_date'] = self.deducted_date
        if self.item_list:
            if hasattr(self.item_list, 'to_alipay_dict'):
                params['item_list'] = self.item_list.to_alipay_dict()
            else:
                params['item_list'] = self.item_list
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.merchant_code:
            if hasattr(self.merchant_code, 'to_alipay_dict'):
                params['merchant_code'] = self.merchant_code.to_alipay_dict()
            else:
                params['merchant_code'] = self.merchant_code
        if self.merchant_exts:
            if hasattr(self.merchant_exts, 'to_alipay_dict'):
                params['merchant_exts'] = self.merchant_exts.to_alipay_dict()
            else:
                params['merchant_exts'] = self.merchant_exts
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.point:
            if hasattr(self.point, 'to_alipay_dict'):
                params['point'] = self.point.to_alipay_dict()
            else:
                params['point'] = self.point
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenNppdUserpointDeleteModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'deducted_date' in d:
            o.deducted_date = d['deducted_date']
        if 'item_list' in d:
            o.item_list = d['item_list']
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'merchant_code' in d:
            o.merchant_code = d['merchant_code']
        if 'merchant_exts' in d:
            o.merchant_exts = d['merchant_exts']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'point' in d:
            o.point = d['point']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


