#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportErrorFeature import ReportErrorFeature


class AlipayOfflineMarketReporterrorCreateModel(object):

    def __init__(self):
        self._err_time = None
        self._feature = None
        self._merchant_id = None
        self._shop_id = None
        self._type = None
        self._user_id = None

    @property
    def err_time(self):
        return self._err_time

    @err_time.setter
    def err_time(self, value):
        self._err_time = value
    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        if isinstance(value, ReportErrorFeature):
            self._feature = value
        else:
            self._feature = ReportErrorFeature.from_alipay_dict(value)
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.err_time:
            if hasattr(self.err_time, 'to_alipay_dict'):
                params['err_time'] = self.err_time.to_alipay_dict()
            else:
                params['err_time'] = self.err_time
        if self.feature:
            if hasattr(self.feature, 'to_alipay_dict'):
                params['feature'] = self.feature.to_alipay_dict()
            else:
                params['feature'] = self.feature
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = AlipayOfflineMarketReporterrorCreateModel()
        if 'err_time' in d:
            o.err_time = d['err_time']
        if 'feature' in d:
            o.feature = d['feature']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


