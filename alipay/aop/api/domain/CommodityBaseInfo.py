#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommodityBaseInfo(object):

    def __init__(self):
        self._logo = None
        self._memo = None
        self._name = None
        self._service_url = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommodityBaseInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'memo' in d:
            o.memo = d['memo']
        if 'name' in d:
            o.name = d['name']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


