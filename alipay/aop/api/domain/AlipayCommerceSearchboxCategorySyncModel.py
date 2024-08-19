#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSearchboxCategorySyncModel(object):

    def __init__(self):
        self._box_biz_type = None
        self._category_id = None
        self._category_logo = None
        self._category_name = None
        self._category_order = None
        self._category_title = None

    @property
    def box_biz_type(self):
        return self._box_biz_type

    @box_biz_type.setter
    def box_biz_type(self, value):
        self._box_biz_type = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def category_logo(self):
        return self._category_logo

    @category_logo.setter
    def category_logo(self, value):
        self._category_logo = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def category_order(self):
        return self._category_order

    @category_order.setter
    def category_order(self, value):
        self._category_order = value
    @property
    def category_title(self):
        return self._category_title

    @category_title.setter
    def category_title(self, value):
        self._category_title = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_biz_type:
            if hasattr(self.box_biz_type, 'to_alipay_dict'):
                params['box_biz_type'] = self.box_biz_type.to_alipay_dict()
            else:
                params['box_biz_type'] = self.box_biz_type
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.category_logo:
            if hasattr(self.category_logo, 'to_alipay_dict'):
                params['category_logo'] = self.category_logo.to_alipay_dict()
            else:
                params['category_logo'] = self.category_logo
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.category_order:
            if hasattr(self.category_order, 'to_alipay_dict'):
                params['category_order'] = self.category_order.to_alipay_dict()
            else:
                params['category_order'] = self.category_order
        if self.category_title:
            if hasattr(self.category_title, 'to_alipay_dict'):
                params['category_title'] = self.category_title.to_alipay_dict()
            else:
                params['category_title'] = self.category_title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceSearchboxCategorySyncModel()
        if 'box_biz_type' in d:
            o.box_biz_type = d['box_biz_type']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_logo' in d:
            o.category_logo = d['category_logo']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'category_order' in d:
            o.category_order = d['category_order']
        if 'category_title' in d:
            o.category_title = d['category_title']
        return o


