#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementQuotaModifyList import AgreementQuotaModifyList


class AlipayFundAgreementQuotaModifyModel(object):

    def __init__(self):
        self._agreement_quota_modify_list = None
        self._biz_scene = None
        self._product_code = None

    @property
    def agreement_quota_modify_list(self):
        return self._agreement_quota_modify_list

    @agreement_quota_modify_list.setter
    def agreement_quota_modify_list(self, value):
        if isinstance(value, list):
            self._agreement_quota_modify_list = list()
            for i in value:
                if isinstance(i, AgreementQuotaModifyList):
                    self._agreement_quota_modify_list.append(i)
                else:
                    self._agreement_quota_modify_list.append(AgreementQuotaModifyList.from_alipay_dict(i))
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
        if self.agreement_quota_modify_list:
            if isinstance(self.agreement_quota_modify_list, list):
                for i in range(0, len(self.agreement_quota_modify_list)):
                    element = self.agreement_quota_modify_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_quota_modify_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_quota_modify_list, 'to_alipay_dict'):
                params['agreement_quota_modify_list'] = self.agreement_quota_modify_list.to_alipay_dict()
            else:
                params['agreement_quota_modify_list'] = self.agreement_quota_modify_list
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
        o = AlipayFundAgreementQuotaModifyModel()
        if 'agreement_quota_modify_list' in d:
            o.agreement_quota_modify_list = d['agreement_quota_modify_list']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


