#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo
from alipay.aop.api.domain.TrustEntityInfo import TrustEntityInfo


class AnttechBlockchainFinanceTvpAccountApplyModel(object):

    def __init__(self):
        self._apply_entity = None
        self._product_code = None
        self._request_no = None
        self._scene_entity = None

    @property
    def apply_entity(self):
        return self._apply_entity

    @apply_entity.setter
    def apply_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._apply_entity = value
        else:
            self._apply_entity = TrustEntityInfo.from_alipay_dict(value)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def scene_entity(self):
        return self._scene_entity

    @scene_entity.setter
    def scene_entity(self, value):
        if isinstance(value, TrustEntityInfo):
            self._scene_entity = value
        else:
            self._scene_entity = TrustEntityInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_entity:
            if hasattr(self.apply_entity, 'to_alipay_dict'):
                params['apply_entity'] = self.apply_entity.to_alipay_dict()
            else:
                params['apply_entity'] = self.apply_entity
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.scene_entity:
            if hasattr(self.scene_entity, 'to_alipay_dict'):
                params['scene_entity'] = self.scene_entity.to_alipay_dict()
            else:
                params['scene_entity'] = self.scene_entity
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceTvpAccountApplyModel()
        if 'apply_entity' in d:
            o.apply_entity = d['apply_entity']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'scene_entity' in d:
            o.scene_entity = d['scene_entity']
        return o


