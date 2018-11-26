#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PracticeEntity(object):

    def __init__(self):
        self._id = None
        self._merchant_id = None
        self._practice_name = None
        self._shop_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def practice_name(self):
        return self._practice_name

    @practice_name.setter
    def practice_name(self, value):
        self._practice_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.practice_name:
            if hasattr(self.practice_name, 'to_alipay_dict'):
                params['practice_name'] = self.practice_name.to_alipay_dict()
            else:
                params['practice_name'] = self.practice_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PracticeEntity()
        if 'id' in d:
            o.id = d['id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'practice_name' in d:
            o.practice_name = d['practice_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


