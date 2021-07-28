#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PurchaseApplyInfoDTO(object):

    def __init__(self):
        self._account_code = None
        self._begin_cycle = None
        self._biz_budget_apply_code = None
        self._biz_budget_id = None
        self._biz_type = None
        self._budget_strategy = None
        self._currency = None
        self._end_cycle = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._pool_code = None
        self._remain_amount = None
        self._status = None
        self._use = None

    @property
    def account_code(self):
        return self._account_code

    @account_code.setter
    def account_code(self, value):
        self._account_code = value
    @property
    def begin_cycle(self):
        return self._begin_cycle

    @begin_cycle.setter
    def begin_cycle(self, value):
        self._begin_cycle = value
    @property
    def biz_budget_apply_code(self):
        return self._biz_budget_apply_code

    @biz_budget_apply_code.setter
    def biz_budget_apply_code(self, value):
        self._biz_budget_apply_code = value
    @property
    def biz_budget_id(self):
        return self._biz_budget_id

    @biz_budget_id.setter
    def biz_budget_id(self, value):
        self._biz_budget_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def budget_strategy(self):
        return self._budget_strategy

    @budget_strategy.setter
    def budget_strategy(self, value):
        self._budget_strategy = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def end_cycle(self):
        return self._end_cycle

    @end_cycle.setter
    def end_cycle(self, value):
        self._end_cycle = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def pool_code(self):
        return self._pool_code

    @pool_code.setter
    def pool_code(self, value):
        self._pool_code = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use(self):
        return self._use

    @use.setter
    def use(self, value):
        self._use = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_code:
            if hasattr(self.account_code, 'to_alipay_dict'):
                params['account_code'] = self.account_code.to_alipay_dict()
            else:
                params['account_code'] = self.account_code
        if self.begin_cycle:
            if hasattr(self.begin_cycle, 'to_alipay_dict'):
                params['begin_cycle'] = self.begin_cycle.to_alipay_dict()
            else:
                params['begin_cycle'] = self.begin_cycle
        if self.biz_budget_apply_code:
            if hasattr(self.biz_budget_apply_code, 'to_alipay_dict'):
                params['biz_budget_apply_code'] = self.biz_budget_apply_code.to_alipay_dict()
            else:
                params['biz_budget_apply_code'] = self.biz_budget_apply_code
        if self.biz_budget_id:
            if hasattr(self.biz_budget_id, 'to_alipay_dict'):
                params['biz_budget_id'] = self.biz_budget_id.to_alipay_dict()
            else:
                params['biz_budget_id'] = self.biz_budget_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.budget_strategy:
            if hasattr(self.budget_strategy, 'to_alipay_dict'):
                params['budget_strategy'] = self.budget_strategy.to_alipay_dict()
            else:
                params['budget_strategy'] = self.budget_strategy
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.end_cycle:
            if hasattr(self.end_cycle, 'to_alipay_dict'):
                params['end_cycle'] = self.end_cycle.to_alipay_dict()
            else:
                params['end_cycle'] = self.end_cycle
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.pool_code:
            if hasattr(self.pool_code, 'to_alipay_dict'):
                params['pool_code'] = self.pool_code.to_alipay_dict()
            else:
                params['pool_code'] = self.pool_code
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.use:
            if hasattr(self.use, 'to_alipay_dict'):
                params['use'] = self.use.to_alipay_dict()
            else:
                params['use'] = self.use
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PurchaseApplyInfoDTO()
        if 'account_code' in d:
            o.account_code = d['account_code']
        if 'begin_cycle' in d:
            o.begin_cycle = d['begin_cycle']
        if 'biz_budget_apply_code' in d:
            o.biz_budget_apply_code = d['biz_budget_apply_code']
        if 'biz_budget_id' in d:
            o.biz_budget_id = d['biz_budget_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'budget_strategy' in d:
            o.budget_strategy = d['budget_strategy']
        if 'currency' in d:
            o.currency = d['currency']
        if 'end_cycle' in d:
            o.end_cycle = d['end_cycle']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'pool_code' in d:
            o.pool_code = d['pool_code']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        if 'status' in d:
            o.status = d['status']
        if 'use' in d:
            o.use = d['use']
        return o


