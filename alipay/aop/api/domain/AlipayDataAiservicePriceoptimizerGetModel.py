#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MakePriceAgrs import MakePriceAgrs
from alipay.aop.api.domain.MakePriceAgrs import MakePriceAgrs
from alipay.aop.api.domain.MakePriceCards import MakePriceCards


class AlipayDataAiservicePriceoptimizerGetModel(object):

    def __init__(self):
        self._app_version = None
        self._channel = None
        self._city_code = None
        self._extend_agrs = None
        self._feature_args = None
        self._from = None
        self._merchant_id = None
        self._product_list = None
        self._scene_code = None
        self._service_name = None
        self._trace_id = None
        self._unit_id = None
        self._user_id = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
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
    def extend_agrs(self):
        return self._extend_agrs

    @extend_agrs.setter
    def extend_agrs(self, value):
        if isinstance(value, list):
            self._extend_agrs = list()
            for i in value:
                if isinstance(i, MakePriceAgrs):
                    self._extend_agrs.append(i)
                else:
                    self._extend_agrs.append(MakePriceAgrs.from_alipay_dict(i))
    @property
    def feature_args(self):
        return self._feature_args

    @feature_args.setter
    def feature_args(self, value):
        if isinstance(value, list):
            self._feature_args = list()
            for i in value:
                if isinstance(i, MakePriceAgrs):
                    self._feature_args.append(i)
                else:
                    self._feature_args.append(MakePriceAgrs.from_alipay_dict(i))
    @property
    def from(self):
        return self._from

    @from.setter
    def from(self, value):
        self._from = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def product_list(self):
        return self._product_list

    @product_list.setter
    def product_list(self, value):
        if isinstance(value, list):
            self._product_list = list()
            for i in value:
                if isinstance(i, MakePriceCards):
                    self._product_list.append(i)
                else:
                    self._product_list.append(MakePriceCards.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
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
        if self.extend_agrs:
            if isinstance(self.extend_agrs, list):
                for i in range(0, len(self.extend_agrs)):
                    element = self.extend_agrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extend_agrs[i] = element.to_alipay_dict()
            if hasattr(self.extend_agrs, 'to_alipay_dict'):
                params['extend_agrs'] = self.extend_agrs.to_alipay_dict()
            else:
                params['extend_agrs'] = self.extend_agrs
        if self.feature_args:
            if isinstance(self.feature_args, list):
                for i in range(0, len(self.feature_args)):
                    element = self.feature_args[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feature_args[i] = element.to_alipay_dict()
            if hasattr(self.feature_args, 'to_alipay_dict'):
                params['feature_args'] = self.feature_args.to_alipay_dict()
            else:
                params['feature_args'] = self.feature_args
        if self.from:
            if hasattr(self.from, 'to_alipay_dict'):
                params['from'] = self.from.to_alipay_dict()
            else:
                params['from'] = self.from
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.product_list:
            if isinstance(self.product_list, list):
                for i in range(0, len(self.product_list)):
                    element = self.product_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_list[i] = element.to_alipay_dict()
            if hasattr(self.product_list, 'to_alipay_dict'):
                params['product_list'] = self.product_list.to_alipay_dict()
            else:
                params['product_list'] = self.product_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiservicePriceoptimizerGetModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'extend_agrs' in d:
            o.extend_agrs = d['extend_agrs']
        if 'feature_args' in d:
            o.feature_args = d['feature_args']
        if 'from' in d:
            o.from = d['from']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'product_list' in d:
            o.product_list = d['product_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


