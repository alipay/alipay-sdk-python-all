#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehicleownerBizruleMatchModel(object):

    def __init__(self):
        self._biz_entity = None
        self._biz_type = None

    @property
    def biz_entity(self):
        return self._biz_entity

    @biz_entity.setter
    def biz_entity(self, value):
        self._biz_entity = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_entity:
            if hasattr(self.biz_entity, 'to_alipay_dict'):
                params['biz_entity'] = self.biz_entity.to_alipay_dict()
            else:
                params['biz_entity'] = self.biz_entity
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehicleownerBizruleMatchModel()
        if 'biz_entity' in d:
            o.biz_entity = d['biz_entity']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        return o


