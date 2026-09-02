#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoanCostDisclosureInfo(object):

    def __init__(self):
        self._capped = None
        self._cost_rate = None
        self._guarantee_fee_org_name = None
        self._guarantee_fee_rate = None
        self._guarantee_fee_rate_type = None
        self._guarantee_fee_repay_mode = None
        self._loan_interest_org_name = None
        self._loan_interest_rate = None
        self._loan_interest_rate_type = None
        self._loan_interest_repay_mode = None
        self._misappropriation_penalty_interest_org_name = None
        self._misappropriation_penalty_interest_text = None
        self._other_fee_org_name = None
        self._other_fee_text = None
        self._overdue_penalty_interest_org_name = None
        self._overdue_penalty_interest_text = None
        self._prepayment_penalty_name = None
        self._prepayment_penalty_org_name = None
        self._prepayment_penalty_text = None

    @property
    def capped(self):
        return self._capped

    @capped.setter
    def capped(self, value):
        self._capped = value
    @property
    def cost_rate(self):
        return self._cost_rate

    @cost_rate.setter
    def cost_rate(self, value):
        self._cost_rate = value
    @property
    def guarantee_fee_org_name(self):
        return self._guarantee_fee_org_name

    @guarantee_fee_org_name.setter
    def guarantee_fee_org_name(self, value):
        self._guarantee_fee_org_name = value
    @property
    def guarantee_fee_rate(self):
        return self._guarantee_fee_rate

    @guarantee_fee_rate.setter
    def guarantee_fee_rate(self, value):
        self._guarantee_fee_rate = value
    @property
    def guarantee_fee_rate_type(self):
        return self._guarantee_fee_rate_type

    @guarantee_fee_rate_type.setter
    def guarantee_fee_rate_type(self, value):
        self._guarantee_fee_rate_type = value
    @property
    def guarantee_fee_repay_mode(self):
        return self._guarantee_fee_repay_mode

    @guarantee_fee_repay_mode.setter
    def guarantee_fee_repay_mode(self, value):
        self._guarantee_fee_repay_mode = value
    @property
    def loan_interest_org_name(self):
        return self._loan_interest_org_name

    @loan_interest_org_name.setter
    def loan_interest_org_name(self, value):
        self._loan_interest_org_name = value
    @property
    def loan_interest_rate(self):
        return self._loan_interest_rate

    @loan_interest_rate.setter
    def loan_interest_rate(self, value):
        self._loan_interest_rate = value
    @property
    def loan_interest_rate_type(self):
        return self._loan_interest_rate_type

    @loan_interest_rate_type.setter
    def loan_interest_rate_type(self, value):
        self._loan_interest_rate_type = value
    @property
    def loan_interest_repay_mode(self):
        return self._loan_interest_repay_mode

    @loan_interest_repay_mode.setter
    def loan_interest_repay_mode(self, value):
        self._loan_interest_repay_mode = value
    @property
    def misappropriation_penalty_interest_org_name(self):
        return self._misappropriation_penalty_interest_org_name

    @misappropriation_penalty_interest_org_name.setter
    def misappropriation_penalty_interest_org_name(self, value):
        self._misappropriation_penalty_interest_org_name = value
    @property
    def misappropriation_penalty_interest_text(self):
        return self._misappropriation_penalty_interest_text

    @misappropriation_penalty_interest_text.setter
    def misappropriation_penalty_interest_text(self, value):
        self._misappropriation_penalty_interest_text = value
    @property
    def other_fee_org_name(self):
        return self._other_fee_org_name

    @other_fee_org_name.setter
    def other_fee_org_name(self, value):
        self._other_fee_org_name = value
    @property
    def other_fee_text(self):
        return self._other_fee_text

    @other_fee_text.setter
    def other_fee_text(self, value):
        self._other_fee_text = value
    @property
    def overdue_penalty_interest_org_name(self):
        return self._overdue_penalty_interest_org_name

    @overdue_penalty_interest_org_name.setter
    def overdue_penalty_interest_org_name(self, value):
        self._overdue_penalty_interest_org_name = value
    @property
    def overdue_penalty_interest_text(self):
        return self._overdue_penalty_interest_text

    @overdue_penalty_interest_text.setter
    def overdue_penalty_interest_text(self, value):
        self._overdue_penalty_interest_text = value
    @property
    def prepayment_penalty_name(self):
        return self._prepayment_penalty_name

    @prepayment_penalty_name.setter
    def prepayment_penalty_name(self, value):
        self._prepayment_penalty_name = value
    @property
    def prepayment_penalty_org_name(self):
        return self._prepayment_penalty_org_name

    @prepayment_penalty_org_name.setter
    def prepayment_penalty_org_name(self, value):
        self._prepayment_penalty_org_name = value
    @property
    def prepayment_penalty_text(self):
        return self._prepayment_penalty_text

    @prepayment_penalty_text.setter
    def prepayment_penalty_text(self, value):
        self._prepayment_penalty_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.capped:
            if hasattr(self.capped, 'to_alipay_dict'):
                params['capped'] = self.capped.to_alipay_dict()
            else:
                params['capped'] = self.capped
        if self.cost_rate:
            if hasattr(self.cost_rate, 'to_alipay_dict'):
                params['cost_rate'] = self.cost_rate.to_alipay_dict()
            else:
                params['cost_rate'] = self.cost_rate
        if self.guarantee_fee_org_name:
            if hasattr(self.guarantee_fee_org_name, 'to_alipay_dict'):
                params['guarantee_fee_org_name'] = self.guarantee_fee_org_name.to_alipay_dict()
            else:
                params['guarantee_fee_org_name'] = self.guarantee_fee_org_name
        if self.guarantee_fee_rate:
            if hasattr(self.guarantee_fee_rate, 'to_alipay_dict'):
                params['guarantee_fee_rate'] = self.guarantee_fee_rate.to_alipay_dict()
            else:
                params['guarantee_fee_rate'] = self.guarantee_fee_rate
        if self.guarantee_fee_rate_type:
            if hasattr(self.guarantee_fee_rate_type, 'to_alipay_dict'):
                params['guarantee_fee_rate_type'] = self.guarantee_fee_rate_type.to_alipay_dict()
            else:
                params['guarantee_fee_rate_type'] = self.guarantee_fee_rate_type
        if self.guarantee_fee_repay_mode:
            if hasattr(self.guarantee_fee_repay_mode, 'to_alipay_dict'):
                params['guarantee_fee_repay_mode'] = self.guarantee_fee_repay_mode.to_alipay_dict()
            else:
                params['guarantee_fee_repay_mode'] = self.guarantee_fee_repay_mode
        if self.loan_interest_org_name:
            if hasattr(self.loan_interest_org_name, 'to_alipay_dict'):
                params['loan_interest_org_name'] = self.loan_interest_org_name.to_alipay_dict()
            else:
                params['loan_interest_org_name'] = self.loan_interest_org_name
        if self.loan_interest_rate:
            if hasattr(self.loan_interest_rate, 'to_alipay_dict'):
                params['loan_interest_rate'] = self.loan_interest_rate.to_alipay_dict()
            else:
                params['loan_interest_rate'] = self.loan_interest_rate
        if self.loan_interest_rate_type:
            if hasattr(self.loan_interest_rate_type, 'to_alipay_dict'):
                params['loan_interest_rate_type'] = self.loan_interest_rate_type.to_alipay_dict()
            else:
                params['loan_interest_rate_type'] = self.loan_interest_rate_type
        if self.loan_interest_repay_mode:
            if hasattr(self.loan_interest_repay_mode, 'to_alipay_dict'):
                params['loan_interest_repay_mode'] = self.loan_interest_repay_mode.to_alipay_dict()
            else:
                params['loan_interest_repay_mode'] = self.loan_interest_repay_mode
        if self.misappropriation_penalty_interest_org_name:
            if hasattr(self.misappropriation_penalty_interest_org_name, 'to_alipay_dict'):
                params['misappropriation_penalty_interest_org_name'] = self.misappropriation_penalty_interest_org_name.to_alipay_dict()
            else:
                params['misappropriation_penalty_interest_org_name'] = self.misappropriation_penalty_interest_org_name
        if self.misappropriation_penalty_interest_text:
            if hasattr(self.misappropriation_penalty_interest_text, 'to_alipay_dict'):
                params['misappropriation_penalty_interest_text'] = self.misappropriation_penalty_interest_text.to_alipay_dict()
            else:
                params['misappropriation_penalty_interest_text'] = self.misappropriation_penalty_interest_text
        if self.other_fee_org_name:
            if hasattr(self.other_fee_org_name, 'to_alipay_dict'):
                params['other_fee_org_name'] = self.other_fee_org_name.to_alipay_dict()
            else:
                params['other_fee_org_name'] = self.other_fee_org_name
        if self.other_fee_text:
            if hasattr(self.other_fee_text, 'to_alipay_dict'):
                params['other_fee_text'] = self.other_fee_text.to_alipay_dict()
            else:
                params['other_fee_text'] = self.other_fee_text
        if self.overdue_penalty_interest_org_name:
            if hasattr(self.overdue_penalty_interest_org_name, 'to_alipay_dict'):
                params['overdue_penalty_interest_org_name'] = self.overdue_penalty_interest_org_name.to_alipay_dict()
            else:
                params['overdue_penalty_interest_org_name'] = self.overdue_penalty_interest_org_name
        if self.overdue_penalty_interest_text:
            if hasattr(self.overdue_penalty_interest_text, 'to_alipay_dict'):
                params['overdue_penalty_interest_text'] = self.overdue_penalty_interest_text.to_alipay_dict()
            else:
                params['overdue_penalty_interest_text'] = self.overdue_penalty_interest_text
        if self.prepayment_penalty_name:
            if hasattr(self.prepayment_penalty_name, 'to_alipay_dict'):
                params['prepayment_penalty_name'] = self.prepayment_penalty_name.to_alipay_dict()
            else:
                params['prepayment_penalty_name'] = self.prepayment_penalty_name
        if self.prepayment_penalty_org_name:
            if hasattr(self.prepayment_penalty_org_name, 'to_alipay_dict'):
                params['prepayment_penalty_org_name'] = self.prepayment_penalty_org_name.to_alipay_dict()
            else:
                params['prepayment_penalty_org_name'] = self.prepayment_penalty_org_name
        if self.prepayment_penalty_text:
            if hasattr(self.prepayment_penalty_text, 'to_alipay_dict'):
                params['prepayment_penalty_text'] = self.prepayment_penalty_text.to_alipay_dict()
            else:
                params['prepayment_penalty_text'] = self.prepayment_penalty_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanCostDisclosureInfo()
        if 'capped' in d:
            o.capped = d['capped']
        if 'cost_rate' in d:
            o.cost_rate = d['cost_rate']
        if 'guarantee_fee_org_name' in d:
            o.guarantee_fee_org_name = d['guarantee_fee_org_name']
        if 'guarantee_fee_rate' in d:
            o.guarantee_fee_rate = d['guarantee_fee_rate']
        if 'guarantee_fee_rate_type' in d:
            o.guarantee_fee_rate_type = d['guarantee_fee_rate_type']
        if 'guarantee_fee_repay_mode' in d:
            o.guarantee_fee_repay_mode = d['guarantee_fee_repay_mode']
        if 'loan_interest_org_name' in d:
            o.loan_interest_org_name = d['loan_interest_org_name']
        if 'loan_interest_rate' in d:
            o.loan_interest_rate = d['loan_interest_rate']
        if 'loan_interest_rate_type' in d:
            o.loan_interest_rate_type = d['loan_interest_rate_type']
        if 'loan_interest_repay_mode' in d:
            o.loan_interest_repay_mode = d['loan_interest_repay_mode']
        if 'misappropriation_penalty_interest_org_name' in d:
            o.misappropriation_penalty_interest_org_name = d['misappropriation_penalty_interest_org_name']
        if 'misappropriation_penalty_interest_text' in d:
            o.misappropriation_penalty_interest_text = d['misappropriation_penalty_interest_text']
        if 'other_fee_org_name' in d:
            o.other_fee_org_name = d['other_fee_org_name']
        if 'other_fee_text' in d:
            o.other_fee_text = d['other_fee_text']
        if 'overdue_penalty_interest_org_name' in d:
            o.overdue_penalty_interest_org_name = d['overdue_penalty_interest_org_name']
        if 'overdue_penalty_interest_text' in d:
            o.overdue_penalty_interest_text = d['overdue_penalty_interest_text']
        if 'prepayment_penalty_name' in d:
            o.prepayment_penalty_name = d['prepayment_penalty_name']
        if 'prepayment_penalty_org_name' in d:
            o.prepayment_penalty_org_name = d['prepayment_penalty_org_name']
        if 'prepayment_penalty_text' in d:
            o.prepayment_penalty_text = d['prepayment_penalty_text']
        return o


