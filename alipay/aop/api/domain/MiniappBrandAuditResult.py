#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniappBrandAuditResult(object):

    def __init__(self):
        self._brand_id = None
        self._brand_name = None
        self._brand_status = None
        self._has_brand = None
        self._invalid_reason = None
        self._reject_reason = None

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, value):
        self._brand_id = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def brand_status(self):
        return self._brand_status

    @brand_status.setter
    def brand_status(self, value):
        self._brand_status = value
    @property
    def has_brand(self):
        return self._has_brand

    @has_brand.setter
    def has_brand(self, value):
        self._has_brand = value
    @property
    def invalid_reason(self):
        return self._invalid_reason

    @invalid_reason.setter
    def invalid_reason(self, value):
        self._invalid_reason = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_id:
            if hasattr(self.brand_id, 'to_alipay_dict'):
                params['brand_id'] = self.brand_id.to_alipay_dict()
            else:
                params['brand_id'] = self.brand_id
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.brand_status:
            if hasattr(self.brand_status, 'to_alipay_dict'):
                params['brand_status'] = self.brand_status.to_alipay_dict()
            else:
                params['brand_status'] = self.brand_status
        if self.has_brand:
            if hasattr(self.has_brand, 'to_alipay_dict'):
                params['has_brand'] = self.has_brand.to_alipay_dict()
            else:
                params['has_brand'] = self.has_brand
        if self.invalid_reason:
            if hasattr(self.invalid_reason, 'to_alipay_dict'):
                params['invalid_reason'] = self.invalid_reason.to_alipay_dict()
            else:
                params['invalid_reason'] = self.invalid_reason
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniappBrandAuditResult()
        if 'brand_id' in d:
            o.brand_id = d['brand_id']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'brand_status' in d:
            o.brand_status = d['brand_status']
        if 'has_brand' in d:
            o.has_brand = d['has_brand']
        if 'invalid_reason' in d:
            o.invalid_reason = d['invalid_reason']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


