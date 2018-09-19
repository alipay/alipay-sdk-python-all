#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserIdenticalAuthbaseQueryModel(object):

    def __init__(self):
        self._base_user_id = None
        self._comparator_user_id = None

    @property
    def base_user_id(self):
        return self._base_user_id

    @base_user_id.setter
    def base_user_id(self, value):
        self._base_user_id = value
    @property
    def comparator_user_id(self):
        return self._comparator_user_id

    @comparator_user_id.setter
    def comparator_user_id(self, value):
        self._comparator_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_user_id:
            if hasattr(self.base_user_id, 'to_alipay_dict'):
                params['base_user_id'] = self.base_user_id.to_alipay_dict()
            else:
                params['base_user_id'] = self.base_user_id
        if self.comparator_user_id:
            if hasattr(self.comparator_user_id, 'to_alipay_dict'):
                params['comparator_user_id'] = self.comparator_user_id.to_alipay_dict()
            else:
                params['comparator_user_id'] = self.comparator_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserIdenticalAuthbaseQueryModel()
        if 'base_user_id' in d:
            o.base_user_id = d['base_user_id']
        if 'comparator_user_id' in d:
            o.comparator_user_id = d['comparator_user_id']
        return o


