#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstCashPoolAccountMappingVO import InstCashPoolAccountMappingVO


class AlipayAccountCashpoolAccountBindModel(object):

    def __init__(self):
        self._cash_pool_account_mapping_vo_list = None
        self._cash_pool_id = None
        self._operator = None

    @property
    def cash_pool_account_mapping_vo_list(self):
        return self._cash_pool_account_mapping_vo_list

    @cash_pool_account_mapping_vo_list.setter
    def cash_pool_account_mapping_vo_list(self, value):
        if isinstance(value, list):
            self._cash_pool_account_mapping_vo_list = list()
            for i in value:
                if isinstance(i, InstCashPoolAccountMappingVO):
                    self._cash_pool_account_mapping_vo_list.append(i)
                else:
                    self._cash_pool_account_mapping_vo_list.append(InstCashPoolAccountMappingVO.from_alipay_dict(i))
    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_account_mapping_vo_list:
            if isinstance(self.cash_pool_account_mapping_vo_list, list):
                for i in range(0, len(self.cash_pool_account_mapping_vo_list)):
                    element = self.cash_pool_account_mapping_vo_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cash_pool_account_mapping_vo_list[i] = element.to_alipay_dict()
            if hasattr(self.cash_pool_account_mapping_vo_list, 'to_alipay_dict'):
                params['cash_pool_account_mapping_vo_list'] = self.cash_pool_account_mapping_vo_list.to_alipay_dict()
            else:
                params['cash_pool_account_mapping_vo_list'] = self.cash_pool_account_mapping_vo_list
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolAccountBindModel()
        if 'cash_pool_account_mapping_vo_list' in d:
            o.cash_pool_account_mapping_vo_list = d['cash_pool_account_mapping_vo_list']
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'operator' in d:
            o.operator = d['operator']
        return o


