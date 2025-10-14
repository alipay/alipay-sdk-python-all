#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QuoteTagDTO(object):

    def __init__(self):
        self._ext_props = None
        self._name = None
        self._obj_id = None
        self._snapshot_date = None
        self._tag_code = None

    @property
    def ext_props(self):
        return self._ext_props

    @ext_props.setter
    def ext_props(self, value):
        self._ext_props = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def obj_id(self):
        return self._obj_id

    @obj_id.setter
    def obj_id(self, value):
        self._obj_id = value
    @property
    def snapshot_date(self):
        return self._snapshot_date

    @snapshot_date.setter
    def snapshot_date(self, value):
        self._snapshot_date = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_props:
            if hasattr(self.ext_props, 'to_alipay_dict'):
                params['ext_props'] = self.ext_props.to_alipay_dict()
            else:
                params['ext_props'] = self.ext_props
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.obj_id:
            if hasattr(self.obj_id, 'to_alipay_dict'):
                params['obj_id'] = self.obj_id.to_alipay_dict()
            else:
                params['obj_id'] = self.obj_id
        if self.snapshot_date:
            if hasattr(self.snapshot_date, 'to_alipay_dict'):
                params['snapshot_date'] = self.snapshot_date.to_alipay_dict()
            else:
                params['snapshot_date'] = self.snapshot_date
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuoteTagDTO()
        if 'ext_props' in d:
            o.ext_props = d['ext_props']
        if 'name' in d:
            o.name = d['name']
        if 'obj_id' in d:
            o.obj_id = d['obj_id']
        if 'snapshot_date' in d:
            o.snapshot_date = d['snapshot_date']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        return o


