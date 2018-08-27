#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsUserOrderQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._ext_param = None
        self._merchant_code = None
        self._target_id = None
        self._target_id_type = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def merchant_code(self):
        return self._merchant_code

    @merchant_code.setter
    def merchant_code(self, value):
        self._merchant_code = value
    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, value):
        self._target_id = value
    @property
    def target_id_type(self):
        return self._target_id_type

    @target_id_type.setter
    def target_id_type(self, value):
        self._target_id_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.merchant_code:
            if hasattr(self.merchant_code, 'to_alipay_dict'):
                params['merchant_code'] = self.merchant_code.to_alipay_dict()
            else:
                params['merchant_code'] = self.merchant_code
        if self.target_id:
            if hasattr(self.target_id, 'to_alipay_dict'):
                params['target_id'] = self.target_id.to_alipay_dict()
            else:
                params['target_id'] = self.target_id
        if self.target_id_type:
            if hasattr(self.target_id_type, 'to_alipay_dict'):
                params['target_id_type'] = self.target_id_type.to_alipay_dict()
            else:
                params['target_id_type'] = self.target_id_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsUserOrderQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'merchant_code' in d:
            o.merchant_code = d['merchant_code']
        if 'target_id' in d:
            o.target_id = d['target_id']
        if 'target_id_type' in d:
            o.target_id_type = d['target_id_type']
        return o


