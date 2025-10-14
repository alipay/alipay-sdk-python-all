#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObjTagRequest(object):

    def __init__(self):
        self._obj_ids = None
        self._obj_types = None
        self._tag_codes = None
        self._tag_groups = None

    @property
    def obj_ids(self):
        return self._obj_ids

    @obj_ids.setter
    def obj_ids(self, value):
        if isinstance(value, list):
            self._obj_ids = list()
            for i in value:
                self._obj_ids.append(i)
    @property
    def obj_types(self):
        return self._obj_types

    @obj_types.setter
    def obj_types(self, value):
        if isinstance(value, list):
            self._obj_types = list()
            for i in value:
                self._obj_types.append(i)
    @property
    def tag_codes(self):
        return self._tag_codes

    @tag_codes.setter
    def tag_codes(self, value):
        if isinstance(value, list):
            self._tag_codes = list()
            for i in value:
                self._tag_codes.append(i)
    @property
    def tag_groups(self):
        return self._tag_groups

    @tag_groups.setter
    def tag_groups(self, value):
        if isinstance(value, list):
            self._tag_groups = list()
            for i in value:
                self._tag_groups.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.obj_ids:
            if isinstance(self.obj_ids, list):
                for i in range(0, len(self.obj_ids)):
                    element = self.obj_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.obj_ids[i] = element.to_alipay_dict()
            if hasattr(self.obj_ids, 'to_alipay_dict'):
                params['obj_ids'] = self.obj_ids.to_alipay_dict()
            else:
                params['obj_ids'] = self.obj_ids
        if self.obj_types:
            if isinstance(self.obj_types, list):
                for i in range(0, len(self.obj_types)):
                    element = self.obj_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.obj_types[i] = element.to_alipay_dict()
            if hasattr(self.obj_types, 'to_alipay_dict'):
                params['obj_types'] = self.obj_types.to_alipay_dict()
            else:
                params['obj_types'] = self.obj_types
        if self.tag_codes:
            if isinstance(self.tag_codes, list):
                for i in range(0, len(self.tag_codes)):
                    element = self.tag_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_codes[i] = element.to_alipay_dict()
            if hasattr(self.tag_codes, 'to_alipay_dict'):
                params['tag_codes'] = self.tag_codes.to_alipay_dict()
            else:
                params['tag_codes'] = self.tag_codes
        if self.tag_groups:
            if isinstance(self.tag_groups, list):
                for i in range(0, len(self.tag_groups)):
                    element = self.tag_groups[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tag_groups[i] = element.to_alipay_dict()
            if hasattr(self.tag_groups, 'to_alipay_dict'):
                params['tag_groups'] = self.tag_groups.to_alipay_dict()
            else:
                params['tag_groups'] = self.tag_groups
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjTagRequest()
        if 'obj_ids' in d:
            o.obj_ids = d['obj_ids']
        if 'obj_types' in d:
            o.obj_types = d['obj_types']
        if 'tag_codes' in d:
            o.tag_codes = d['tag_codes']
        if 'tag_groups' in d:
            o.tag_groups = d['tag_groups']
        return o


