#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRecycleCreditServiceEvaluateModel(object):

    def __init__(self):
        self._open_id = None
        self._service_category = None
        self._submerchant = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def service_category(self):
        return self._service_category

    @service_category.setter
    def service_category(self, value):
        self._service_category = value
    @property
    def submerchant(self):
        return self._submerchant

    @submerchant.setter
    def submerchant(self, value):
        self._submerchant = value
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
        if self.service_category:
            if hasattr(self.service_category, 'to_alipay_dict'):
                params['service_category'] = self.service_category.to_alipay_dict()
            else:
                params['service_category'] = self.service_category
        if self.submerchant:
            if hasattr(self.submerchant, 'to_alipay_dict'):
                params['submerchant'] = self.submerchant.to_alipay_dict()
            else:
                params['submerchant'] = self.submerchant
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
        o = AlipayCommerceRecycleCreditServiceEvaluateModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'service_category' in d:
            o.service_category = d['service_category']
        if 'submerchant' in d:
            o.submerchant = d['submerchant']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


