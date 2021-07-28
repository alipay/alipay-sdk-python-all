#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenifitGoodsInfo import BenifitGoodsInfo


class UseDetail(object):

    def __init__(self):
        self._actual_amount = None
        self._amount = None
        self._date = None
        self._goods_info = None

    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, BenifitGoodsInfo):
            self._goods_info = value
        else:
            self._goods_info = BenifitGoodsInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.goods_info:
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UseDetail()
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'date' in d:
            o.date = d['date']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        return o


