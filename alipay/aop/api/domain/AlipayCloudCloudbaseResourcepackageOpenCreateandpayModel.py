#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseResourcepackageOpenCreateandpayModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._auto_renew = None
        self._biz_app_id = None
        self._coupon_codes = None
        self._env_description = None
        self._env_name = None
        self._open_id = None
        self._purchase_month = None
        self._region = None
        self._spec_code = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
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
    def coupon_codes(self):
        return self._coupon_codes

    @coupon_codes.setter
    def coupon_codes(self, value):
        if isinstance(value, list):
            self._coupon_codes = list()
            for i in value:
                self._coupon_codes.append(i)
    @property
    def env_description(self):
        return self._env_description

    @env_description.setter
    def env_description(self, value):
        self._env_description = value
    @property
    def env_name(self):
        return self._env_name

    @env_name.setter
    def env_name(self, value):
        self._env_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def purchase_month(self):
        return self._purchase_month

    @purchase_month.setter
    def purchase_month(self, value):
        self._purchase_month = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
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
        if self.env_description:
            if hasattr(self.env_description, 'to_alipay_dict'):
                params['env_description'] = self.env_description.to_alipay_dict()
            else:
                params['env_description'] = self.env_description
        if self.env_name:
            if hasattr(self.env_name, 'to_alipay_dict'):
                params['env_name'] = self.env_name.to_alipay_dict()
            else:
                params['env_name'] = self.env_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.purchase_month:
            if hasattr(self.purchase_month, 'to_alipay_dict'):
                params['purchase_month'] = self.purchase_month.to_alipay_dict()
            else:
                params['purchase_month'] = self.purchase_month
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
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
        o = AlipayCloudCloudbaseResourcepackageOpenCreateandpayModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'auto_renew' in d:
            o.auto_renew = d['auto_renew']
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'coupon_codes' in d:
            o.coupon_codes = d['coupon_codes']
        if 'env_description' in d:
            o.env_description = d['env_description']
        if 'env_name' in d:
            o.env_name = d['env_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'purchase_month' in d:
            o.purchase_month = d['purchase_month']
        if 'region' in d:
            o.region = d['region']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


