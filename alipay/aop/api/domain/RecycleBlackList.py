#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecyleBlackAddress import RecyleBlackAddress


class RecycleBlackList(object):

    def __init__(self):
        self._address = None
        self._forbidden_reason = None
        self._forbidden_time = None
        self._mobile = None
        self._open_id = None
        self._order_id = None
        self._user_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, RecyleBlackAddress):
            self._address = value
        else:
            self._address = RecyleBlackAddress.from_alipay_dict(value)
    @property
    def forbidden_reason(self):
        return self._forbidden_reason

    @forbidden_reason.setter
    def forbidden_reason(self, value):
        self._forbidden_reason = value
    @property
    def forbidden_time(self):
        return self._forbidden_time

    @forbidden_time.setter
    def forbidden_time(self, value):
        self._forbidden_time = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.forbidden_reason:
            if hasattr(self.forbidden_reason, 'to_alipay_dict'):
                params['forbidden_reason'] = self.forbidden_reason.to_alipay_dict()
            else:
                params['forbidden_reason'] = self.forbidden_reason
        if self.forbidden_time:
            if hasattr(self.forbidden_time, 'to_alipay_dict'):
                params['forbidden_time'] = self.forbidden_time.to_alipay_dict()
            else:
                params['forbidden_time'] = self.forbidden_time
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = RecycleBlackList()
        if 'address' in d:
            o.address = d['address']
        if 'forbidden_reason' in d:
            o.forbidden_reason = d['forbidden_reason']
        if 'forbidden_time' in d:
            o.forbidden_time = d['forbidden_time']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


