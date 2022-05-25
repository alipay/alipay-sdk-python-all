#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TagDistDTO import TagDistDTO


class TagRuleItemDTO(object):

    def __init__(self):
        self._data_type = None
        self._datas = None
        self._scene_code = None
        self._show_type = None
        self._store_type = None
        self._tag_code = None
        self._tag_name = None
        self._tag_type = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, value):
        if isinstance(value, list):
            self._datas = list()
            for i in value:
                if isinstance(i, TagDistDTO):
                    self._datas.append(i)
                else:
                    self._datas.append(TagDistDTO.from_alipay_dict(i))
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
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.datas:
            if isinstance(self.datas, list):
                for i in range(0, len(self.datas)):
                    element = self.datas[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.datas[i] = element.to_alipay_dict()
            if hasattr(self.datas, 'to_alipay_dict'):
                params['datas'] = self.datas.to_alipay_dict()
            else:
                params['datas'] = self.datas
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
        o = TagRuleItemDTO()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'datas' in d:
            o.datas = d['datas']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'store_type' in d:
            o.store_type = d['store_type']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'tag_type' in d:
            o.tag_type = d['tag_type']
        return o


