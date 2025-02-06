#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpuDetailInfo(object):

    def __init__(self):
        self._category = None
        self._category_id = None
        self._description = None
        self._id = None
        self._image = None
        self._name = None
        self._sales_status = None
        self._sales_status_desc = None
        self._spu_id = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sales_status(self):
        return self._sales_status

    @sales_status.setter
    def sales_status(self, value):
        self._sales_status = value
    @property
    def sales_status_desc(self):
        return self._sales_status_desc

    @sales_status_desc.setter
    def sales_status_desc(self, value):
        self._sales_status_desc = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sales_status:
            if hasattr(self.sales_status, 'to_alipay_dict'):
                params['sales_status'] = self.sales_status.to_alipay_dict()
            else:
                params['sales_status'] = self.sales_status
        if self.sales_status_desc:
            if hasattr(self.sales_status_desc, 'to_alipay_dict'):
                params['sales_status_desc'] = self.sales_status_desc.to_alipay_dict()
            else:
                params['sales_status_desc'] = self.sales_status_desc
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpuDetailInfo()
        if 'category' in d:
            o.category = d['category']
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'description' in d:
            o.description = d['description']
        if 'id' in d:
            o.id = d['id']
        if 'image' in d:
            o.image = d['image']
        if 'name' in d:
            o.name = d['name']
        if 'sales_status' in d:
            o.sales_status = d['sales_status']
        if 'sales_status_desc' in d:
            o.sales_status_desc = d['sales_status_desc']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        return o


