#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvestigCategoryData(object):

    def __init__(self):
        self._category = None
        self._data_version = None
        self._entity_code = None
        self._entity_name = None
        self._entity_type = None
        self._model_result_object = None
        self._state = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def entity_code(self):
        return self._entity_code

    @entity_code.setter
    def entity_code(self, value):
        self._entity_code = value
    @property
    def entity_name(self):
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        self._entity_name = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def model_result_object(self):
        return self._model_result_object

    @model_result_object.setter
    def model_result_object(self, value):
        self._model_result_object = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.entity_code:
            if hasattr(self.entity_code, 'to_alipay_dict'):
                params['entity_code'] = self.entity_code.to_alipay_dict()
            else:
                params['entity_code'] = self.entity_code
        if self.entity_name:
            if hasattr(self.entity_name, 'to_alipay_dict'):
                params['entity_name'] = self.entity_name.to_alipay_dict()
            else:
                params['entity_name'] = self.entity_name
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.model_result_object:
            if hasattr(self.model_result_object, 'to_alipay_dict'):
                params['model_result_object'] = self.model_result_object.to_alipay_dict()
            else:
                params['model_result_object'] = self.model_result_object
        if self.state:
            if hasattr(self.state, 'to_alipay_dict'):
                params['state'] = self.state.to_alipay_dict()
            else:
                params['state'] = self.state
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvestigCategoryData()
        if 'category' in d:
            o.category = d['category']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'entity_code' in d:
            o.entity_code = d['entity_code']
        if 'entity_name' in d:
            o.entity_name = d['entity_name']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'model_result_object' in d:
            o.model_result_object = d['model_result_object']
        if 'state' in d:
            o.state = d['state']
        return o


