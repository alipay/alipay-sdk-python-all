#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BaseInfoConfig import BaseInfoConfig
from alipay.aop.api.domain.PromiseConfig import PromiseConfig
from alipay.aop.api.domain.RiskConfig import RiskConfig


class ZhimaMerchantCreditserviceDetailModifyModel(object):

    def __init__(self):
        self._base_info_config = None
        self._credit_service_id = None
        self._extra_info = None
        self._promise_config = None
        self._risk_config = None

    @property
    def base_info_config(self):
        return self._base_info_config

    @base_info_config.setter
    def base_info_config(self, value):
        if isinstance(value, BaseInfoConfig):
            self._base_info_config = value
        else:
            self._base_info_config = BaseInfoConfig.from_alipay_dict(value)
    @property
    def credit_service_id(self):
        return self._credit_service_id

    @credit_service_id.setter
    def credit_service_id(self, value):
        self._credit_service_id = value
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        self._extra_info = value
    @property
    def promise_config(self):
        return self._promise_config

    @promise_config.setter
    def promise_config(self, value):
        if isinstance(value, PromiseConfig):
            self._promise_config = value
        else:
            self._promise_config = PromiseConfig.from_alipay_dict(value)
    @property
    def risk_config(self):
        return self._risk_config

    @risk_config.setter
    def risk_config(self, value):
        if isinstance(value, RiskConfig):
            self._risk_config = value
        else:
            self._risk_config = RiskConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.base_info_config:
            if hasattr(self.base_info_config, 'to_alipay_dict'):
                params['base_info_config'] = self.base_info_config.to_alipay_dict()
            else:
                params['base_info_config'] = self.base_info_config
        if self.credit_service_id:
            if hasattr(self.credit_service_id, 'to_alipay_dict'):
                params['credit_service_id'] = self.credit_service_id.to_alipay_dict()
            else:
                params['credit_service_id'] = self.credit_service_id
        if self.extra_info:
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
        if self.promise_config:
            if hasattr(self.promise_config, 'to_alipay_dict'):
                params['promise_config'] = self.promise_config.to_alipay_dict()
            else:
                params['promise_config'] = self.promise_config
        if self.risk_config:
            if hasattr(self.risk_config, 'to_alipay_dict'):
                params['risk_config'] = self.risk_config.to_alipay_dict()
            else:
                params['risk_config'] = self.risk_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaMerchantCreditserviceDetailModifyModel()
        if 'base_info_config' in d:
            o.base_info_config = d['base_info_config']
        if 'credit_service_id' in d:
            o.credit_service_id = d['credit_service_id']
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'promise_config' in d:
            o.promise_config = d['promise_config']
        if 'risk_config' in d:
            o.risk_config = d['risk_config']
        return o


