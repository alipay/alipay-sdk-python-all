#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanPayInstallment(object):

    def __init__(self):
        self._base_element = None
        self._details_element = None
        self._extends_element = None
        self._installment_id = None

    @property
    def base_element(self):
        return self._base_element

    @base_element.setter
    def base_element(self, value):
        self._base_element = value
    @property
    def details_element(self):
        return self._details_element

    @details_element.setter
    def details_element(self, value):
        self._details_element = value
    @property
    def extends_element(self):
        return self._extends_element

    @extends_element.setter
    def extends_element(self, value):
        self._extends_element = value
    @property
    def installment_id(self):
        return self._installment_id

    @installment_id.setter
    def installment_id(self, value):
        self._installment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_element:
            if hasattr(self.base_element, 'to_alipay_dict'):
                params['base_element'] = self.base_element.to_alipay_dict()
            else:
                params['base_element'] = self.base_element
        if self.details_element:
            if hasattr(self.details_element, 'to_alipay_dict'):
                params['details_element'] = self.details_element.to_alipay_dict()
            else:
                params['details_element'] = self.details_element
        if self.extends_element:
            if hasattr(self.extends_element, 'to_alipay_dict'):
                params['extends_element'] = self.extends_element.to_alipay_dict()
            else:
                params['extends_element'] = self.extends_element
        if self.installment_id:
            if hasattr(self.installment_id, 'to_alipay_dict'):
                params['installment_id'] = self.installment_id.to_alipay_dict()
            else:
                params['installment_id'] = self.installment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanPayInstallment()
        if 'base_element' in d:
            o.base_element = d['base_element']
        if 'details_element' in d:
            o.details_element = d['details_element']
        if 'extends_element' in d:
            o.extends_element = d['extends_element']
        if 'installment_id' in d:
            o.installment_id = d['installment_id']
        return o


