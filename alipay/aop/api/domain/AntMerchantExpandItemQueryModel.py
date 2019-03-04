#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandItemQueryModel(object):

    def __init__(self):
        self._front_category_id = None
        self._status = None
        self._target_id = None
        self._target_type = None
        self._undefined_category = None

    @property
    def front_category_id(self):
        return self._front_category_id

    @front_category_id.setter
    def front_category_id(self, value):
        self._front_category_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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
    @property
    def undefined_category(self):
        return self._undefined_category

    @undefined_category.setter
    def undefined_category(self, value):
        self._undefined_category = value


    def to_alipay_dict(self):
        params = dict()
        if self.front_category_id:
            if hasattr(self.front_category_id, 'to_alipay_dict'):
                params['front_category_id'] = self.front_category_id.to_alipay_dict()
            else:
                params['front_category_id'] = self.front_category_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        if self.undefined_category:
            if hasattr(self.undefined_category, 'to_alipay_dict'):
                params['undefined_category'] = self.undefined_category.to_alipay_dict()
            else:
                params['undefined_category'] = self.undefined_category
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandItemQueryModel()
        if 'front_category_id' in d:
            o.front_category_id = d['front_category_id']
        if 'status' in d:
            o.status = d['status']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_type' in d:
            o.target_type = d['target_type']
        if 'undefined_category' in d:
            o.undefined_category = d['undefined_category']
        return o


