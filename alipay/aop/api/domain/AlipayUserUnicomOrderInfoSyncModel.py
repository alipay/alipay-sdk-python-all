#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserUnicomOrderInfoSyncModel(object):

    def __init__(self):
        self._gmt_order_change = None
        self._order_no = None
        self._order_operate_type = None
        self._phone_no = None
        self._product_name = None
        self._sec_key = None
        self._user_id = None

    @property
    def gmt_order_change(self):
        return self._gmt_order_change

    @gmt_order_change.setter
    def gmt_order_change(self, value):
        self._gmt_order_change = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_operate_type(self):
        return self._order_operate_type

    @order_operate_type.setter
    def order_operate_type(self, value):
        self._order_operate_type = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def sec_key(self):
        return self._sec_key

    @sec_key.setter
    def sec_key(self, value):
        self._sec_key = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_order_change:
            if hasattr(self.gmt_order_change, 'to_alipay_dict'):
                params['gmt_order_change'] = self.gmt_order_change.to_alipay_dict()
            else:
                params['gmt_order_change'] = self.gmt_order_change
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_operate_type:
            if hasattr(self.order_operate_type, 'to_alipay_dict'):
                params['order_operate_type'] = self.order_operate_type.to_alipay_dict()
            else:
                params['order_operate_type'] = self.order_operate_type
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.sec_key:
            if hasattr(self.sec_key, 'to_alipay_dict'):
                params['sec_key'] = self.sec_key.to_alipay_dict()
            else:
                params['sec_key'] = self.sec_key
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
        o = AlipayUserUnicomOrderInfoSyncModel()
        if 'gmt_order_change' in d:
            o.gmt_order_change = d['gmt_order_change']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_operate_type' in d:
            o.order_operate_type = d['order_operate_type']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'sec_key' in d:
            o.sec_key = d['sec_key']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


