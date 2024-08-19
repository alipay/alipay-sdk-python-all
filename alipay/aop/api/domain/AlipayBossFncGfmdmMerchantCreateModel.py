#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncGfmdmMerchantCreateModel(object):

    def __init__(self):
        self._cert_no = None
        self._country = None
        self._merchant_id = None
        self._merchant_name = None
        self._merchant_status = None
        self._merchant_type = None
        self._province = None
        self._source = None
        self._source_id = None
        self._source_status = None
        self._tax_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_status(self):
        return self._merchant_status

    @merchant_status.setter
    def merchant_status(self, value):
        self._merchant_status = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def source_status(self):
        return self._source_status

    @source_status.setter
    def source_status(self, value):
        self._source_status = value
    @property
    def tax_id(self):
        return self._tax_id

    @tax_id.setter
    def tax_id(self, value):
        self._tax_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_status:
            if hasattr(self.merchant_status, 'to_alipay_dict'):
                params['merchant_status'] = self.merchant_status.to_alipay_dict()
            else:
                params['merchant_status'] = self.merchant_status
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.source_status:
            if hasattr(self.source_status, 'to_alipay_dict'):
                params['source_status'] = self.source_status.to_alipay_dict()
            else:
                params['source_status'] = self.source_status
        if self.tax_id:
            if hasattr(self.tax_id, 'to_alipay_dict'):
                params['tax_id'] = self.tax_id.to_alipay_dict()
            else:
                params['tax_id'] = self.tax_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfmdmMerchantCreateModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'country' in d:
            o.country = d['country']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_status' in d:
            o.merchant_status = d['merchant_status']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'province' in d:
            o.province = d['province']
        if 'source' in d:
            o.source = d['source']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'source_status' in d:
            o.source_status = d['source_status']
        if 'tax_id' in d:
            o.tax_id = d['tax_id']
        return o


