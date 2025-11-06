#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockSecuUserQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._agreement_no_list = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def agreement_no_list(self):
        return self._agreement_no_list

    @agreement_no_list.setter
    def agreement_no_list(self, value):
        if isinstance(value, list):
            self._agreement_no_list = list()
            for i in value:
                self._agreement_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockSecuUserQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'agreement_no_list' in d:
            o.agreement_no_list = d['agreement_no_list']
        return o


