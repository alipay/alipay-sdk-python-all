#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankBudgetConfigInfo import DtBankBudgetConfigInfo
from alipay.aop.api.domain.DtBankBudgetRealTimeInfo import DtBankBudgetRealTimeInfo


class DtBankBudgetInfo(object):

    def __init__(self):
        self._budget_config_info = None
        self._budget_real_time_info = None

    @property
    def budget_config_info(self):
        return self._budget_config_info

    @budget_config_info.setter
    def budget_config_info(self, value):
        if isinstance(value, DtBankBudgetConfigInfo):
            self._budget_config_info = value
        else:
            self._budget_config_info = DtBankBudgetConfigInfo.from_alipay_dict(value)
    @property
    def budget_real_time_info(self):
        return self._budget_real_time_info

    @budget_real_time_info.setter
    def budget_real_time_info(self, value):
        if isinstance(value, DtBankBudgetRealTimeInfo):
            self._budget_real_time_info = value
        else:
            self._budget_real_time_info = DtBankBudgetRealTimeInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.budget_config_info:
            if hasattr(self.budget_config_info, 'to_alipay_dict'):
                params['budget_config_info'] = self.budget_config_info.to_alipay_dict()
            else:
                params['budget_config_info'] = self.budget_config_info
        if self.budget_real_time_info:
            if hasattr(self.budget_real_time_info, 'to_alipay_dict'):
                params['budget_real_time_info'] = self.budget_real_time_info.to_alipay_dict()
            else:
                params['budget_real_time_info'] = self.budget_real_time_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankBudgetInfo()
        if 'budget_config_info' in d:
            o.budget_config_info = d['budget_config_info']
        if 'budget_real_time_info' in d:
            o.budget_real_time_info = d['budget_real_time_info']
        return o


