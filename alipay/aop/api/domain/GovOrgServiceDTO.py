#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GovOrgServiceDTO(object):

    def __init__(self):
        self._channel = None
        self._city_code = None
        self._desc = None
        self._logo = None
        self._name = None
        self._out_service_id = None
        self._run_status = None
        self._supplier = None
        self._url = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def run_status(self):
        return self._run_status

    @run_status.setter
    def run_status(self, value):
        self._run_status = value
    @property
    def supplier(self):
        return self._supplier

    @supplier.setter
    def supplier(self, value):
        self._supplier = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.run_status:
            if hasattr(self.run_status, 'to_alipay_dict'):
                params['run_status'] = self.run_status.to_alipay_dict()
            else:
                params['run_status'] = self.run_status
        if self.supplier:
            if hasattr(self.supplier, 'to_alipay_dict'):
                params['supplier'] = self.supplier.to_alipay_dict()
            else:
                params['supplier'] = self.supplier
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GovOrgServiceDTO()
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'desc' in d:
            o.desc = d['desc']
        if 'logo' in d:
            o.logo = d['logo']
        if 'name' in d:
            o.name = d['name']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'run_status' in d:
            o.run_status = d['run_status']
        if 'supplier' in d:
            o.supplier = d['supplier']
        if 'url' in d:
            o.url = d['url']
        return o


