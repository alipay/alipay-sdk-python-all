#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingIotBoothQueryModel(object):

    def __init__(self):
        self._api_version = None
        self._app_info = None
        self._bar_code = None
        self._dynamic_id_type = None
        self._ftoken = None
        self._merchant_plan_id = None
        self._space_code = None
        self._trade_no = None

    @property
    def api_version(self):
        return self._api_version

    @api_version.setter
    def api_version(self, value):
        self._api_version = value
    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        self._app_info = value
    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, value):
        self._bar_code = value
    @property
    def dynamic_id_type(self):
        return self._dynamic_id_type

    @dynamic_id_type.setter
    def dynamic_id_type(self, value):
        self._dynamic_id_type = value
    @property
    def ftoken(self):
        return self._ftoken

    @ftoken.setter
    def ftoken(self, value):
        self._ftoken = value
    @property
    def merchant_plan_id(self):
        return self._merchant_plan_id

    @merchant_plan_id.setter
    def merchant_plan_id(self, value):
        self._merchant_plan_id = value
    @property
    def space_code(self):
        return self._space_code

    @space_code.setter
    def space_code(self, value):
        self._space_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_version:
            if hasattr(self.api_version, 'to_alipay_dict'):
                params['api_version'] = self.api_version.to_alipay_dict()
            else:
                params['api_version'] = self.api_version
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.bar_code:
            if hasattr(self.bar_code, 'to_alipay_dict'):
                params['bar_code'] = self.bar_code.to_alipay_dict()
            else:
                params['bar_code'] = self.bar_code
        if self.dynamic_id_type:
            if hasattr(self.dynamic_id_type, 'to_alipay_dict'):
                params['dynamic_id_type'] = self.dynamic_id_type.to_alipay_dict()
            else:
                params['dynamic_id_type'] = self.dynamic_id_type
        if self.ftoken:
            if hasattr(self.ftoken, 'to_alipay_dict'):
                params['ftoken'] = self.ftoken.to_alipay_dict()
            else:
                params['ftoken'] = self.ftoken
        if self.merchant_plan_id:
            if hasattr(self.merchant_plan_id, 'to_alipay_dict'):
                params['merchant_plan_id'] = self.merchant_plan_id.to_alipay_dict()
            else:
                params['merchant_plan_id'] = self.merchant_plan_id
        if self.space_code:
            if hasattr(self.space_code, 'to_alipay_dict'):
                params['space_code'] = self.space_code.to_alipay_dict()
            else:
                params['space_code'] = self.space_code
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingIotBoothQueryModel()
        if 'api_version' in d:
            o.api_version = d['api_version']
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'bar_code' in d:
            o.bar_code = d['bar_code']
        if 'dynamic_id_type' in d:
            o.dynamic_id_type = d['dynamic_id_type']
        if 'ftoken' in d:
            o.ftoken = d['ftoken']
        if 'merchant_plan_id' in d:
            o.merchant_plan_id = d['merchant_plan_id']
        if 'space_code' in d:
            o.space_code = d['space_code']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


