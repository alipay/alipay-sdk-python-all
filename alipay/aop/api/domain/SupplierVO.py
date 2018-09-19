#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierVO(object):

    def __init__(self):
        self._biz_status = None
        self._business_desc = None
        self._certificate_desc = None
        self._short_code = None
        self._supplier_id = None
        self._supplier_name = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def business_desc(self):
        return self._business_desc

    @business_desc.setter
    def business_desc(self, value):
        self._business_desc = value
    @property
    def certificate_desc(self):
        return self._certificate_desc

    @certificate_desc.setter
    def certificate_desc(self, value):
        self._certificate_desc = value
    @property
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value):
        self._supplier_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.business_desc:
            if hasattr(self.business_desc, 'to_alipay_dict'):
                params['business_desc'] = self.business_desc.to_alipay_dict()
            else:
                params['business_desc'] = self.business_desc
        if self.certificate_desc:
            if hasattr(self.certificate_desc, 'to_alipay_dict'):
                params['certificate_desc'] = self.certificate_desc.to_alipay_dict()
            else:
                params['certificate_desc'] = self.certificate_desc
        if self.short_code:
            if hasattr(self.short_code, 'to_alipay_dict'):
                params['short_code'] = self.short_code.to_alipay_dict()
            else:
                params['short_code'] = self.short_code
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        if self.supplier_name:
            if hasattr(self.supplier_name, 'to_alipay_dict'):
                params['supplier_name'] = self.supplier_name.to_alipay_dict()
            else:
                params['supplier_name'] = self.supplier_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierVO()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'business_desc' in d:
            o.business_desc = d['business_desc']
        if 'certificate_desc' in d:
            o.certificate_desc = d['certificate_desc']
        if 'short_code' in d:
            o.short_code = d['short_code']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        if 'supplier_name' in d:
            o.supplier_name = d['supplier_name']
        return o


