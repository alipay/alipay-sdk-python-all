#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EvaluateIndicate import EvaluateIndicate


class EvalueateItem(object):

    def __init__(self):
        self._evaluate_indicates = None
        self._evaluate_standard = None
        self._evaluate_type = None
        self._evalueate_model_img = None
        self._evalueate_report_img = None
        self._isv_model_id = None
        self._isv_model_name = None
        self._isv_series_id = None
        self._isv_series_name = None

    @property
    def evaluate_indicates(self):
        return self._evaluate_indicates

    @evaluate_indicates.setter
    def evaluate_indicates(self, value):
        if isinstance(value, list):
            self._evaluate_indicates = list()
            for i in value:
                if isinstance(i, EvaluateIndicate):
                    self._evaluate_indicates.append(i)
                else:
                    self._evaluate_indicates.append(EvaluateIndicate.from_alipay_dict(i))
    @property
    def evaluate_standard(self):
        return self._evaluate_standard

    @evaluate_standard.setter
    def evaluate_standard(self, value):
        self._evaluate_standard = value
    @property
    def evaluate_type(self):
        return self._evaluate_type

    @evaluate_type.setter
    def evaluate_type(self, value):
        self._evaluate_type = value
    @property
    def evalueate_model_img(self):
        return self._evalueate_model_img

    @evalueate_model_img.setter
    def evalueate_model_img(self, value):
        self._evalueate_model_img = value
    @property
    def evalueate_report_img(self):
        return self._evalueate_report_img

    @evalueate_report_img.setter
    def evalueate_report_img(self, value):
        self._evalueate_report_img = value
    @property
    def isv_model_id(self):
        return self._isv_model_id

    @isv_model_id.setter
    def isv_model_id(self, value):
        self._isv_model_id = value
    @property
    def isv_model_name(self):
        return self._isv_model_name

    @isv_model_name.setter
    def isv_model_name(self, value):
        self._isv_model_name = value
    @property
    def isv_series_id(self):
        return self._isv_series_id

    @isv_series_id.setter
    def isv_series_id(self, value):
        self._isv_series_id = value
    @property
    def isv_series_name(self):
        return self._isv_series_name

    @isv_series_name.setter
    def isv_series_name(self, value):
        self._isv_series_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.evaluate_indicates:
            if isinstance(self.evaluate_indicates, list):
                for i in range(0, len(self.evaluate_indicates)):
                    element = self.evaluate_indicates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.evaluate_indicates[i] = element.to_alipay_dict()
            if hasattr(self.evaluate_indicates, 'to_alipay_dict'):
                params['evaluate_indicates'] = self.evaluate_indicates.to_alipay_dict()
            else:
                params['evaluate_indicates'] = self.evaluate_indicates
        if self.evaluate_standard:
            if hasattr(self.evaluate_standard, 'to_alipay_dict'):
                params['evaluate_standard'] = self.evaluate_standard.to_alipay_dict()
            else:
                params['evaluate_standard'] = self.evaluate_standard
        if self.evaluate_type:
            if hasattr(self.evaluate_type, 'to_alipay_dict'):
                params['evaluate_type'] = self.evaluate_type.to_alipay_dict()
            else:
                params['evaluate_type'] = self.evaluate_type
        if self.evalueate_model_img:
            if hasattr(self.evalueate_model_img, 'to_alipay_dict'):
                params['evalueate_model_img'] = self.evalueate_model_img.to_alipay_dict()
            else:
                params['evalueate_model_img'] = self.evalueate_model_img
        if self.evalueate_report_img:
            if hasattr(self.evalueate_report_img, 'to_alipay_dict'):
                params['evalueate_report_img'] = self.evalueate_report_img.to_alipay_dict()
            else:
                params['evalueate_report_img'] = self.evalueate_report_img
        if self.isv_model_id:
            if hasattr(self.isv_model_id, 'to_alipay_dict'):
                params['isv_model_id'] = self.isv_model_id.to_alipay_dict()
            else:
                params['isv_model_id'] = self.isv_model_id
        if self.isv_model_name:
            if hasattr(self.isv_model_name, 'to_alipay_dict'):
                params['isv_model_name'] = self.isv_model_name.to_alipay_dict()
            else:
                params['isv_model_name'] = self.isv_model_name
        if self.isv_series_id:
            if hasattr(self.isv_series_id, 'to_alipay_dict'):
                params['isv_series_id'] = self.isv_series_id.to_alipay_dict()
            else:
                params['isv_series_id'] = self.isv_series_id
        if self.isv_series_name:
            if hasattr(self.isv_series_name, 'to_alipay_dict'):
                params['isv_series_name'] = self.isv_series_name.to_alipay_dict()
            else:
                params['isv_series_name'] = self.isv_series_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvalueateItem()
        if 'evaluate_indicates' in d:
            o.evaluate_indicates = d['evaluate_indicates']
        if 'evaluate_standard' in d:
            o.evaluate_standard = d['evaluate_standard']
        if 'evaluate_type' in d:
            o.evaluate_type = d['evaluate_type']
        if 'evalueate_model_img' in d:
            o.evalueate_model_img = d['evalueate_model_img']
        if 'evalueate_report_img' in d:
            o.evalueate_report_img = d['evalueate_report_img']
        if 'isv_model_id' in d:
            o.isv_model_id = d['isv_model_id']
        if 'isv_model_name' in d:
            o.isv_model_name = d['isv_model_name']
        if 'isv_series_id' in d:
            o.isv_series_id = d['isv_series_id']
        if 'isv_series_name' in d:
            o.isv_series_name = d['isv_series_name']
        return o


