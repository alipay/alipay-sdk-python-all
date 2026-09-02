#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeductionInfoE import DeductionInfoE
from alipay.aop.api.domain.FlexibleRentInfo import FlexibleRentInfo
from alipay.aop.api.domain.MergeInfoE import MergeInfoE
from alipay.aop.api.domain.SplitInfoE import SplitInfoE


class TradeDetailE(object):

    def __init__(self):
        self._credit_must_pass = None
        self._deduction_info = None
        self._flexible_rent_info = None
        self._merge_info = None
        self._split_info = None

    @property
    def credit_must_pass(self):
        return self._credit_must_pass

    @credit_must_pass.setter
    def credit_must_pass(self, value):
        self._credit_must_pass = value
    @property
    def deduction_info(self):
        return self._deduction_info

    @deduction_info.setter
    def deduction_info(self, value):
        if isinstance(value, DeductionInfoE):
            self._deduction_info = value
        else:
            self._deduction_info = DeductionInfoE.from_alipay_dict(value)
    @property
    def flexible_rent_info(self):
        return self._flexible_rent_info

    @flexible_rent_info.setter
    def flexible_rent_info(self, value):
        if isinstance(value, FlexibleRentInfo):
            self._flexible_rent_info = value
        else:
            self._flexible_rent_info = FlexibleRentInfo.from_alipay_dict(value)
    @property
    def merge_info(self):
        return self._merge_info

    @merge_info.setter
    def merge_info(self, value):
        if isinstance(value, MergeInfoE):
            self._merge_info = value
        else:
            self._merge_info = MergeInfoE.from_alipay_dict(value)
    @property
    def split_info(self):
        return self._split_info

    @split_info.setter
    def split_info(self, value):
        if isinstance(value, SplitInfoE):
            self._split_info = value
        else:
            self._split_info = SplitInfoE.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.credit_must_pass:
            if hasattr(self.credit_must_pass, 'to_alipay_dict'):
                params['credit_must_pass'] = self.credit_must_pass.to_alipay_dict()
            else:
                params['credit_must_pass'] = self.credit_must_pass
        if self.deduction_info:
            if hasattr(self.deduction_info, 'to_alipay_dict'):
                params['deduction_info'] = self.deduction_info.to_alipay_dict()
            else:
                params['deduction_info'] = self.deduction_info
        if self.flexible_rent_info:
            if hasattr(self.flexible_rent_info, 'to_alipay_dict'):
                params['flexible_rent_info'] = self.flexible_rent_info.to_alipay_dict()
            else:
                params['flexible_rent_info'] = self.flexible_rent_info
        if self.merge_info:
            if hasattr(self.merge_info, 'to_alipay_dict'):
                params['merge_info'] = self.merge_info.to_alipay_dict()
            else:
                params['merge_info'] = self.merge_info
        if self.split_info:
            if hasattr(self.split_info, 'to_alipay_dict'):
                params['split_info'] = self.split_info.to_alipay_dict()
            else:
                params['split_info'] = self.split_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeDetailE()
        if 'credit_must_pass' in d:
            o.credit_must_pass = d['credit_must_pass']
        if 'deduction_info' in d:
            o.deduction_info = d['deduction_info']
        if 'flexible_rent_info' in d:
            o.flexible_rent_info = d['flexible_rent_info']
        if 'merge_info' in d:
            o.merge_info = d['merge_info']
        if 'split_info' in d:
            o.split_info = d['split_info']
        return o


