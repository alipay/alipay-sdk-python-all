#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApeRecommendStrategy import ApeRecommendStrategy


class AlipayDigitalopUcdpApeprojectCreateModel(object):

    def __init__(self):
        self._actual_merchant_id = None
        self._invoker_id = None
        self._merchant_id = None
        self._mini_app_id = None
        self._org_id = None
        self._project_id = None
        self._project_name = None
        self._recommend_strategy = None
        self._template_code = None

    @property
    def actual_merchant_id(self):
        return self._actual_merchant_id

    @actual_merchant_id.setter
    def actual_merchant_id(self, value):
        self._actual_merchant_id = value
    @property
    def invoker_id(self):
        return self._invoker_id

    @invoker_id.setter
    def invoker_id(self, value):
        self._invoker_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def recommend_strategy(self):
        return self._recommend_strategy

    @recommend_strategy.setter
    def recommend_strategy(self, value):
        if isinstance(value, ApeRecommendStrategy):
            self._recommend_strategy = value
        else:
            self._recommend_strategy = ApeRecommendStrategy.from_alipay_dict(value)
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_merchant_id:
            if hasattr(self.actual_merchant_id, 'to_alipay_dict'):
                params['actual_merchant_id'] = self.actual_merchant_id.to_alipay_dict()
            else:
                params['actual_merchant_id'] = self.actual_merchant_id
        if self.invoker_id:
            if hasattr(self.invoker_id, 'to_alipay_dict'):
                params['invoker_id'] = self.invoker_id.to_alipay_dict()
            else:
                params['invoker_id'] = self.invoker_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.recommend_strategy:
            if hasattr(self.recommend_strategy, 'to_alipay_dict'):
                params['recommend_strategy'] = self.recommend_strategy.to_alipay_dict()
            else:
                params['recommend_strategy'] = self.recommend_strategy
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalopUcdpApeprojectCreateModel()
        if 'actual_merchant_id' in d:
            o.actual_merchant_id = d['actual_merchant_id']
        if 'invoker_id' in d:
            o.invoker_id = d['invoker_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'recommend_strategy' in d:
            o.recommend_strategy = d['recommend_strategy']
        if 'template_code' in d:
            o.template_code = d['template_code']
        return o


