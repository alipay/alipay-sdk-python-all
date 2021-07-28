#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantShopInfo(object):

    def __init__(self):
        self._audit_desc = None
        self._merchant_pid = None
        self._shop_no = None
        self._shop_status = None

    @property
    def audit_desc(self):
        return self._audit_desc

    @audit_desc.setter
    def audit_desc(self, value):
        self._audit_desc = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value
    @property
    def shop_status(self):
        return self._shop_status

    @shop_status.setter
    def shop_status(self, value):
        self._shop_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_desc:
            if hasattr(self.audit_desc, 'to_alipay_dict'):
                params['audit_desc'] = self.audit_desc.to_alipay_dict()
            else:
                params['audit_desc'] = self.audit_desc
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        if self.shop_status:
            if hasattr(self.shop_status, 'to_alipay_dict'):
                params['shop_status'] = self.shop_status.to_alipay_dict()
            else:
                params['shop_status'] = self.shop_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantShopInfo()
        if 'audit_desc' in d:
            o.audit_desc = d['audit_desc']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        if 'shop_status' in d:
            o.shop_status = d['shop_status']
        return o


