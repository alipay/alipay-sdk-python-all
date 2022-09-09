#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KVObj import KVObj
from alipay.aop.api.domain.NimitzPageCond import NimitzPageCond
from alipay.aop.api.domain.NimitzRangeCond import NimitzRangeCond


class DatasetRequest(object):

    def __init__(self):
        self._fields = None
        self._individual_dim_keys = None
        self._obj_dim_keys = None
        self._page_cond = None
        self._range_cond = None
        self._reversed = None
        self._rs_dataset = None

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                self._fields.append(i)
    @property
    def individual_dim_keys(self):
        return self._individual_dim_keys

    @individual_dim_keys.setter
    def individual_dim_keys(self, value):
        if isinstance(value, list):
            self._individual_dim_keys = list()
            for i in value:
                if isinstance(i, KVObj):
                    self._individual_dim_keys.append(i)
                else:
                    self._individual_dim_keys.append(KVObj.from_alipay_dict(i))
    @property
    def obj_dim_keys(self):
        return self._obj_dim_keys

    @obj_dim_keys.setter
    def obj_dim_keys(self, value):
        if isinstance(value, list):
            self._obj_dim_keys = list()
            for i in value:
                self._obj_dim_keys.append(i)
    @property
    def page_cond(self):
        return self._page_cond

    @page_cond.setter
    def page_cond(self, value):
        if isinstance(value, NimitzPageCond):
            self._page_cond = value
        else:
            self._page_cond = NimitzPageCond.from_alipay_dict(value)
    @property
    def range_cond(self):
        return self._range_cond

    @range_cond.setter
    def range_cond(self, value):
        if isinstance(value, NimitzRangeCond):
            self._range_cond = value
        else:
            self._range_cond = NimitzRangeCond.from_alipay_dict(value)
    @property
    def reversed(self):
        return self._reversed

    @reversed.setter
    def reversed(self, value):
        self._reversed = value
    @property
    def rs_dataset(self):
        return self._rs_dataset

    @rs_dataset.setter
    def rs_dataset(self, value):
        self._rs_dataset = value


    def to_alipay_dict(self):
        params = dict()
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.individual_dim_keys:
            if isinstance(self.individual_dim_keys, list):
                for i in range(0, len(self.individual_dim_keys)):
                    element = self.individual_dim_keys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.individual_dim_keys[i] = element.to_alipay_dict()
            if hasattr(self.individual_dim_keys, 'to_alipay_dict'):
                params['individual_dim_keys'] = self.individual_dim_keys.to_alipay_dict()
            else:
                params['individual_dim_keys'] = self.individual_dim_keys
        if self.obj_dim_keys:
            if isinstance(self.obj_dim_keys, list):
                for i in range(0, len(self.obj_dim_keys)):
                    element = self.obj_dim_keys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.obj_dim_keys[i] = element.to_alipay_dict()
            if hasattr(self.obj_dim_keys, 'to_alipay_dict'):
                params['obj_dim_keys'] = self.obj_dim_keys.to_alipay_dict()
            else:
                params['obj_dim_keys'] = self.obj_dim_keys
        if self.page_cond:
            if hasattr(self.page_cond, 'to_alipay_dict'):
                params['page_cond'] = self.page_cond.to_alipay_dict()
            else:
                params['page_cond'] = self.page_cond
        if self.range_cond:
            if hasattr(self.range_cond, 'to_alipay_dict'):
                params['range_cond'] = self.range_cond.to_alipay_dict()
            else:
                params['range_cond'] = self.range_cond
        if self.reversed:
            if hasattr(self.reversed, 'to_alipay_dict'):
                params['reversed'] = self.reversed.to_alipay_dict()
            else:
                params['reversed'] = self.reversed
        if self.rs_dataset:
            if hasattr(self.rs_dataset, 'to_alipay_dict'):
                params['rs_dataset'] = self.rs_dataset.to_alipay_dict()
            else:
                params['rs_dataset'] = self.rs_dataset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatasetRequest()
        if 'fields' in d:
            o.fields = d['fields']
        if 'individual_dim_keys' in d:
            o.individual_dim_keys = d['individual_dim_keys']
        if 'obj_dim_keys' in d:
            o.obj_dim_keys = d['obj_dim_keys']
        if 'page_cond' in d:
            o.page_cond = d['page_cond']
        if 'range_cond' in d:
            o.range_cond = d['range_cond']
        if 'reversed' in d:
            o.reversed = d['reversed']
        if 'rs_dataset' in d:
            o.rs_dataset = d['rs_dataset']
        return o


