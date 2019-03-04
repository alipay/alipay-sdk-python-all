#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppCategory(object):

    def __init__(self):
        self._category_id = None
        self._category_name = None
        self._has_child = None
        self._need_license = None
        self._need_out_door_pic = None
        self._need_special_license = None
        self._parent_category_id = None

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
    def has_child(self):
        return self._has_child

    @has_child.setter
    def has_child(self, value):
        self._has_child = value
    @property
    def need_license(self):
        return self._need_license

    @need_license.setter
    def need_license(self, value):
        self._need_license = value
    @property
    def need_out_door_pic(self):
        return self._need_out_door_pic

    @need_out_door_pic.setter
    def need_out_door_pic(self, value):
        self._need_out_door_pic = value
    @property
    def need_special_license(self):
        return self._need_special_license

    @need_special_license.setter
    def need_special_license(self, value):
        self._need_special_license = value
    @property
    def parent_category_id(self):
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, value):
        self._parent_category_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.has_child:
            if hasattr(self.has_child, 'to_alipay_dict'):
                params['has_child'] = self.has_child.to_alipay_dict()
            else:
                params['has_child'] = self.has_child
        if self.need_license:
            if hasattr(self.need_license, 'to_alipay_dict'):
                params['need_license'] = self.need_license.to_alipay_dict()
            else:
                params['need_license'] = self.need_license
        if self.need_out_door_pic:
            if hasattr(self.need_out_door_pic, 'to_alipay_dict'):
                params['need_out_door_pic'] = self.need_out_door_pic.to_alipay_dict()
            else:
                params['need_out_door_pic'] = self.need_out_door_pic
        if self.need_special_license:
            if hasattr(self.need_special_license, 'to_alipay_dict'):
                params['need_special_license'] = self.need_special_license.to_alipay_dict()
            else:
                params['need_special_license'] = self.need_special_license
        if self.parent_category_id:
            if hasattr(self.parent_category_id, 'to_alipay_dict'):
                params['parent_category_id'] = self.parent_category_id.to_alipay_dict()
            else:
                params['parent_category_id'] = self.parent_category_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppCategory()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'has_child' in d:
            o.has_child = d['has_child']
        if 'need_license' in d:
            o.need_license = d['need_license']
        if 'need_out_door_pic' in d:
            o.need_out_door_pic = d['need_out_door_pic']
        if 'need_special_license' in d:
            o.need_special_license = d['need_special_license']
        if 'parent_category_id' in d:
            o.parent_category_id = d['parent_category_id']
        return o


