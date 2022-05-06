#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserDTO(object):

    def __init__(self):
        self._order_num = None
        self._user_id = None
        self._user_name = None
        self._user_no = None

    @property
    def order_num(self):
        return self._order_num

    @order_num.setter
    def order_num(self, value):
        self._order_num = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def user_no(self):
        return self._user_no

    @user_no.setter
    def user_no(self, value):
        self._user_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.order_num:
            if hasattr(self.order_num, 'to_alipay_dict'):
                params['order_num'] = self.order_num.to_alipay_dict()
            else:
                params['order_num'] = self.order_num
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.user_no:
            if hasattr(self.user_no, 'to_alipay_dict'):
                params['user_no'] = self.user_no.to_alipay_dict()
            else:
                params['user_no'] = self.user_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserDTO()
        if 'order_num' in d:
            o.order_num = d['order_num']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'user_no' in d:
            o.user_no = d['user_no']
        return o


