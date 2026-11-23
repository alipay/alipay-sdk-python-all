#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductRelationDTO(object):

    def __init__(self):
        self._display_scene = None
        self._product_id = None
        self._product_type = None
        self._sort_no = None

    @property
    def display_scene(self):
        return self._display_scene

    @display_scene.setter
    def display_scene(self, value):
        self._display_scene = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def sort_no(self):
        return self._sort_no

    @sort_no.setter
    def sort_no(self, value):
        self._sort_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_scene:
            if hasattr(self.display_scene, 'to_alipay_dict'):
                params['display_scene'] = self.display_scene.to_alipay_dict()
            else:
                params['display_scene'] = self.display_scene
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.sort_no:
            if hasattr(self.sort_no, 'to_alipay_dict'):
                params['sort_no'] = self.sort_no.to_alipay_dict()
            else:
                params['sort_no'] = self.sort_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductRelationDTO()
        if 'display_scene' in d:
            o.display_scene = d['display_scene']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'sort_no' in d:
            o.sort_no = d['sort_no']
        return o


