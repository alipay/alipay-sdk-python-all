#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiSecurityRiskEventSendModel(object):

    def __init__(self):
        self._business_info = None
        self._gmt_occur = None
        self._product = None
        self._request_id = None
        self._scene_code = None

    @property
    def business_info(self):
        return self._business_info

    @business_info.setter
    def business_info(self, value):
        self._business_info = value
    @property
    def gmt_occur(self):
        return self._gmt_occur

    @gmt_occur.setter
    def gmt_occur(self, value):
        self._gmt_occur = value
    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_info:
            if hasattr(self.business_info, 'to_alipay_dict'):
                params['business_info'] = self.business_info.to_alipay_dict()
            else:
                params['business_info'] = self.business_info
        if self.gmt_occur:
            if hasattr(self.gmt_occur, 'to_alipay_dict'):
                params['gmt_occur'] = self.gmt_occur.to_alipay_dict()
            else:
                params['gmt_occur'] = self.gmt_occur
        if self.product:
            if hasattr(self.product, 'to_alipay_dict'):
                params['product'] = self.product.to_alipay_dict()
            else:
                params['product'] = self.product
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
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
        o = KoubeiSecurityRiskEventSendModel()
        if 'business_info' in d:
            o.business_info = d['business_info']
        if 'gmt_occur' in d:
            o.gmt_occur = d['gmt_occur']
        if 'product' in d:
            o.product = d['product']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


