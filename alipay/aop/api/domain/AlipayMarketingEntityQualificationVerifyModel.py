#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingEntityQualificationVerifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._entity_id = None
        self._entity_info = None
        self._entity_type = None
        self._fund_scene = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def entity_info(self):
        return self._entity_info

    @entity_info.setter
    def entity_info(self, value):
        self._entity_info = value
    @property
    def entity_type(self):
        return self._entity_type

    @entity_type.setter
    def entity_type(self, value):
        self._entity_type = value
    @property
    def fund_scene(self):
        return self._fund_scene

    @fund_scene.setter
    def fund_scene(self, value):
        self._fund_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.entity_info:
            if hasattr(self.entity_info, 'to_alipay_dict'):
                params['entity_info'] = self.entity_info.to_alipay_dict()
            else:
                params['entity_info'] = self.entity_info
        if self.entity_type:
            if hasattr(self.entity_type, 'to_alipay_dict'):
                params['entity_type'] = self.entity_type.to_alipay_dict()
            else:
                params['entity_type'] = self.entity_type
        if self.fund_scene:
            if hasattr(self.fund_scene, 'to_alipay_dict'):
                params['fund_scene'] = self.fund_scene.to_alipay_dict()
            else:
                params['fund_scene'] = self.fund_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingEntityQualificationVerifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'entity_info' in d:
            o.entity_info = d['entity_info']
        if 'entity_type' in d:
            o.entity_type = d['entity_type']
        if 'fund_scene' in d:
            o.fund_scene = d['fund_scene']
        return o


