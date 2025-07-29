#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdentitylibraryServiceentityQueryModel(object):

    def __init__(self):
        self._goods_id = None
        self._market_target_code = None
        self._principal_id = None
        self._principal_tag = None
        self._service_entity_out_source = None
        self._service_entity_type = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def market_target_code(self):
        return self._market_target_code

    @market_target_code.setter
    def market_target_code(self, value):
        self._market_target_code = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value
    @property
    def service_entity_out_source(self):
        return self._service_entity_out_source

    @service_entity_out_source.setter
    def service_entity_out_source(self, value):
        self._service_entity_out_source = value
    @property
    def service_entity_type(self):
        return self._service_entity_type

    @service_entity_type.setter
    def service_entity_type(self, value):
        self._service_entity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.market_target_code:
            if hasattr(self.market_target_code, 'to_alipay_dict'):
                params['market_target_code'] = self.market_target_code.to_alipay_dict()
            else:
                params['market_target_code'] = self.market_target_code
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        if self.service_entity_out_source:
            if hasattr(self.service_entity_out_source, 'to_alipay_dict'):
                params['service_entity_out_source'] = self.service_entity_out_source.to_alipay_dict()
            else:
                params['service_entity_out_source'] = self.service_entity_out_source
        if self.service_entity_type:
            if hasattr(self.service_entity_type, 'to_alipay_dict'):
                params['service_entity_type'] = self.service_entity_type.to_alipay_dict()
            else:
                params['service_entity_type'] = self.service_entity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdentitylibraryServiceentityQueryModel()
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'market_target_code' in d:
            o.market_target_code = d['market_target_code']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        if 'service_entity_out_source' in d:
            o.service_entity_out_source = d['service_entity_out_source']
        if 'service_entity_type' in d:
            o.service_entity_type = d['service_entity_type']
        return o


