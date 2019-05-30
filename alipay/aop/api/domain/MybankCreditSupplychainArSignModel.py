#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditSupplychainArSignModel(object):

    def __init__(self):
        self._ar_pd_code = None
        self._request_id = None
        self._shop_id = None
        self._shop_name = None
        self._site = None
        self._site_user_id = None
        self._trade_source = None

    @property
    def ar_pd_code(self):
        return self._ar_pd_code

    @ar_pd_code.setter
    def ar_pd_code(self, value):
        self._ar_pd_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, value):
        self._site = value
    @property
    def site_user_id(self):
        return self._site_user_id

    @site_user_id.setter
    def site_user_id(self, value):
        self._site_user_id = value
    @property
    def trade_source(self):
        return self._trade_source

    @trade_source.setter
    def trade_source(self, value):
        self._trade_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_pd_code:
            if hasattr(self.ar_pd_code, 'to_alipay_dict'):
                params['ar_pd_code'] = self.ar_pd_code.to_alipay_dict()
            else:
                params['ar_pd_code'] = self.ar_pd_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.site:
            if hasattr(self.site, 'to_alipay_dict'):
                params['site'] = self.site.to_alipay_dict()
            else:
                params['site'] = self.site
        if self.site_user_id:
            if hasattr(self.site_user_id, 'to_alipay_dict'):
                params['site_user_id'] = self.site_user_id.to_alipay_dict()
            else:
                params['site_user_id'] = self.site_user_id
        if self.trade_source:
            if hasattr(self.trade_source, 'to_alipay_dict'):
                params['trade_source'] = self.trade_source.to_alipay_dict()
            else:
                params['trade_source'] = self.trade_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainArSignModel()
        if 'ar_pd_code' in d:
            o.ar_pd_code = d['ar_pd_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'site' in d:
            o.site = d['site']
        if 'site_user_id' in d:
            o.site_user_id = d['site_user_id']
        if 'trade_source' in d:
            o.trade_source = d['trade_source']
        return o


