#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageAlterConsultModel(object):

    def __init__(self):
        self._alter_spec_code = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._coupon_codes = None

    @property
    def alter_spec_code(self):
        return self._alter_spec_code

    @alter_spec_code.setter
    def alter_spec_code(self, value):
        self._alter_spec_code = value
    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def coupon_codes(self):
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, value):
        if isinstance(value, list):
            self._coupon_codes = list()
            for i in value:
                self._coupon_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.alter_spec_code:
            if hasattr(self.alter_spec_code, 'to_alipay_dict'):
                params['alter_spec_code'] = self.alter_spec_code.to_alipay_dict()
            else:
                params['alter_spec_code'] = self.alter_spec_code
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.coupon_codes:
            if isinstance(self.coupon_codes, list):
                for i in range(0, len(self.coupon_codes)):
                    element = self.coupon_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.coupon_codes[i] = element.to_alipay_dict()
            if hasattr(self.coupon_codes, 'to_alipay_dict'):
                params['coupon_codes'] = self.coupon_codes.to_alipay_dict()
            else:
                params['coupon_codes'] = self.coupon_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourcepackageAlterConsultModel()
        if 'alter_spec_code' in d:
            o.alter_spec_code = d['alter_spec_code']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'coupon_codes' in d:
            o.coupon_codes = d['coupon_codes']
        return o


