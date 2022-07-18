#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaterialField import MaterialField


class AlipayMarketingMaterialCreateModel(object):

    def __init__(self):
        self._material_fields = None
        self._material_name = None
        self._material_spec_id = None
        self._out_biz_no = None

    @property
    def material_fields(self):
        return self._material_fields

    @material_fields.setter
    def material_fields(self, value):
        if isinstance(value, list):
            self._material_fields = list()
            for i in value:
                if isinstance(i, MaterialField):
                    self._material_fields.append(i)
                else:
                    self._material_fields.append(MaterialField.from_alipay_dict(i))
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def material_spec_id(self):
        return self._material_spec_id

    @material_spec_id.setter
    def material_spec_id(self, value):
        self._material_spec_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_fields:
            if isinstance(self.material_fields, list):
                for i in range(0, len(self.material_fields)):
                    element = self.material_fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.material_fields[i] = element.to_alipay_dict()
            if hasattr(self.material_fields, 'to_alipay_dict'):
                params['material_fields'] = self.material_fields.to_alipay_dict()
            else:
                params['material_fields'] = self.material_fields
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.material_spec_id:
            if hasattr(self.material_spec_id, 'to_alipay_dict'):
                params['material_spec_id'] = self.material_spec_id.to_alipay_dict()
            else:
                params['material_spec_id'] = self.material_spec_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingMaterialCreateModel()
        if 'material_fields' in d:
            o.material_fields = d['material_fields']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'material_spec_id' in d:
            o.material_spec_id = d['material_spec_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


