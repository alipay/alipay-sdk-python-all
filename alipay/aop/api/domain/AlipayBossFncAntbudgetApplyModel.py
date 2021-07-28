#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyBizBudgetRequest import ApplyBizBudgetRequest


class AlipayBossFncAntbudgetApplyModel(object):

    def __init__(self):
        self._apply_biz_budget_request_list = None
        self._idempotent_id = None

    @property
    def apply_biz_budget_request_list(self):
        return self._apply_biz_budget_request_list

    @apply_biz_budget_request_list.setter
    def apply_biz_budget_request_list(self, value):
        if isinstance(value, list):
            self._apply_biz_budget_request_list = list()
            for i in value:
                if isinstance(i, ApplyBizBudgetRequest):
                    self._apply_biz_budget_request_list.append(i)
                else:
                    self._apply_biz_budget_request_list.append(ApplyBizBudgetRequest.from_alipay_dict(i))
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_biz_budget_request_list:
            if isinstance(self.apply_biz_budget_request_list, list):
                for i in range(0, len(self.apply_biz_budget_request_list)):
                    element = self.apply_biz_budget_request_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_biz_budget_request_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_biz_budget_request_list, 'to_alipay_dict'):
                params['apply_biz_budget_request_list'] = self.apply_biz_budget_request_list.to_alipay_dict()
            else:
                params['apply_biz_budget_request_list'] = self.apply_biz_budget_request_list
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAntbudgetApplyModel()
        if 'apply_biz_budget_request_list' in d:
            o.apply_biz_budget_request_list = d['apply_biz_budget_request_list']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        return o


