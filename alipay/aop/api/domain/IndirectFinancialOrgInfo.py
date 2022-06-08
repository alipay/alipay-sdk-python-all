#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectFinancialOrgInfo(object):

    def __init__(self):
        self._financial_org_cert_img = None
        self._financial_org_type = None

    @property
    def financial_org_cert_img(self):
        return self._financial_org_cert_img

    @financial_org_cert_img.setter
    def financial_org_cert_img(self, value):
        if isinstance(value, list):
            self._financial_org_cert_img = list()
            for i in value:
                self._financial_org_cert_img.append(i)
    @property
    def financial_org_type(self):
        return self._financial_org_type

    @financial_org_type.setter
    def financial_org_type(self, value):
        self._financial_org_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.financial_org_cert_img:
            if isinstance(self.financial_org_cert_img, list):
                for i in range(0, len(self.financial_org_cert_img)):
                    element = self.financial_org_cert_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.financial_org_cert_img[i] = element.to_alipay_dict()
            if hasattr(self.financial_org_cert_img, 'to_alipay_dict'):
                params['financial_org_cert_img'] = self.financial_org_cert_img.to_alipay_dict()
            else:
                params['financial_org_cert_img'] = self.financial_org_cert_img
        if self.financial_org_type:
            if hasattr(self.financial_org_type, 'to_alipay_dict'):
                params['financial_org_type'] = self.financial_org_type.to_alipay_dict()
            else:
                params['financial_org_type'] = self.financial_org_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectFinancialOrgInfo()
        if 'financial_org_cert_img' in d:
            o.financial_org_cert_img = d['financial_org_cert_img']
        if 'financial_org_type' in d:
            o.financial_org_type = d['financial_org_type']
        return o


