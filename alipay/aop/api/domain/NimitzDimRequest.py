#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KVObj import KVObj
from alipay.aop.api.domain.NimitzPageCond import NimitzPageCond
from alipay.aop.api.domain.NimitzRangeCond import NimitzRangeCond


class NimitzDimRequest(object):

    def __init__(self):
        self._fields = None
        self._kv_attributes = None
        self._page_cond = None
        self._range_attributes = None
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
    def kv_attributes(self):
        return self._kv_attributes

    @kv_attributes.setter
    def kv_attributes(self, value):
        if isinstance(value, list):
            self._kv_attributes = list()
            for i in value:
                if isinstance(i, KVObj):
                    self._kv_attributes.append(i)
                else:
                    self._kv_attributes.append(KVObj.from_alipay_dict(i))
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
    def range_attributes(self):
        return self._range_attributes

    @range_attributes.setter
    def range_attributes(self, value):
        if isinstance(value, list):
            self._range_attributes = list()
            for i in value:
                if isinstance(i, NimitzRangeCond):
                    self._range_attributes.append(i)
                else:
                    self._range_attributes.append(NimitzRangeCond.from_alipay_dict(i))
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
        if self.kv_attributes:
            if isinstance(self.kv_attributes, list):
                for i in range(0, len(self.kv_attributes)):
                    element = self.kv_attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.kv_attributes[i] = element.to_alipay_dict()
            if hasattr(self.kv_attributes, 'to_alipay_dict'):
                params['kv_attributes'] = self.kv_attributes.to_alipay_dict()
            else:
                params['kv_attributes'] = self.kv_attributes
        if self.page_cond:
            if hasattr(self.page_cond, 'to_alipay_dict'):
                params['page_cond'] = self.page_cond.to_alipay_dict()
            else:
                params['page_cond'] = self.page_cond
        if self.range_attributes:
            if isinstance(self.range_attributes, list):
                for i in range(0, len(self.range_attributes)):
                    element = self.range_attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.range_attributes[i] = element.to_alipay_dict()
            if hasattr(self.range_attributes, 'to_alipay_dict'):
                params['range_attributes'] = self.range_attributes.to_alipay_dict()
            else:
                params['range_attributes'] = self.range_attributes
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
        o = NimitzDimRequest()
        if 'fields' in d:
            o.fields = d['fields']
        if 'kv_attributes' in d:
            o.kv_attributes = d['kv_attributes']
        if 'page_cond' in d:
            o.page_cond = d['page_cond']
        if 'range_attributes' in d:
            o.range_attributes = d['range_attributes']
        if 'rs_dataset' in d:
            o.rs_dataset = d['rs_dataset']
        return o


