#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsLinkGetModel(object):

    def __init__(self):
        self._logistics_biz_scene_action = None
        self._merchant_request_source = None
        self._merchant_station_code = None
        self._merchant_station_expressman_id = None
        self._merchant_station_name = None
        self._merchant_station_shop_id = None

    @property
    def logistics_biz_scene_action(self):
        return self._logistics_biz_scene_action

    @logistics_biz_scene_action.setter
    def logistics_biz_scene_action(self, value):
        self._logistics_biz_scene_action = value
    @property
    def merchant_request_source(self):
        return self._merchant_request_source

    @merchant_request_source.setter
    def merchant_request_source(self, value):
        self._merchant_request_source = value
    @property
    def merchant_station_code(self):
        return self._merchant_station_code

    @merchant_station_code.setter
    def merchant_station_code(self, value):
        self._merchant_station_code = value
    @property
    def merchant_station_expressman_id(self):
        return self._merchant_station_expressman_id

    @merchant_station_expressman_id.setter
    def merchant_station_expressman_id(self, value):
        self._merchant_station_expressman_id = value
    @property
    def merchant_station_name(self):
        return self._merchant_station_name

    @merchant_station_name.setter
    def merchant_station_name(self, value):
        self._merchant_station_name = value
    @property
    def merchant_station_shop_id(self):
        return self._merchant_station_shop_id

    @merchant_station_shop_id.setter
    def merchant_station_shop_id(self, value):
        self._merchant_station_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_biz_scene_action:
            if hasattr(self.logistics_biz_scene_action, 'to_alipay_dict'):
                params['logistics_biz_scene_action'] = self.logistics_biz_scene_action.to_alipay_dict()
            else:
                params['logistics_biz_scene_action'] = self.logistics_biz_scene_action
        if self.merchant_request_source:
            if hasattr(self.merchant_request_source, 'to_alipay_dict'):
                params['merchant_request_source'] = self.merchant_request_source.to_alipay_dict()
            else:
                params['merchant_request_source'] = self.merchant_request_source
        if self.merchant_station_code:
            if hasattr(self.merchant_station_code, 'to_alipay_dict'):
                params['merchant_station_code'] = self.merchant_station_code.to_alipay_dict()
            else:
                params['merchant_station_code'] = self.merchant_station_code
        if self.merchant_station_expressman_id:
            if hasattr(self.merchant_station_expressman_id, 'to_alipay_dict'):
                params['merchant_station_expressman_id'] = self.merchant_station_expressman_id.to_alipay_dict()
            else:
                params['merchant_station_expressman_id'] = self.merchant_station_expressman_id
        if self.merchant_station_name:
            if hasattr(self.merchant_station_name, 'to_alipay_dict'):
                params['merchant_station_name'] = self.merchant_station_name.to_alipay_dict()
            else:
                params['merchant_station_name'] = self.merchant_station_name
        if self.merchant_station_shop_id:
            if hasattr(self.merchant_station_shop_id, 'to_alipay_dict'):
                params['merchant_station_shop_id'] = self.merchant_station_shop_id.to_alipay_dict()
            else:
                params['merchant_station_shop_id'] = self.merchant_station_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsLinkGetModel()
        if 'logistics_biz_scene_action' in d:
            o.logistics_biz_scene_action = d['logistics_biz_scene_action']
        if 'merchant_request_source' in d:
            o.merchant_request_source = d['merchant_request_source']
        if 'merchant_station_code' in d:
            o.merchant_station_code = d['merchant_station_code']
        if 'merchant_station_expressman_id' in d:
            o.merchant_station_expressman_id = d['merchant_station_expressman_id']
        if 'merchant_station_name' in d:
            o.merchant_station_name = d['merchant_station_name']
        if 'merchant_station_shop_id' in d:
            o.merchant_station_shop_id = d['merchant_station_shop_id']
        return o


