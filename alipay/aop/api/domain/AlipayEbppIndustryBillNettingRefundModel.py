#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryExtendField import IndustryExtendField


class AlipayEbppIndustryBillNettingRefundModel(object):

    def __init__(self):
        self._alipay_bill_no = None
        self._industry_extend_field_list = None
        self._memo = None
        self._netting_amount = None
        self._scene = None

    @property
    def alipay_bill_no(self):
        return self._alipay_bill_no

    @alipay_bill_no.setter
    def alipay_bill_no(self, value):
        self._alipay_bill_no = value
    @property
    def industry_extend_field_list(self):
        return self._industry_extend_field_list

    @industry_extend_field_list.setter
    def industry_extend_field_list(self, value):
        if isinstance(value, list):
            self._industry_extend_field_list = list()
            for i in value:
                if isinstance(i, IndustryExtendField):
                    self._industry_extend_field_list.append(i)
                else:
                    self._industry_extend_field_list.append(IndustryExtendField.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def netting_amount(self):
        return self._netting_amount

    @netting_amount.setter
    def netting_amount(self, value):
        self._netting_amount = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_bill_no:
            if hasattr(self.alipay_bill_no, 'to_alipay_dict'):
                params['alipay_bill_no'] = self.alipay_bill_no.to_alipay_dict()
            else:
                params['alipay_bill_no'] = self.alipay_bill_no
        if self.industry_extend_field_list:
            if isinstance(self.industry_extend_field_list, list):
                for i in range(0, len(self.industry_extend_field_list)):
                    element = self.industry_extend_field_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.industry_extend_field_list[i] = element.to_alipay_dict()
            if hasattr(self.industry_extend_field_list, 'to_alipay_dict'):
                params['industry_extend_field_list'] = self.industry_extend_field_list.to_alipay_dict()
            else:
                params['industry_extend_field_list'] = self.industry_extend_field_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.netting_amount:
            if hasattr(self.netting_amount, 'to_alipay_dict'):
                params['netting_amount'] = self.netting_amount.to_alipay_dict()
            else:
                params['netting_amount'] = self.netting_amount
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryBillNettingRefundModel()
        if 'alipay_bill_no' in d:
            o.alipay_bill_no = d['alipay_bill_no']
        if 'industry_extend_field_list' in d:
            o.industry_extend_field_list = d['industry_extend_field_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'netting_amount' in d:
            o.netting_amount = d['netting_amount']
        if 'scene' in d:
            o.scene = d['scene']
        return o


