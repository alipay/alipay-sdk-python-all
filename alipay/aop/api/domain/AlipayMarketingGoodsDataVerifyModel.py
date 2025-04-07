#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingGoodsDataVerifyModel(object):

    def __init__(self):
        self._action_type = None
        self._biz_no = None
        self._entity_info = None
        self._scene_code = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def entity_info(self):
        return self._entity_info

    @entity_info.setter
    def entity_info(self, value):
        self._entity_info = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.entity_info:
            if hasattr(self.entity_info, 'to_alipay_dict'):
                params['entity_info'] = self.entity_info.to_alipay_dict()
            else:
                params['entity_info'] = self.entity_info
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingGoodsDataVerifyModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'entity_info' in d:
            o.entity_info = d['entity_info']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


