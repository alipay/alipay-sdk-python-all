#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryWithholdPlanDTO(object):

    def __init__(self):
        self._deducted_amount = None
        self._plan_id = None
        self._repayed_amount = None
        self._status = None
        self._to_deduct_amount = None
        self._total_to_repay_amount = None
        self._withhold_date = None

    @property
    def deducted_amount(self):
        return self._deducted_amount

    @deducted_amount.setter
    def deducted_amount(self, value):
        self._deducted_amount = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def repayed_amount(self):
        return self._repayed_amount

    @repayed_amount.setter
    def repayed_amount(self, value):
        self._repayed_amount = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def to_deduct_amount(self):
        return self._to_deduct_amount

    @to_deduct_amount.setter
    def to_deduct_amount(self, value):
        self._to_deduct_amount = value
    @property
    def total_to_repay_amount(self):
        return self._total_to_repay_amount

    @total_to_repay_amount.setter
    def total_to_repay_amount(self, value):
        self._total_to_repay_amount = value
    @property
    def withhold_date(self):
        return self._withhold_date

    @withhold_date.setter
    def withhold_date(self, value):
        self._withhold_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.deducted_amount:
            if hasattr(self.deducted_amount, 'to_alipay_dict'):
                params['deducted_amount'] = self.deducted_amount.to_alipay_dict()
            else:
                params['deducted_amount'] = self.deducted_amount
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.repayed_amount:
            if hasattr(self.repayed_amount, 'to_alipay_dict'):
                params['repayed_amount'] = self.repayed_amount.to_alipay_dict()
            else:
                params['repayed_amount'] = self.repayed_amount
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.to_deduct_amount:
            if hasattr(self.to_deduct_amount, 'to_alipay_dict'):
                params['to_deduct_amount'] = self.to_deduct_amount.to_alipay_dict()
            else:
                params['to_deduct_amount'] = self.to_deduct_amount
        if self.total_to_repay_amount:
            if hasattr(self.total_to_repay_amount, 'to_alipay_dict'):
                params['total_to_repay_amount'] = self.total_to_repay_amount.to_alipay_dict()
            else:
                params['total_to_repay_amount'] = self.total_to_repay_amount
        if self.withhold_date:
            if hasattr(self.withhold_date, 'to_alipay_dict'):
                params['withhold_date'] = self.withhold_date.to_alipay_dict()
            else:
                params['withhold_date'] = self.withhold_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryWithholdPlanDTO()
        if 'deducted_amount' in d:
            o.deducted_amount = d['deducted_amount']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'repayed_amount' in d:
            o.repayed_amount = d['repayed_amount']
        if 'status' in d:
            o.status = d['status']
        if 'to_deduct_amount' in d:
            o.to_deduct_amount = d['to_deduct_amount']
        if 'total_to_repay_amount' in d:
            o.total_to_repay_amount = d['total_to_repay_amount']
        if 'withhold_date' in d:
            o.withhold_date = d['withhold_date']
        return o


