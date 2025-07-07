#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCreditInfoVO(object):

    def __init__(self):
        self._category_id = None
        self._zm_service_id = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCreditInfoVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


