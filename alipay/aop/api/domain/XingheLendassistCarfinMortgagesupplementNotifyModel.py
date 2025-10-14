#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementFullInfo import AgreementFullInfo


class XingheLendassistCarfinMortgagesupplementNotifyModel(object):

    def __init__(self):
        self._agreement_list = None
        self._apply_no = None
        self._lend_apply_no = None
        self._mortgage_no = None
        self._out_apply_no = None
        self._out_lend_apply_no = None
        self._supple_file_list = None
        self._supplement_list = None

    @property
    def agreement_list(self):
        return self._agreement_list

    @agreement_list.setter
    def agreement_list(self, value):
        if isinstance(value, list):
            self._agreement_list = list()
            for i in value:
                if isinstance(i, AgreementFullInfo):
                    self._agreement_list.append(i)
                else:
                    self._agreement_list.append(AgreementFullInfo.from_alipay_dict(i))
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def lend_apply_no(self):
        return self._lend_apply_no

    @lend_apply_no.setter
    def lend_apply_no(self, value):
        self._lend_apply_no = value
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def out_apply_no(self):
        return self._out_apply_no

    @out_apply_no.setter
    def out_apply_no(self, value):
        self._out_apply_no = value
    @property
    def out_lend_apply_no(self):
        return self._out_lend_apply_no

    @out_lend_apply_no.setter
    def out_lend_apply_no(self, value):
        self._out_lend_apply_no = value
    @property
    def supple_file_list(self):
        return self._supple_file_list

    @supple_file_list.setter
    def supple_file_list(self, value):
        if isinstance(value, list):
            self._supple_file_list = list()
            for i in value:
                self._supple_file_list.append(i)
    @property
    def supplement_list(self):
        return self._supplement_list

    @supplement_list.setter
    def supplement_list(self, value):
        if isinstance(value, list):
            self._supplement_list = list()
            for i in value:
                self._supplement_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_list:
            if isinstance(self.agreement_list, list):
                for i in range(0, len(self.agreement_list)):
                    element = self.agreement_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_list, 'to_alipay_dict'):
                params['agreement_list'] = self.agreement_list.to_alipay_dict()
            else:
                params['agreement_list'] = self.agreement_list
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.lend_apply_no:
            if hasattr(self.lend_apply_no, 'to_alipay_dict'):
                params['lend_apply_no'] = self.lend_apply_no.to_alipay_dict()
            else:
                params['lend_apply_no'] = self.lend_apply_no
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.out_apply_no:
            if hasattr(self.out_apply_no, 'to_alipay_dict'):
                params['out_apply_no'] = self.out_apply_no.to_alipay_dict()
            else:
                params['out_apply_no'] = self.out_apply_no
        if self.out_lend_apply_no:
            if hasattr(self.out_lend_apply_no, 'to_alipay_dict'):
                params['out_lend_apply_no'] = self.out_lend_apply_no.to_alipay_dict()
            else:
                params['out_lend_apply_no'] = self.out_lend_apply_no
        if self.supple_file_list:
            if isinstance(self.supple_file_list, list):
                for i in range(0, len(self.supple_file_list)):
                    element = self.supple_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supple_file_list[i] = element.to_alipay_dict()
            if hasattr(self.supple_file_list, 'to_alipay_dict'):
                params['supple_file_list'] = self.supple_file_list.to_alipay_dict()
            else:
                params['supple_file_list'] = self.supple_file_list
        if self.supplement_list:
            if isinstance(self.supplement_list, list):
                for i in range(0, len(self.supplement_list)):
                    element = self.supplement_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supplement_list[i] = element.to_alipay_dict()
            if hasattr(self.supplement_list, 'to_alipay_dict'):
                params['supplement_list'] = self.supplement_list.to_alipay_dict()
            else:
                params['supplement_list'] = self.supplement_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinMortgagesupplementNotifyModel()
        if 'agreement_list' in d:
            o.agreement_list = d['agreement_list']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'lend_apply_no' in d:
            o.lend_apply_no = d['lend_apply_no']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_lend_apply_no' in d:
            o.out_lend_apply_no = d['out_lend_apply_no']
        if 'supple_file_list' in d:
            o.supple_file_list = d['supple_file_list']
        if 'supplement_list' in d:
            o.supplement_list = d['supplement_list']
        return o


