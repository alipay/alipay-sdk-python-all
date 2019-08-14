#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPayAssetBaseVO import CreditPayAssetBaseVO
from alipay.aop.api.domain.CreditPayInstallmentDetailVO import CreditPayInstallmentDetailVO


class CreditPayInstallmentAssetVO(object):

    def __init__(self):
        self._base_info = None
        self._installment_details = None

    @property
    def base_info(self):
        return self._base_info

    @base_info.setter
    def base_info(self, value):
        if isinstance(value, CreditPayAssetBaseVO):
            self._base_info = value
        else:
            self._base_info = CreditPayAssetBaseVO.from_alipay_dict(value)
    @property
    def installment_details(self):
        return self._installment_details

    @installment_details.setter
    def installment_details(self, value):
        if isinstance(value, list):
            self._installment_details = list()
            for i in value:
                if isinstance(i, CreditPayInstallmentDetailVO):
                    self._installment_details.append(i)
                else:
                    self._installment_details.append(CreditPayInstallmentDetailVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.base_info:
            if hasattr(self.base_info, 'to_alipay_dict'):
                params['base_info'] = self.base_info.to_alipay_dict()
            else:
                params['base_info'] = self.base_info
        if self.installment_details:
            if isinstance(self.installment_details, list):
                for i in range(0, len(self.installment_details)):
                    element = self.installment_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.installment_details[i] = element.to_alipay_dict()
            if hasattr(self.installment_details, 'to_alipay_dict'):
                params['installment_details'] = self.installment_details.to_alipay_dict()
            else:
                params['installment_details'] = self.installment_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPayInstallmentAssetVO()
        if 'base_info' in d:
            o.base_info = d['base_info']
        if 'installment_details' in d:
            o.installment_details = d['installment_details']
        return o


