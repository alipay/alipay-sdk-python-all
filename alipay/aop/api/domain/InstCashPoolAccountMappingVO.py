#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAccountDTO import InstAccountDTO
from alipay.aop.api.domain.InstAccountDTO import InstAccountDTO


class InstCashPoolAccountMappingVO(object):

    def __init__(self):
        self._cash_pool_id = None
        self._inst_account = None
        self._main_account = None
        self._operator = None
        self._parent_inst_account = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def inst_account(self):
        return self._inst_account

    @inst_account.setter
    def inst_account(self, value):
        if isinstance(value, InstAccountDTO):
            self._inst_account = value
        else:
            self._inst_account = InstAccountDTO.from_alipay_dict(value)
    @property
    def main_account(self):
        return self._main_account

    @main_account.setter
    def main_account(self, value):
        self._main_account = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def parent_inst_account(self):
        return self._parent_inst_account

    @parent_inst_account.setter
    def parent_inst_account(self, value):
        if isinstance(value, InstAccountDTO):
            self._parent_inst_account = value
        else:
            self._parent_inst_account = InstAccountDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.inst_account:
            if hasattr(self.inst_account, 'to_alipay_dict'):
                params['inst_account'] = self.inst_account.to_alipay_dict()
            else:
                params['inst_account'] = self.inst_account
        if self.main_account:
            if hasattr(self.main_account, 'to_alipay_dict'):
                params['main_account'] = self.main_account.to_alipay_dict()
            else:
                params['main_account'] = self.main_account
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.parent_inst_account:
            if hasattr(self.parent_inst_account, 'to_alipay_dict'):
                params['parent_inst_account'] = self.parent_inst_account.to_alipay_dict()
            else:
                params['parent_inst_account'] = self.parent_inst_account
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstCashPoolAccountMappingVO()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'inst_account' in d:
            o.inst_account = d['inst_account']
        if 'main_account' in d:
            o.main_account = d['main_account']
        if 'operator' in d:
            o.operator = d['operator']
        if 'parent_inst_account' in d:
            o.parent_inst_account = d['parent_inst_account']
        return o


