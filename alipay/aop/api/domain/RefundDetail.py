#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundRoyaltyInfo import RefundRoyaltyInfo


class RefundDetail(object):

    def __init__(self):
        self._refund_amount = None
        self._refund_memo = None
        self._refund_royaltys = None
        self._refund_suppl_amount = None
        self._refund_suppl_memo = None
        self._trade_no = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_memo(self):
        return self._refund_memo

    @refund_memo.setter
    def refund_memo(self, value):
        self._refund_memo = value
    @property
    def refund_royaltys(self):
        return self._refund_royaltys

    @refund_royaltys.setter
    def refund_royaltys(self, value):
        if isinstance(value, list):
            self._refund_royaltys = list()
            for i in value:
                if isinstance(i, RefundRoyaltyInfo):
                    self._refund_royaltys.append(i)
                else:
                    self._refund_royaltys.append(RefundRoyaltyInfo.from_alipay_dict(i))
    @property
    def refund_suppl_amount(self):
        return self._refund_suppl_amount

    @refund_suppl_amount.setter
    def refund_suppl_amount(self, value):
        self._refund_suppl_amount = value
    @property
    def refund_suppl_memo(self):
        return self._refund_suppl_memo

    @refund_suppl_memo.setter
    def refund_suppl_memo(self, value):
        self._refund_suppl_memo = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_memo:
            if hasattr(self.refund_memo, 'to_alipay_dict'):
                params['refund_memo'] = self.refund_memo.to_alipay_dict()
            else:
                params['refund_memo'] = self.refund_memo
        if self.refund_royaltys:
            if isinstance(self.refund_royaltys, list):
                for i in range(0, len(self.refund_royaltys)):
                    element = self.refund_royaltys[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_royaltys[i] = element.to_alipay_dict()
            if hasattr(self.refund_royaltys, 'to_alipay_dict'):
                params['refund_royaltys'] = self.refund_royaltys.to_alipay_dict()
            else:
                params['refund_royaltys'] = self.refund_royaltys
        if self.refund_suppl_amount:
            if hasattr(self.refund_suppl_amount, 'to_alipay_dict'):
                params['refund_suppl_amount'] = self.refund_suppl_amount.to_alipay_dict()
            else:
                params['refund_suppl_amount'] = self.refund_suppl_amount
        if self.refund_suppl_memo:
            if hasattr(self.refund_suppl_memo, 'to_alipay_dict'):
                params['refund_suppl_memo'] = self.refund_suppl_memo.to_alipay_dict()
            else:
                params['refund_suppl_memo'] = self.refund_suppl_memo
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundDetail()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_memo' in d:
            o.refund_memo = d['refund_memo']
        if 'refund_royaltys' in d:
            o.refund_royaltys = d['refund_royaltys']
        if 'refund_suppl_amount' in d:
            o.refund_suppl_amount = d['refund_suppl_amount']
        if 'refund_suppl_memo' in d:
            o.refund_suppl_memo = d['refund_suppl_memo']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


