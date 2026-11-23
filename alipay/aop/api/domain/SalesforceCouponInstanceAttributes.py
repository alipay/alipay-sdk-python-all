#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SalesforceCouponInstanceAttributes(object):

    def __init__(self):
        self._cloud_provider = None
        self._commodity_code = None
        self._instance_level = None
        self._out_instance_id = None
        self._passport_id = None
        self._pay_type = None
        self._related_instance_id = None
        self._sale_channel = None
        self._status = None

    @property
    def cloud_provider(self):
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, value):
        self._cloud_provider = value
    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def instance_level(self):
        return self._instance_level

    @instance_level.setter
    def instance_level(self, value):
        self._instance_level = value
    @property
    def out_instance_id(self):
        return self._out_instance_id

    @out_instance_id.setter
    def out_instance_id(self, value):
        self._out_instance_id = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value):
        self._pay_type = value
    @property
    def related_instance_id(self):
        return self._related_instance_id

    @related_instance_id.setter
    def related_instance_id(self, value):
        self._related_instance_id = value
    @property
    def sale_channel(self):
        return self._sale_channel

    @sale_channel.setter
    def sale_channel(self, value):
        self._sale_channel = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_provider:
            if hasattr(self.cloud_provider, 'to_alipay_dict'):
                params['cloud_provider'] = self.cloud_provider.to_alipay_dict()
            else:
                params['cloud_provider'] = self.cloud_provider
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.instance_level:
            if hasattr(self.instance_level, 'to_alipay_dict'):
                params['instance_level'] = self.instance_level.to_alipay_dict()
            else:
                params['instance_level'] = self.instance_level
        if self.out_instance_id:
            if hasattr(self.out_instance_id, 'to_alipay_dict'):
                params['out_instance_id'] = self.out_instance_id.to_alipay_dict()
            else:
                params['out_instance_id'] = self.out_instance_id
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.pay_type:
            if hasattr(self.pay_type, 'to_alipay_dict'):
                params['pay_type'] = self.pay_type.to_alipay_dict()
            else:
                params['pay_type'] = self.pay_type
        if self.related_instance_id:
            if hasattr(self.related_instance_id, 'to_alipay_dict'):
                params['related_instance_id'] = self.related_instance_id.to_alipay_dict()
            else:
                params['related_instance_id'] = self.related_instance_id
        if self.sale_channel:
            if hasattr(self.sale_channel, 'to_alipay_dict'):
                params['sale_channel'] = self.sale_channel.to_alipay_dict()
            else:
                params['sale_channel'] = self.sale_channel
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SalesforceCouponInstanceAttributes()
        if 'cloud_provider' in d:
            o.cloud_provider = d['cloud_provider']
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'instance_level' in d:
            o.instance_level = d['instance_level']
        if 'out_instance_id' in d:
            o.out_instance_id = d['out_instance_id']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'pay_type' in d:
            o.pay_type = d['pay_type']
        if 'related_instance_id' in d:
            o.related_instance_id = d['related_instance_id']
        if 'sale_channel' in d:
            o.sale_channel = d['sale_channel']
        if 'status' in d:
            o.status = d['status']
        return o


