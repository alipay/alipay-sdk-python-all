#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EvaluteIndicateId import EvaluteIndicateId
from alipay.aop.api.domain.EvaluateIndicateGrade import EvaluateIndicateGrade


class EvaluateIndicate(object):

    def __init__(self):
        self._children_ids = None
        self._grade_indicates = None
        self._isv_indicate_desc = None
        self._isv_indicate_id = None
        self._isv_indicate_img = None
        self._isv_indicate_name = None

    @property
    def children_ids(self):
        return self._children_ids

    @children_ids.setter
    def children_ids(self, value):
        if isinstance(value, list):
            self._children_ids = list()
            for i in value:
                if isinstance(i, EvaluteIndicateId):
                    self._children_ids.append(i)
                else:
                    self._children_ids.append(EvaluteIndicateId.from_alipay_dict(i))
    @property
    def grade_indicates(self):
        return self._grade_indicates

    @grade_indicates.setter
    def grade_indicates(self, value):
        if isinstance(value, list):
            self._grade_indicates = list()
            for i in value:
                if isinstance(i, EvaluateIndicateGrade):
                    self._grade_indicates.append(i)
                else:
                    self._grade_indicates.append(EvaluateIndicateGrade.from_alipay_dict(i))
    @property
    def isv_indicate_desc(self):
        return self._isv_indicate_desc

    @isv_indicate_desc.setter
    def isv_indicate_desc(self, value):
        self._isv_indicate_desc = value
    @property
    def isv_indicate_id(self):
        return self._isv_indicate_id

    @isv_indicate_id.setter
    def isv_indicate_id(self, value):
        self._isv_indicate_id = value
    @property
    def isv_indicate_img(self):
        return self._isv_indicate_img

    @isv_indicate_img.setter
    def isv_indicate_img(self, value):
        self._isv_indicate_img = value
    @property
    def isv_indicate_name(self):
        return self._isv_indicate_name

    @isv_indicate_name.setter
    def isv_indicate_name(self, value):
        self._isv_indicate_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.children_ids:
            if isinstance(self.children_ids, list):
                for i in range(0, len(self.children_ids)):
                    element = self.children_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.children_ids[i] = element.to_alipay_dict()
            if hasattr(self.children_ids, 'to_alipay_dict'):
                params['children_ids'] = self.children_ids.to_alipay_dict()
            else:
                params['children_ids'] = self.children_ids
        if self.grade_indicates:
            if isinstance(self.grade_indicates, list):
                for i in range(0, len(self.grade_indicates)):
                    element = self.grade_indicates[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.grade_indicates[i] = element.to_alipay_dict()
            if hasattr(self.grade_indicates, 'to_alipay_dict'):
                params['grade_indicates'] = self.grade_indicates.to_alipay_dict()
            else:
                params['grade_indicates'] = self.grade_indicates
        if self.isv_indicate_desc:
            if hasattr(self.isv_indicate_desc, 'to_alipay_dict'):
                params['isv_indicate_desc'] = self.isv_indicate_desc.to_alipay_dict()
            else:
                params['isv_indicate_desc'] = self.isv_indicate_desc
        if self.isv_indicate_id:
            if hasattr(self.isv_indicate_id, 'to_alipay_dict'):
                params['isv_indicate_id'] = self.isv_indicate_id.to_alipay_dict()
            else:
                params['isv_indicate_id'] = self.isv_indicate_id
        if self.isv_indicate_img:
            if hasattr(self.isv_indicate_img, 'to_alipay_dict'):
                params['isv_indicate_img'] = self.isv_indicate_img.to_alipay_dict()
            else:
                params['isv_indicate_img'] = self.isv_indicate_img
        if self.isv_indicate_name:
            if hasattr(self.isv_indicate_name, 'to_alipay_dict'):
                params['isv_indicate_name'] = self.isv_indicate_name.to_alipay_dict()
            else:
                params['isv_indicate_name'] = self.isv_indicate_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EvaluateIndicate()
        if 'children_ids' in d:
            o.children_ids = d['children_ids']
        if 'grade_indicates' in d:
            o.grade_indicates = d['grade_indicates']
        if 'isv_indicate_desc' in d:
            o.isv_indicate_desc = d['isv_indicate_desc']
        if 'isv_indicate_id' in d:
            o.isv_indicate_id = d['isv_indicate_id']
        if 'isv_indicate_img' in d:
            o.isv_indicate_img = d['isv_indicate_img']
        if 'isv_indicate_name' in d:
            o.isv_indicate_name = d['isv_indicate_name']
        return o


