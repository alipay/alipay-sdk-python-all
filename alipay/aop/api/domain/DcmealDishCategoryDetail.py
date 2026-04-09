#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DcmealDishCategoryDetail(object):

    def __init__(self):
        self._campus_id = None
        self._campus_name = None
        self._category_id = None
        self._category_name = None
        self._category_no = None
        self._parent_id = None
        self._remark = None
        self._restaurant_id = None
        self._restaurant_name = None

    @property
    def campus_id(self):
        return self._campus_id

    @campus_id.setter
    def campus_id(self, value):
        self._campus_id = value
    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_no(self):
        return self._category_no

    @category_no.setter
    def category_no(self, value):
        self._category_no = value
    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        self._parent_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def restaurant_id(self):
        return self._restaurant_id

    @restaurant_id.setter
    def restaurant_id(self, value):
        self._restaurant_id = value
    @property
    def restaurant_name(self):
        return self._restaurant_name

    @restaurant_name.setter
    def restaurant_name(self, value):
        self._restaurant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_id:
            if hasattr(self.campus_id, 'to_alipay_dict'):
                params['campus_id'] = self.campus_id.to_alipay_dict()
            else:
                params['campus_id'] = self.campus_id
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_no:
            if hasattr(self.category_no, 'to_alipay_dict'):
                params['category_no'] = self.category_no.to_alipay_dict()
            else:
                params['category_no'] = self.category_no
        if self.parent_id:
            if hasattr(self.parent_id, 'to_alipay_dict'):
                params['parent_id'] = self.parent_id.to_alipay_dict()
            else:
                params['parent_id'] = self.parent_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.restaurant_id:
            if hasattr(self.restaurant_id, 'to_alipay_dict'):
                params['restaurant_id'] = self.restaurant_id.to_alipay_dict()
            else:
                params['restaurant_id'] = self.restaurant_id
        if self.restaurant_name:
            if hasattr(self.restaurant_name, 'to_alipay_dict'):
                params['restaurant_name'] = self.restaurant_name.to_alipay_dict()
            else:
                params['restaurant_name'] = self.restaurant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DcmealDishCategoryDetail()
        if 'campus_id' in d:
            o.campus_id = d['campus_id']
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_no' in d:
            o.category_no = d['category_no']
        if 'parent_id' in d:
            o.parent_id = d['parent_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'restaurant_id' in d:
            o.restaurant_id = d['restaurant_id']
        if 'restaurant_name' in d:
            o.restaurant_name = d['restaurant_name']
        return o


