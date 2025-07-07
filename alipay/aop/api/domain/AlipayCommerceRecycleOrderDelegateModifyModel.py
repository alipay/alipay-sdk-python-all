#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleOrderDelegateModifyModel(object):

    def __init__(self):
        self._delegate_type = None
        self._open_id = None
        self._order_id = None
        self._user_address = None
        self._user_area = None
        self._user_city = None
        self._user_id = None
        self._user_phone = None
        self._user_province = None

    @property
    def delegate_type(self):
        return self._delegate_type

    @delegate_type.setter
    def delegate_type(self, value):
        self._delegate_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_address(self):
        return self._user_address

    @user_address.setter
    def user_address(self, value):
        self._user_address = value
    @property
    def user_area(self):
        return self._user_area

    @user_area.setter
    def user_area(self, value):
        self._user_area = value
    @property
    def user_city(self):
        return self._user_city

    @user_city.setter
    def user_city(self, value):
        self._user_city = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_phone(self):
        return self._user_phone

    @user_phone.setter
    def user_phone(self, value):
        self._user_phone = value
    @property
    def user_province(self):
        return self._user_province

    @user_province.setter
    def user_province(self, value):
        self._user_province = value


    def to_alipay_dict(self):
        params = dict()
        if self.delegate_type:
            if hasattr(self.delegate_type, 'to_alipay_dict'):
                params['delegate_type'] = self.delegate_type.to_alipay_dict()
            else:
                params['delegate_type'] = self.delegate_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.user_address:
            if hasattr(self.user_address, 'to_alipay_dict'):
                params['user_address'] = self.user_address.to_alipay_dict()
            else:
                params['user_address'] = self.user_address
        if self.user_area:
            if hasattr(self.user_area, 'to_alipay_dict'):
                params['user_area'] = self.user_area.to_alipay_dict()
            else:
                params['user_area'] = self.user_area
        if self.user_city:
            if hasattr(self.user_city, 'to_alipay_dict'):
                params['user_city'] = self.user_city.to_alipay_dict()
            else:
                params['user_city'] = self.user_city
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_phone:
            if hasattr(self.user_phone, 'to_alipay_dict'):
                params['user_phone'] = self.user_phone.to_alipay_dict()
            else:
                params['user_phone'] = self.user_phone
        if self.user_province:
            if hasattr(self.user_province, 'to_alipay_dict'):
                params['user_province'] = self.user_province.to_alipay_dict()
            else:
                params['user_province'] = self.user_province
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRecycleOrderDelegateModifyModel()
        if 'delegate_type' in d:
            o.delegate_type = d['delegate_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_address' in d:
            o.user_address = d['user_address']
        if 'user_area' in d:
            o.user_area = d['user_area']
        if 'user_city' in d:
            o.user_city = d['user_city']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_phone' in d:
            o.user_phone = d['user_phone']
        if 'user_province' in d:
            o.user_province = d['user_province']
        return o


