#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeUserclassificationCreateormodifyModel(object):

    def __init__(self):
        self._classification_name = None
        self._classification_value = None
        self._user_id = None

    @property
    def classification_name(self):
        return self._classification_name

    @classification_name.setter
    def classification_name(self, value):
        self._classification_name = value
    @property
    def classification_value(self):
        return self._classification_value

    @classification_value.setter
    def classification_value(self, value):
        self._classification_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.classification_name:
            if hasattr(self.classification_name, 'to_alipay_dict'):
                params['classification_name'] = self.classification_name.to_alipay_dict()
            else:
                params['classification_name'] = self.classification_name
        if self.classification_value:
            if hasattr(self.classification_value, 'to_alipay_dict'):
                params['classification_value'] = self.classification_value.to_alipay_dict()
            else:
                params['classification_value'] = self.classification_value
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
        o = MybankPaymentTradeUserclassificationCreateormodifyModel()
        if 'classification_name' in d:
            o.classification_name = d['classification_name']
        if 'classification_value' in d:
            o.classification_value = d['classification_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


