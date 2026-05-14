#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalServicepackageOrderQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._order_no_list = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no_list(self):
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, value):
        if isinstance(value, list):
            self._order_no_list = list()
            for i in value:
                self._order_no_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_no_list:
            if isinstance(self.order_no_list, list):
                for i in range(0, len(self.order_no_list)):
                    element = self.order_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_no_list[i] = element.to_alipay_dict()
            if hasattr(self.order_no_list, 'to_alipay_dict'):
                params['order_no_list'] = self.order_no_list.to_alipay_dict()
            else:
                params['order_no_list'] = self.order_no_list
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
        o = AlipayCommerceMedicalServicepackageOrderQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no_list' in d:
            o.order_no_list = d['order_no_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


