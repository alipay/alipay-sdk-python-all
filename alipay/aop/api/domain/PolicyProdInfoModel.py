#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DutyResidueAmount import DutyResidueAmount


class PolicyProdInfoModel(object):

    def __init__(self):
        self._duty_residue_amount_list = None
        self._prod_name = None
        self._prod_no = None

    @property
    def duty_residue_amount_list(self):
        return self._duty_residue_amount_list

    @duty_residue_amount_list.setter
    def duty_residue_amount_list(self, value):
        if isinstance(value, list):
            self._duty_residue_amount_list = list()
            for i in value:
                if isinstance(i, DutyResidueAmount):
                    self._duty_residue_amount_list.append(i)
                else:
                    self._duty_residue_amount_list.append(DutyResidueAmount.from_alipay_dict(i))
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_no(self):
        return self._prod_no

    @prod_no.setter
    def prod_no(self, value):
        self._prod_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.duty_residue_amount_list:
            if isinstance(self.duty_residue_amount_list, list):
                for i in range(0, len(self.duty_residue_amount_list)):
                    element = self.duty_residue_amount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.duty_residue_amount_list[i] = element.to_alipay_dict()
            if hasattr(self.duty_residue_amount_list, 'to_alipay_dict'):
                params['duty_residue_amount_list'] = self.duty_residue_amount_list.to_alipay_dict()
            else:
                params['duty_residue_amount_list'] = self.duty_residue_amount_list
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_no:
            if hasattr(self.prod_no, 'to_alipay_dict'):
                params['prod_no'] = self.prod_no.to_alipay_dict()
            else:
                params['prod_no'] = self.prod_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PolicyProdInfoModel()
        if 'duty_residue_amount_list' in d:
            o.duty_residue_amount_list = d['duty_residue_amount_list']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_no' in d:
            o.prod_no = d['prod_no']
        return o


