#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJfexportInputfieldQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._charge_inst = None
        self._extend_field = None
        self._field_scene = None
        self._sub_biz_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def field_scene(self):
        return self._field_scene

    @field_scene.setter
    def field_scene(self, value):
        self._field_scene = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.field_scene:
            if hasattr(self.field_scene, 'to_alipay_dict'):
                params['field_scene'] = self.field_scene.to_alipay_dict()
            else:
                params['field_scene'] = self.field_scene
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJfexportInputfieldQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'field_scene' in d:
            o.field_scene = d['field_scene']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        return o


