#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentAftersaleFundItemVO import RentAftersaleFundItemVO


class RentAftersaleFundInfoVO(object):

    def __init__(self):
        self._fund_item_list = None
        self._total_amount = None

    @property
    def fund_item_list(self):
        return self._fund_item_list

    @fund_item_list.setter
    def fund_item_list(self, value):
        if isinstance(value, list):
            self._fund_item_list = list()
            for i in value:
                if isinstance(i, RentAftersaleFundItemVO):
                    self._fund_item_list.append(i)
                else:
                    self._fund_item_list.append(RentAftersaleFundItemVO.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_item_list:
            if isinstance(self.fund_item_list, list):
                for i in range(0, len(self.fund_item_list)):
                    element = self.fund_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_item_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_item_list, 'to_alipay_dict'):
                params['fund_item_list'] = self.fund_item_list.to_alipay_dict()
            else:
                params['fund_item_list'] = self.fund_item_list
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentAftersaleFundInfoVO()
        if 'fund_item_list' in d:
            o.fund_item_list = d['fund_item_list']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


