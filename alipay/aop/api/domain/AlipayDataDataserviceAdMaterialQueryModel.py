#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdMaterialQueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._deal_id = None
        self._deal_type = None
        self._material_outer_id = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdMaterialQueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'deal_id' in d:
            o.deal_id = d['deal_id']
        if 'deal_type' in d:
            o.deal_type = d['deal_type']
        if 'material_outer_id' in d:
            o.material_outer_id = d['material_outer_id']
        return o


