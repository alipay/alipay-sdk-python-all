#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UploadMaterial import UploadMaterial


class AlipayDataDataserviceAdMaterialUploadModel(object):

    def __init__(self):
        self._action_type = None
        self._biz_token = None
        self._deal_id = None
        self._deal_type = None
        self._material_outer_id = None
        self._material_unit = None
        self._template_id = None
        self._upload_type = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def deal_id(self):
        return self._deal_id

    @deal_id.setter
    def deal_id(self, value):
        self._deal_id = value
    @property
    def deal_type(self):
        return self._deal_type

    @deal_type.setter
    def deal_type(self, value):
        self._deal_type = value
    @property
    def material_outer_id(self):
        return self._material_outer_id

    @material_outer_id.setter
    def material_outer_id(self, value):
        self._material_outer_id = value
    @property
    def material_unit(self):
        return self._material_unit

    @material_unit.setter
    def material_unit(self, value):
        if isinstance(value, UploadMaterial):
            self._material_unit = value
        else:
            self._material_unit = UploadMaterial.from_alipay_dict(value)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def upload_type(self):
        return self._upload_type

    @upload_type.setter
    def upload_type(self, value):
        self._upload_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.deal_id:
            if hasattr(self.deal_id, 'to_alipay_dict'):
                params['deal_id'] = self.deal_id.to_alipay_dict()
            else:
                params['deal_id'] = self.deal_id
        if self.deal_type:
            if hasattr(self.deal_type, 'to_alipay_dict'):
                params['deal_type'] = self.deal_type.to_alipay_dict()
            else:
                params['deal_type'] = self.deal_type
        if self.material_outer_id:
            if hasattr(self.material_outer_id, 'to_alipay_dict'):
                params['material_outer_id'] = self.material_outer_id.to_alipay_dict()
            else:
                params['material_outer_id'] = self.material_outer_id
        if self.material_unit:
            if hasattr(self.material_unit, 'to_alipay_dict'):
                params['material_unit'] = self.material_unit.to_alipay_dict()
            else:
                params['material_unit'] = self.material_unit
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.upload_type:
            if hasattr(self.upload_type, 'to_alipay_dict'):
                params['upload_type'] = self.upload_type.to_alipay_dict()
            else:
                params['upload_type'] = self.upload_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdMaterialUploadModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'deal_id' in d:
            o.deal_id = d['deal_id']
        if 'deal_type' in d:
            o.deal_type = d['deal_type']
        if 'material_outer_id' in d:
            o.material_outer_id = d['material_outer_id']
        if 'material_unit' in d:
            o.material_unit = d['material_unit']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'upload_type' in d:
            o.upload_type = d['upload_type']
        return o


