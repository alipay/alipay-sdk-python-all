#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementFile import AgreementFile


class XingheLendassistCarfinFinagreementNotifyModel(object):

    def __init__(self):
        self._agreement_file_list = None
        self._apply_no = None
        self._lend_apply_no = None
        self._out_apply_no = None
        self._out_lend_apply_no = None

    @property
    def agreement_file_list(self):
        return self._agreement_file_list

    @agreement_file_list.setter
    def agreement_file_list(self, value):
        if isinstance(value, list):
            self._agreement_file_list = list()
            for i in value:
                if isinstance(i, AgreementFile):
                    self._agreement_file_list.append(i)
                else:
                    self._agreement_file_list.append(AgreementFile.from_alipay_dict(i))
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


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_file_list:
            if isinstance(self.agreement_file_list, list):
                for i in range(0, len(self.agreement_file_list)):
                    element = self.agreement_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.agreement_file_list[i] = element.to_alipay_dict()
            if hasattr(self.agreement_file_list, 'to_alipay_dict'):
                params['agreement_file_list'] = self.agreement_file_list.to_alipay_dict()
            else:
                params['agreement_file_list'] = self.agreement_file_list
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinFinagreementNotifyModel()
        if 'agreement_file_list' in d:
            o.agreement_file_list = d['agreement_file_list']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'lend_apply_no' in d:
            o.lend_apply_no = d['lend_apply_no']
        if 'out_apply_no' in d:
            o.out_apply_no = d['out_apply_no']
        if 'out_lend_apply_no' in d:
            o.out_lend_apply_no = d['out_lend_apply_no']
        return o


