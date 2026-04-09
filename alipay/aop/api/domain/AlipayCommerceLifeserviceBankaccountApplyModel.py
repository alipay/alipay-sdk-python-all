#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceBankaccountApplyModel(object):

    def __init__(self):
        self._auto_brand_site = None
        self._brand = None
        self._pid = None
        self._site = None

    @property
    def auto_brand_site(self):
        return self._auto_brand_site

    @auto_brand_site.setter
    def auto_brand_site(self, value):
        self._auto_brand_site = value
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value


    def to_alipay_dict(self):
        params = dict()
        if self.auto_brand_site:
            if hasattr(self.auto_brand_site, 'to_alipay_dict'):
                params['auto_brand_site'] = self.auto_brand_site.to_alipay_dict()
            else:
                params['auto_brand_site'] = self.auto_brand_site
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceBankaccountApplyModel()
        if 'auto_brand_site' in d:
            o.auto_brand_site = d['auto_brand_site']
        if 'brand' in d:
            o.brand = d['brand']
        if 'pid' in d:
            o.pid = d['pid']
        if 'site' in d:
            o.site = d['site']
        return o


