#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundAgreementQuotaQueryModel(object):

    def __init__(self):
        self._agreement_no_list = None
        self._biz_scene = None
        self._product_code = None

    @property
    def agreement_no_list(self):
        return self._agreement_no_list

    @agreement_no_list.setter
    def agreement_no_list(self, value):
        if isinstance(value, list):
            self._agreement_no_list = list()
            for i in value:
                self._agreement_no_list.append(i)
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no_list:
            if isinstance(self.agreement_no_list, list):
                for i in range(0, len(self.agreement_no_list)):
                    element = self.agreement_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_no_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_no_list, 'to_alipay_dict'):
                params['agreement_no_list'] = self.agreement_no_list.to_alipay_dict()
            else:
                params['agreement_no_list'] = self.agreement_no_list
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundAgreementQuotaQueryModel()
        if 'agreement_no_list' in d:
            o.agreement_no_list = d['agreement_no_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


