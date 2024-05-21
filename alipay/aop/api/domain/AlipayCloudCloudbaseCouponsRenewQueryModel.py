#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseCouponsRenewQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._purchase_month = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def purchase_month(self):
        return self._purchase_month

    @purchase_month.setter
    def purchase_month(self, value):
        self._purchase_month = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.purchase_month:
            if hasattr(self.purchase_month, 'to_alipay_dict'):
                params['purchase_month'] = self.purchase_month.to_alipay_dict()
            else:
                params['purchase_month'] = self.purchase_month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseCouponsRenewQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'purchase_month' in d:
            o.purchase_month = d['purchase_month']
        return o


