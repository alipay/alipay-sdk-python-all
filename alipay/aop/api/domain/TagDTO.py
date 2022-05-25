#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TagDTO(object):

    def __init__(self):
        self._cate_id = None
        self._category_name = None
        self._data_type = None
        self._scene_code = None
        self._show_type = None
        self._store_type = None
        self._tag_code = None
        self._tag_desc = None
        self._tag_kind = None
        self._tag_name = None
        self._tag_type = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value
    @property
    def store_type(self):
        return self._store_type

    @store_type.setter
    def store_type(self, value):
        self._store_type = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_desc(self):
        return self._tag_desc

    @tag_desc.setter
    def tag_desc(self, value):
        self._tag_desc = value
    @property
    def tag_kind(self):
        return self._tag_kind

    @tag_kind.setter
    def tag_kind(self, value):
        self._tag_kind = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def tag_type(self):
        return self._tag_type

    @tag_type.setter
    def tag_type(self, value):
        self._tag_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        if self.store_type:
            if hasattr(self.store_type, 'to_alipay_dict'):
                params['store_type'] = self.store_type.to_alipay_dict()
            else:
                params['store_type'] = self.store_type
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_desc:
            if hasattr(self.tag_desc, 'to_alipay_dict'):
                params['tag_desc'] = self.tag_desc.to_alipay_dict()
            else:
                params['tag_desc'] = self.tag_desc
        if self.tag_kind:
            if hasattr(self.tag_kind, 'to_alipay_dict'):
                params['tag_kind'] = self.tag_kind.to_alipay_dict()
            else:
                params['tag_kind'] = self.tag_kind
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.tag_type:
            if hasattr(self.tag_type, 'to_alipay_dict'):
                params['tag_type'] = self.tag_type.to_alipay_dict()
            else:
                params['tag_type'] = self.tag_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TagDTO()
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'store_type' in d:
            o.store_type = d['store_type']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_desc' in d:
            o.tag_desc = d['tag_desc']
        if 'tag_kind' in d:
            o.tag_kind = d['tag_kind']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        return o


