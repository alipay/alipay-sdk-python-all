#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfItemCategoryQualificationVO import AxfItemCategoryQualificationVO


class AxfItemCategoryVO(object):

    def __init__(self):
        self._category_code = None
        self._category_name = None
        self._category_status = None
        self._parent_category_code = None
        self._required_qualifications = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_status(self):
        return self._category_status

    @category_status.setter
    def category_status(self, value):
        self._category_status = value
    @property
    def parent_category_code(self):
        return self._parent_category_code

    @parent_category_code.setter
    def parent_category_code(self, value):
        self._parent_category_code = value
    @property
    def required_qualifications(self):
        return self._required_qualifications

    @required_qualifications.setter
    def required_qualifications(self, value):
        if isinstance(value, AxfItemCategoryQualificationVO):
            self._required_qualifications = value
        else:
            self._required_qualifications = AxfItemCategoryQualificationVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_status:
            if hasattr(self.category_status, 'to_alipay_dict'):
                params['category_status'] = self.category_status.to_alipay_dict()
            else:
                params['category_status'] = self.category_status
        if self.parent_category_code:
            if hasattr(self.parent_category_code, 'to_alipay_dict'):
                params['parent_category_code'] = self.parent_category_code.to_alipay_dict()
            else:
                params['parent_category_code'] = self.parent_category_code
        if self.required_qualifications:
            if hasattr(self.required_qualifications, 'to_alipay_dict'):
                params['required_qualifications'] = self.required_qualifications.to_alipay_dict()
            else:
                params['required_qualifications'] = self.required_qualifications
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfItemCategoryVO()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_status' in d:
            o.category_status = d['category_status']
        if 'parent_category_code' in d:
            o.parent_category_code = d['parent_category_code']
        if 'required_qualifications' in d:
            o.required_qualifications = d['required_qualifications']
        return o


