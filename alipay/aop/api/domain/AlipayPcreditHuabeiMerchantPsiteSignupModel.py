#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FqNumChargeInfo import FqNumChargeInfo


class AlipayPcreditHuabeiMerchantPsiteSignupModel(object):

    def __init__(self):
        self._fq_num_charge_info = None
        self._max_apply_amt = None
        self._merchant_ids = None
        self._min_apply_amt = None
        self._out_request_no = None
        self._plan_id = None

    @property
    def fq_num_charge_info(self):
        return self._fq_num_charge_info

    @fq_num_charge_info.setter
    def fq_num_charge_info(self, value):
        if isinstance(value, list):
            self._fq_num_charge_info = list()
            for i in value:
                if isinstance(i, FqNumChargeInfo):
                    self._fq_num_charge_info.append(i)
                else:
                    self._fq_num_charge_info.append(FqNumChargeInfo.from_alipay_dict(i))
    @property
    def max_apply_amt(self):
        return self._max_apply_amt

    @max_apply_amt.setter
    def max_apply_amt(self, value):
        self._max_apply_amt = value
    @property
    def merchant_ids(self):
        return self._merchant_ids

    @merchant_ids.setter
    def merchant_ids(self, value):
        if isinstance(value, list):
            self._merchant_ids = list()
            for i in value:
                self._merchant_ids.append(i)
    @property
    def min_apply_amt(self):
        return self._min_apply_amt

    @min_apply_amt.setter
    def min_apply_amt(self, value):
        self._min_apply_amt = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fq_num_charge_info:
            if isinstance(self.fq_num_charge_info, list):
                for i in range(0, len(self.fq_num_charge_info)):
                    element = self.fq_num_charge_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fq_num_charge_info[i] = element.to_alipay_dict()
            if hasattr(self.fq_num_charge_info, 'to_alipay_dict'):
                params['fq_num_charge_info'] = self.fq_num_charge_info.to_alipay_dict()
            else:
                params['fq_num_charge_info'] = self.fq_num_charge_info
        if self.max_apply_amt:
            if hasattr(self.max_apply_amt, 'to_alipay_dict'):
                params['max_apply_amt'] = self.max_apply_amt.to_alipay_dict()
            else:
                params['max_apply_amt'] = self.max_apply_amt
        if self.merchant_ids:
            if isinstance(self.merchant_ids, list):
                for i in range(0, len(self.merchant_ids)):
                    element = self.merchant_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_ids[i] = element.to_alipay_dict()
            if hasattr(self.merchant_ids, 'to_alipay_dict'):
                params['merchant_ids'] = self.merchant_ids.to_alipay_dict()
            else:
                params['merchant_ids'] = self.merchant_ids
        if self.min_apply_amt:
            if hasattr(self.min_apply_amt, 'to_alipay_dict'):
                params['min_apply_amt'] = self.min_apply_amt.to_alipay_dict()
            else:
                params['min_apply_amt'] = self.min_apply_amt
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMerchantPsiteSignupModel()
        if 'fq_num_charge_info' in d:
            o.fq_num_charge_info = d['fq_num_charge_info']
        if 'max_apply_amt' in d:
            o.max_apply_amt = d['max_apply_amt']
        if 'merchant_ids' in d:
            o.merchant_ids = d['merchant_ids']
        if 'min_apply_amt' in d:
            o.min_apply_amt = d['min_apply_amt']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


