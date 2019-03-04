#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppFlowQualificationDetectModel(object):

    def __init__(self):
        self._mobile = None
        self._product_id = None
        self._user_id = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        if isinstance(value, list):
            self._product_id = list()
            for i in value:
                self._product_id.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.product_id:
            if isinstance(self.product_id, list):
                for i in range(0, len(self.product_id)):
                    element = self.product_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_id[i] = element.to_alipay_dict()
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
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
        o = AlipayEbppFlowQualificationDetectModel()
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


