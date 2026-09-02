#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportRailwayCouponQueryModel(object):

    def __init__(self):
        self._activity_id = None
        self._open_id = None
        self._phone_list = None
        self._request_id = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def phone_list(self):
        return self._phone_list

    @phone_list.setter
    def phone_list(self, value):
        if isinstance(value, list):
            self._phone_list = list()
            for i in value:
                self._phone_list.append(i)
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
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.phone_list:
            if isinstance(self.phone_list, list):
                for i in range(0, len(self.phone_list)):
                    element = self.phone_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_list[i] = element.to_alipay_dict()
            if hasattr(self.phone_list, 'to_alipay_dict'):
                params['phone_list'] = self.phone_list.to_alipay_dict()
            else:
                params['phone_list'] = self.phone_list
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
        o = AlipayCommerceTransportRailwayCouponQueryModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'phone_list' in d:
            o.phone_list = d['phone_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


