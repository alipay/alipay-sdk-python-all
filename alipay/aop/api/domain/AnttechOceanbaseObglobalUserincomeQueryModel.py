#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalUserincomeQueryModel(object):

    def __init__(self):
        self._cloud_provider = None
        self._passport_id = None
        self._platform_id = None
        self._platform_ids = None
        self._sale_channel = None
        self._year = None

    @property
    def cloud_provider(self):
        return self._cloud_provider

    @cloud_provider.setter
    def cloud_provider(self, value):
        self._cloud_provider = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def platform_id(self):
        return self._platform_id

    @platform_id.setter
    def platform_id(self, value):
        self._platform_id = value
    @property
    def platform_ids(self):
        return self._platform_ids

    @platform_ids.setter
    def platform_ids(self, value):
        if isinstance(value, list):
            self._platform_ids = list()
            for i in value:
                self._platform_ids.append(i)
    @property
    def sale_channel(self):
        return self._sale_channel

    @sale_channel.setter
    def sale_channel(self, value):
        self._sale_channel = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.cloud_provider:
            if hasattr(self.cloud_provider, 'to_alipay_dict'):
                params['cloud_provider'] = self.cloud_provider.to_alipay_dict()
            else:
                params['cloud_provider'] = self.cloud_provider
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.platform_id:
            if hasattr(self.platform_id, 'to_alipay_dict'):
                params['platform_id'] = self.platform_id.to_alipay_dict()
            else:
                params['platform_id'] = self.platform_id
        if self.platform_ids:
            if isinstance(self.platform_ids, list):
                for i in range(0, len(self.platform_ids)):
                    element = self.platform_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.platform_ids[i] = element.to_alipay_dict()
            if hasattr(self.platform_ids, 'to_alipay_dict'):
                params['platform_ids'] = self.platform_ids.to_alipay_dict()
            else:
                params['platform_ids'] = self.platform_ids
        if self.sale_channel:
            if hasattr(self.sale_channel, 'to_alipay_dict'):
                params['sale_channel'] = self.sale_channel.to_alipay_dict()
            else:
                params['sale_channel'] = self.sale_channel
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalUserincomeQueryModel()
        if 'cloud_provider' in d:
            o.cloud_provider = d['cloud_provider']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'platform_id' in d:
            o.platform_id = d['platform_id']
        if 'platform_ids' in d:
            o.platform_ids = d['platform_ids']
        if 'sale_channel' in d:
            o.sale_channel = d['sale_channel']
        if 'year' in d:
            o.year = d['year']
        return o


