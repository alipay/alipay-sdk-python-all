#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandClassificationCreateormodifyModel(object):

    def __init__(self):
        self._classification_key = None
        self._classification_value = None
        self._target_id = None
        self._target_type = None

    @property
    def classification_key(self):
        return self._classification_key

    @classification_key.setter
    def classification_key(self, value):
        self._classification_key = value
    @property
    def classification_value(self):
        return self._classification_value

    @classification_value.setter
    def classification_value(self, value):
        self._classification_value = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.classification_key:
            if hasattr(self.classification_key, 'to_alipay_dict'):
                params['classification_key'] = self.classification_key.to_alipay_dict()
            else:
                params['classification_key'] = self.classification_key
        if self.classification_value:
            if hasattr(self.classification_value, 'to_alipay_dict'):
                params['classification_value'] = self.classification_value.to_alipay_dict()
            else:
                params['classification_value'] = self.classification_value
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_type:
            if hasattr(self.target_type, 'to_alipay_dict'):
                params['target_type'] = self.target_type.to_alipay_dict()
            else:
                params['target_type'] = self.target_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandClassificationCreateormodifyModel()
        if 'classification_key' in d:
            o.classification_key = d['classification_key']
        if 'classification_value' in d:
            o.classification_value = d['classification_value']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        return o


