#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageFrompostpaidCreateandpayModel(object):

    def __init__(self):
        self._auto_renew = None
        self._biz_app_id = None
        self._biz_env_id = None
        self._coupon_codes = None
        self._purchase_month = None
        self._spec_code = None

    @property
    def auto_renew(self):
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, value):
        self._auto_renew = value
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
    @property
    def purchase_month(self):
        return self._purchase_month

    @purchase_month.setter
    def purchase_month(self, value):
        self._purchase_month = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_renew:
            if hasattr(self.auto_renew, 'to_alipay_dict'):
                params['auto_renew'] = self.auto_renew.to_alipay_dict()
            else:
                params['auto_renew'] = self.auto_renew
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
        if self.purchase_month:
            if hasattr(self.purchase_month, 'to_alipay_dict'):
                params['purchase_month'] = self.purchase_month.to_alipay_dict()
            else:
                params['purchase_month'] = self.purchase_month
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseResourcepackageFrompostpaidCreateandpayModel()
        if 'auto_renew' in d:
            o.auto_renew = d['auto_renew']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'coupon_codes' in d:
            o.coupon_codes = d['coupon_codes']
        if 'purchase_month' in d:
            o.purchase_month = d['purchase_month']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


