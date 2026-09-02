#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsTokenPickupNotifyModel(object):

    def __init__(self):
        self._info_token = None
        self._logistics_code = None
        self._match_type = None
        self._pickup_auth_type = None
        self._token_scene = None
        self._waybill_no = None

    @property
    def info_token(self):
        return self._info_token

    @info_token.setter
    def info_token(self, value):
        self._info_token = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def match_type(self):
        return self._match_type

    @match_type.setter
    def match_type(self, value):
        self._match_type = value
    @property
    def pickup_auth_type(self):
        return self._pickup_auth_type

    @pickup_auth_type.setter
    def pickup_auth_type(self, value):
        self._pickup_auth_type = value
    @property
    def token_scene(self):
        return self._token_scene

    @token_scene.setter
    def token_scene(self, value):
        self._token_scene = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.info_token:
            if hasattr(self.info_token, 'to_alipay_dict'):
                params['info_token'] = self.info_token.to_alipay_dict()
            else:
                params['info_token'] = self.info_token
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.match_type:
            if hasattr(self.match_type, 'to_alipay_dict'):
                params['match_type'] = self.match_type.to_alipay_dict()
            else:
                params['match_type'] = self.match_type
        if self.pickup_auth_type:
            if hasattr(self.pickup_auth_type, 'to_alipay_dict'):
                params['pickup_auth_type'] = self.pickup_auth_type.to_alipay_dict()
            else:
                params['pickup_auth_type'] = self.pickup_auth_type
        if self.token_scene:
            if hasattr(self.token_scene, 'to_alipay_dict'):
                params['token_scene'] = self.token_scene.to_alipay_dict()
            else:
                params['token_scene'] = self.token_scene
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsTokenPickupNotifyModel()
        if 'info_token' in d:
            o.info_token = d['info_token']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'match_type' in d:
            o.match_type = d['match_type']
        if 'pickup_auth_type' in d:
            o.pickup_auth_type = d['pickup_auth_type']
        if 'token_scene' in d:
            o.token_scene = d['token_scene']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


