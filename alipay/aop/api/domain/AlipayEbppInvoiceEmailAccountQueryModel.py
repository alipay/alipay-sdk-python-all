#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceEmailAccountQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._user_id = None
        self._user_mobile = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_mobile(self):
        return self._user_mobile

    @user_mobile.setter
    def user_mobile(self, value):
        self._user_mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_mobile:
            if hasattr(self.user_mobile, 'to_alipay_dict'):
                params['user_mobile'] = self.user_mobile.to_alipay_dict()
            else:
                params['user_mobile'] = self.user_mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceEmailAccountQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_mobile' in d:
            o.user_mobile = d['user_mobile']
        return o


