#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosDiscountDetail(object):

    def __init__(self):
        self._activity_id = None
        self._activity_type = None
        self._discount_name = None
        self._discount_type = None
        self._dish_id = None
        self._ext_info = None
        self._mrt_discount = None
        self._rt_discount = None
        self._target_user_type = None
        self._used_item_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def mrt_discount(self):
        return self._mrt_discount

    @mrt_discount.setter
    def mrt_discount(self, value):
        self._mrt_discount = value
    @property
    def rt_discount(self):
        return self._rt_discount

    @rt_discount.setter
    def rt_discount(self, value):
        self._rt_discount = value
    @property
    def target_user_type(self):
        return self._target_user_type

    @target_user_type.setter
    def target_user_type(self, value):
        self._target_user_type = value
    @property
    def used_item_id(self):
        return self._used_item_id

    @used_item_id.setter
    def used_item_id(self, value):
        self._used_item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.mrt_discount:
            if hasattr(self.mrt_discount, 'to_alipay_dict'):
                params['mrt_discount'] = self.mrt_discount.to_alipay_dict()
            else:
                params['mrt_discount'] = self.mrt_discount
        if self.rt_discount:
            if hasattr(self.rt_discount, 'to_alipay_dict'):
                params['rt_discount'] = self.rt_discount.to_alipay_dict()
            else:
                params['rt_discount'] = self.rt_discount
        if self.target_user_type:
            if hasattr(self.target_user_type, 'to_alipay_dict'):
                params['target_user_type'] = self.target_user_type.to_alipay_dict()
            else:
                params['target_user_type'] = self.target_user_type
        if self.used_item_id:
            if hasattr(self.used_item_id, 'to_alipay_dict'):
                params['used_item_id'] = self.used_item_id.to_alipay_dict()
            else:
                params['used_item_id'] = self.used_item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosDiscountDetail()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'mrt_discount' in d:
            o.mrt_discount = d['mrt_discount']
        if 'rt_discount' in d:
            o.rt_discount = d['rt_discount']
        if 'target_user_type' in d:
            o.target_user_type = d['target_user_type']
        if 'used_item_id' in d:
            o.used_item_id = d['used_item_id']
        return o


