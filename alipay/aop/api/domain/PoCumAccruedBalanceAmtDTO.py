#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PoCumAccruedBalanceAmtDetailDTO import PoCumAccruedBalanceAmtDetailDTO


class PoCumAccruedBalanceAmtDTO(object):

    def __init__(self):
        self._account_period = None
        self._accrued_balance_detail_list = None
        self._close_accounted_status = None

    @property
    def account_period(self):
        return self._account_period

    @account_period.setter
    def account_period(self, value):
        self._account_period = value
    @property
    def accrued_balance_detail_list(self):
        return self._accrued_balance_detail_list

    @accrued_balance_detail_list.setter
    def accrued_balance_detail_list(self, value):
        if isinstance(value, list):
            self._accrued_balance_detail_list = list()
            for i in value:
                if isinstance(i, PoCumAccruedBalanceAmtDetailDTO):
                    self._accrued_balance_detail_list.append(i)
                else:
                    self._accrued_balance_detail_list.append(PoCumAccruedBalanceAmtDetailDTO.from_alipay_dict(i))
    @property
    def close_accounted_status(self):
        return self._close_accounted_status

    @close_accounted_status.setter
    def close_accounted_status(self, value):
        self._close_accounted_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_period:
            if hasattr(self.account_period, 'to_alipay_dict'):
                params['account_period'] = self.account_period.to_alipay_dict()
            else:
                params['account_period'] = self.account_period
        if self.accrued_balance_detail_list:
            if isinstance(self.accrued_balance_detail_list, list):
                for i in range(0, len(self.accrued_balance_detail_list)):
                    element = self.accrued_balance_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.accrued_balance_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.accrued_balance_detail_list, 'to_alipay_dict'):
                params['accrued_balance_detail_list'] = self.accrued_balance_detail_list.to_alipay_dict()
            else:
                params['accrued_balance_detail_list'] = self.accrued_balance_detail_list
        if self.close_accounted_status:
            if hasattr(self.close_accounted_status, 'to_alipay_dict'):
                params['close_accounted_status'] = self.close_accounted_status.to_alipay_dict()
            else:
                params['close_accounted_status'] = self.close_accounted_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoCumAccruedBalanceAmtDTO()
        if 'account_period' in d:
            o.account_period = d['account_period']
        if 'accrued_balance_detail_list' in d:
            o.accrued_balance_detail_list = d['accrued_balance_detail_list']
        if 'close_accounted_status' in d:
            o.close_accounted_status = d['close_accounted_status']
        return o


