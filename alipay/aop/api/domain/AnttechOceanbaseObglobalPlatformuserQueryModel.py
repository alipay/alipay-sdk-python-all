#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalPlatformuserQueryModel(object):

    def __init__(self):
        self._cid = None
        self._cloud_provider = None
        self._customer_name = None
        self._passport_id = None
        self._sale_channel = None

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def cloud_provider(self):
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, value):
        self._cloud_provider = value
    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def sale_channel(self):
        return self._sale_channel

    @sale_channel.setter
    def sale_channel(self, value):
        self._sale_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.cloud_provider:
            if hasattr(self.cloud_provider, 'to_alipay_dict'):
                params['cloud_provider'] = self.cloud_provider.to_alipay_dict()
            else:
                params['cloud_provider'] = self.cloud_provider
        if self.customer_name:
            if hasattr(self.customer_name, 'to_alipay_dict'):
                params['customer_name'] = self.customer_name.to_alipay_dict()
            else:
                params['customer_name'] = self.customer_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.sale_channel:
            if hasattr(self.sale_channel, 'to_alipay_dict'):
                params['sale_channel'] = self.sale_channel.to_alipay_dict()
            else:
                params['sale_channel'] = self.sale_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalPlatformuserQueryModel()
        if 'cid' in d:
            o.cid = d['cid']
        if 'cloud_provider' in d:
            o.cloud_provider = d['cloud_provider']
        if 'customer_name' in d:
            o.customer_name = d['customer_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'sale_channel' in d:
            o.sale_channel = d['sale_channel']
        return o


