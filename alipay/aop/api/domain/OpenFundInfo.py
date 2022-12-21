#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenBudget import OpenBudget


class OpenFundInfo(object):

    def __init__(self):
        self._budget = None
        self._ceiling_amount = None
        self._display_account = None
        self._fund_account = None
        self._fund_mode = None
        self._fund_provider = None
        self._fund_ratio = None
        self._fund_related_id = None
        self._fund_source_type = None
        self._fund_type = None
        self._item_ceiling_amount = None
        self._item_merchant_subsidy_rounding_mode = None
        self._minitrans_account = None
        self._point_budget_code = None
        self._recharge_freeze_code = None
        self._recharge_type = None
        self._refund_account = None
        self._refund_funding_priority = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, OpenBudget):
            self._budget = value
        else:
            self._budget = OpenBudget.from_alipay_dict(value)
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def display_account(self):
        return self._display_account

    @display_account.setter
    def display_account(self, value):
        self._display_account = value
    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def fund_mode(self):
        return self._fund_mode

    @fund_mode.setter
    def fund_mode(self, value):
        self._fund_mode = value
    @property
    def fund_provider(self):
        return self._fund_provider

    @fund_provider.setter
    def fund_provider(self, value):
        self._fund_provider = value
    @property
    def fund_ratio(self):
        return self._fund_ratio

    @fund_ratio.setter
    def fund_ratio(self, value):
        self._fund_ratio = value
    @property
    def fund_related_id(self):
        return self._fund_related_id

    @fund_related_id.setter
    def fund_related_id(self, value):
        self._fund_related_id = value
    @property
    def fund_source_type(self):
        return self._fund_source_type

    @fund_source_type.setter
    def fund_source_type(self, value):
        self._fund_source_type = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def item_ceiling_amount(self):
        return self._item_ceiling_amount

    @item_ceiling_amount.setter
    def item_ceiling_amount(self, value):
        self._item_ceiling_amount = value
    @property
    def item_merchant_subsidy_rounding_mode(self):
        return self._item_merchant_subsidy_rounding_mode

    @item_merchant_subsidy_rounding_mode.setter
    def item_merchant_subsidy_rounding_mode(self, value):
        self._item_merchant_subsidy_rounding_mode = value
    @property
    def minitrans_account(self):
        return self._minitrans_account

    @minitrans_account.setter
    def minitrans_account(self, value):
        self._minitrans_account = value
    @property
    def point_budget_code(self):
        return self._point_budget_code

    @point_budget_code.setter
    def point_budget_code(self, value):
        self._point_budget_code = value
    @property
    def recharge_freeze_code(self):
        return self._recharge_freeze_code

    @recharge_freeze_code.setter
    def recharge_freeze_code(self, value):
        self._recharge_freeze_code = value
    @property
    def recharge_type(self):
        return self._recharge_type

    @recharge_type.setter
    def recharge_type(self, value):
        self._recharge_type = value
    @property
    def refund_account(self):
        return self._refund_account

    @refund_account.setter
    def refund_account(self, value):
        self._refund_account = value
    @property
    def refund_funding_priority(self):
        return self._refund_funding_priority

    @refund_funding_priority.setter
    def refund_funding_priority(self, value):
        self._refund_funding_priority = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.display_account:
            if hasattr(self.display_account, 'to_alipay_dict'):
                params['display_account'] = self.display_account.to_alipay_dict()
            else:
                params['display_account'] = self.display_account
        if self.fund_account:
            if hasattr(self.fund_account, 'to_alipay_dict'):
                params['fund_account'] = self.fund_account.to_alipay_dict()
            else:
                params['fund_account'] = self.fund_account
        if self.fund_mode:
            if hasattr(self.fund_mode, 'to_alipay_dict'):
                params['fund_mode'] = self.fund_mode.to_alipay_dict()
            else:
                params['fund_mode'] = self.fund_mode
        if self.fund_provider:
            if hasattr(self.fund_provider, 'to_alipay_dict'):
                params['fund_provider'] = self.fund_provider.to_alipay_dict()
            else:
                params['fund_provider'] = self.fund_provider
        if self.fund_ratio:
            if hasattr(self.fund_ratio, 'to_alipay_dict'):
                params['fund_ratio'] = self.fund_ratio.to_alipay_dict()
            else:
                params['fund_ratio'] = self.fund_ratio
        if self.fund_related_id:
            if hasattr(self.fund_related_id, 'to_alipay_dict'):
                params['fund_related_id'] = self.fund_related_id.to_alipay_dict()
            else:
                params['fund_related_id'] = self.fund_related_id
        if self.fund_source_type:
            if hasattr(self.fund_source_type, 'to_alipay_dict'):
                params['fund_source_type'] = self.fund_source_type.to_alipay_dict()
            else:
                params['fund_source_type'] = self.fund_source_type
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.item_ceiling_amount:
            if hasattr(self.item_ceiling_amount, 'to_alipay_dict'):
                params['item_ceiling_amount'] = self.item_ceiling_amount.to_alipay_dict()
            else:
                params['item_ceiling_amount'] = self.item_ceiling_amount
        if self.item_merchant_subsidy_rounding_mode:
            if hasattr(self.item_merchant_subsidy_rounding_mode, 'to_alipay_dict'):
                params['item_merchant_subsidy_rounding_mode'] = self.item_merchant_subsidy_rounding_mode.to_alipay_dict()
            else:
                params['item_merchant_subsidy_rounding_mode'] = self.item_merchant_subsidy_rounding_mode
        if self.minitrans_account:
            if hasattr(self.minitrans_account, 'to_alipay_dict'):
                params['minitrans_account'] = self.minitrans_account.to_alipay_dict()
            else:
                params['minitrans_account'] = self.minitrans_account
        if self.point_budget_code:
            if hasattr(self.point_budget_code, 'to_alipay_dict'):
                params['point_budget_code'] = self.point_budget_code.to_alipay_dict()
            else:
                params['point_budget_code'] = self.point_budget_code
        if self.recharge_freeze_code:
            if hasattr(self.recharge_freeze_code, 'to_alipay_dict'):
                params['recharge_freeze_code'] = self.recharge_freeze_code.to_alipay_dict()
            else:
                params['recharge_freeze_code'] = self.recharge_freeze_code
        if self.recharge_type:
            if hasattr(self.recharge_type, 'to_alipay_dict'):
                params['recharge_type'] = self.recharge_type.to_alipay_dict()
            else:
                params['recharge_type'] = self.recharge_type
        if self.refund_account:
            if hasattr(self.refund_account, 'to_alipay_dict'):
                params['refund_account'] = self.refund_account.to_alipay_dict()
            else:
                params['refund_account'] = self.refund_account
        if self.refund_funding_priority:
            if hasattr(self.refund_funding_priority, 'to_alipay_dict'):
                params['refund_funding_priority'] = self.refund_funding_priority.to_alipay_dict()
            else:
                params['refund_funding_priority'] = self.refund_funding_priority
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenFundInfo()
        if 'budget' in d:
            o.budget = d['budget']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'display_account' in d:
            o.display_account = d['display_account']
        if 'fund_account' in d:
            o.fund_account = d['fund_account']
        if 'fund_mode' in d:
            o.fund_mode = d['fund_mode']
        if 'fund_provider' in d:
            o.fund_provider = d['fund_provider']
        if 'fund_ratio' in d:
            o.fund_ratio = d['fund_ratio']
        if 'fund_related_id' in d:
            o.fund_related_id = d['fund_related_id']
        if 'fund_source_type' in d:
            o.fund_source_type = d['fund_source_type']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'item_ceiling_amount' in d:
            o.item_ceiling_amount = d['item_ceiling_amount']
        if 'item_merchant_subsidy_rounding_mode' in d:
            o.item_merchant_subsidy_rounding_mode = d['item_merchant_subsidy_rounding_mode']
        if 'minitrans_account' in d:
            o.minitrans_account = d['minitrans_account']
        if 'point_budget_code' in d:
            o.point_budget_code = d['point_budget_code']
        if 'recharge_freeze_code' in d:
            o.recharge_freeze_code = d['recharge_freeze_code']
        if 'recharge_type' in d:
            o.recharge_type = d['recharge_type']
        if 'refund_account' in d:
            o.refund_account = d['refund_account']
        if 'refund_funding_priority' in d:
            o.refund_funding_priority = d['refund_funding_priority']
        return o


