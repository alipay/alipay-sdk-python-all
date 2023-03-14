#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScenePayBusinessParamDTO import ScenePayBusinessParamDTO
from alipay.aop.api.domain.QuotaRuleModelDTO import QuotaRuleModelDTO


class AlipayFundScenepayOrderCreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._business_params = None
        self._identity = None
        self._identity_type = None
        self._out_biz_no = None
        self._product_code = None
        self._quota_rule_list = None
        self._sub_biz_scene = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def business_params(self):
        return self._business_params

    @business_params.setter
    def business_params(self, value):
        if isinstance(value, ScenePayBusinessParamDTO):
            self._business_params = value
        else:
            self._business_params = ScenePayBusinessParamDTO.from_alipay_dict(value)
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def quota_rule_list(self):
        return self._quota_rule_list

    @quota_rule_list.setter
    def quota_rule_list(self, value):
        if isinstance(value, list):
            self._quota_rule_list = list()
            for i in value:
                if isinstance(i, QuotaRuleModelDTO):
                    self._quota_rule_list.append(i)
                else:
                    self._quota_rule_list.append(QuotaRuleModelDTO.from_alipay_dict(i))
    @property
    def sub_biz_scene(self):
        return self._sub_biz_scene

    @sub_biz_scene.setter
    def sub_biz_scene(self, value):
        self._sub_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.business_params:
            if hasattr(self.business_params, 'to_alipay_dict'):
                params['business_params'] = self.business_params.to_alipay_dict()
            else:
                params['business_params'] = self.business_params
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.quota_rule_list:
            if isinstance(self.quota_rule_list, list):
                for i in range(0, len(self.quota_rule_list)):
                    element = self.quota_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quota_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.quota_rule_list, 'to_alipay_dict'):
                params['quota_rule_list'] = self.quota_rule_list.to_alipay_dict()
            else:
                params['quota_rule_list'] = self.quota_rule_list
        if self.sub_biz_scene:
            if hasattr(self.sub_biz_scene, 'to_alipay_dict'):
                params['sub_biz_scene'] = self.sub_biz_scene.to_alipay_dict()
            else:
                params['sub_biz_scene'] = self.sub_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundScenepayOrderCreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'business_params' in d:
            o.business_params = d['business_params']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'quota_rule_list' in d:
            o.quota_rule_list = d['quota_rule_list']
        if 'sub_biz_scene' in d:
            o.sub_biz_scene = d['sub_biz_scene']
        return o


