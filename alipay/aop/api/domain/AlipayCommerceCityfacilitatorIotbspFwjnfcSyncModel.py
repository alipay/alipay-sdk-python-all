#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorIotbspFwjnfcSyncModel(object):

    def __init__(self):
        self._merchant_app_id = None
        self._nfc_biz_tid = None
        self._nfc_sn = None
        self._open_id = None
        self._params = None
        self._pid = None
        self._query_params = None
        self._route_page = None
        self._upper_biz_tid = None
        self._upper_sn = None
        self._url = None

    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def nfc_biz_tid(self):
        return self._nfc_biz_tid

    @nfc_biz_tid.setter
    def nfc_biz_tid(self, value):
        self._nfc_biz_tid = value
    @property
    def nfc_sn(self):
        return self._nfc_sn

    @nfc_sn.setter
    def nfc_sn(self, value):
        self._nfc_sn = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def query_params(self):
        return self._query_params

    @query_params.setter
    def query_params(self, value):
        self._query_params = value
    @property
    def route_page(self):
        return self._route_page

    @route_page.setter
    def route_page(self, value):
        self._route_page = value
    @property
    def upper_biz_tid(self):
        return self._upper_biz_tid

    @upper_biz_tid.setter
    def upper_biz_tid(self, value):
        self._upper_biz_tid = value
    @property
    def upper_sn(self):
        return self._upper_sn

    @upper_sn.setter
    def upper_sn(self, value):
        self._upper_sn = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_app_id:
            if hasattr(self.merchant_app_id, 'to_alipay_dict'):
                params['merchant_app_id'] = self.merchant_app_id.to_alipay_dict()
            else:
                params['merchant_app_id'] = self.merchant_app_id
        if self.nfc_biz_tid:
            if hasattr(self.nfc_biz_tid, 'to_alipay_dict'):
                params['nfc_biz_tid'] = self.nfc_biz_tid.to_alipay_dict()
            else:
                params['nfc_biz_tid'] = self.nfc_biz_tid
        if self.nfc_sn:
            if hasattr(self.nfc_sn, 'to_alipay_dict'):
                params['nfc_sn'] = self.nfc_sn.to_alipay_dict()
            else:
                params['nfc_sn'] = self.nfc_sn
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.query_params:
            if hasattr(self.query_params, 'to_alipay_dict'):
                params['query_params'] = self.query_params.to_alipay_dict()
            else:
                params['query_params'] = self.query_params
        if self.route_page:
            if hasattr(self.route_page, 'to_alipay_dict'):
                params['route_page'] = self.route_page.to_alipay_dict()
            else:
                params['route_page'] = self.route_page
        if self.upper_biz_tid:
            if hasattr(self.upper_biz_tid, 'to_alipay_dict'):
                params['upper_biz_tid'] = self.upper_biz_tid.to_alipay_dict()
            else:
                params['upper_biz_tid'] = self.upper_biz_tid
        if self.upper_sn:
            if hasattr(self.upper_sn, 'to_alipay_dict'):
                params['upper_sn'] = self.upper_sn.to_alipay_dict()
            else:
                params['upper_sn'] = self.upper_sn
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
        o = AlipayCommerceCityfacilitatorIotbspFwjnfcSyncModel()
        if 'merchant_app_id' in d:
            o.merchant_app_id = d['merchant_app_id']
        if 'nfc_biz_tid' in d:
            o.nfc_biz_tid = d['nfc_biz_tid']
        if 'nfc_sn' in d:
            o.nfc_sn = d['nfc_sn']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'params' in d:
            o.params = d['params']
        if 'pid' in d:
            o.pid = d['pid']
        if 'query_params' in d:
            o.query_params = d['query_params']
        if 'route_page' in d:
            o.route_page = d['route_page']
        if 'upper_biz_tid' in d:
            o.upper_biz_tid = d['upper_biz_tid']
        if 'upper_sn' in d:
            o.upper_sn = d['upper_sn']
        if 'url' in d:
            o.url = d['url']
        return o


