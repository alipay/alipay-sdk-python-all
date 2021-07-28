#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionRefundRoyaltyInfo import TuitionRefundRoyaltyInfo


class RefundPaidDetail(object):

    def __init__(self):
        self._plan_id = None
        self._refund_amount = None
        self._refund_royalty_info_list = None

    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_royalty_info_list(self):
        return self._refund_royalty_info_list

    @refund_royalty_info_list.setter
    def refund_royalty_info_list(self, value):
        if isinstance(value, list):
            self._refund_royalty_info_list = list()
            for i in value:
                if isinstance(i, TuitionRefundRoyaltyInfo):
                    self._refund_royalty_info_list.append(i)
                else:
                    self._refund_royalty_info_list.append(TuitionRefundRoyaltyInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_royalty_info_list:
            if isinstance(self.refund_royalty_info_list, list):
                for i in range(0, len(self.refund_royalty_info_list)):
                    element = self.refund_royalty_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_royalty_info_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_royalty_info_list, 'to_alipay_dict'):
                params['refund_royalty_info_list'] = self.refund_royalty_info_list.to_alipay_dict()
            else:
                params['refund_royalty_info_list'] = self.refund_royalty_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundPaidDetail()
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_royalty_info_list' in d:
            o.refund_royalty_info_list = d['refund_royalty_info_list']
        return o


