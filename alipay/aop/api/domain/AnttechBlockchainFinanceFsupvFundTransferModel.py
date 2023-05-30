#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvFundTransferModel(object):

    def __init__(self):
        self._fund_supv_task_id = None
        self._request_no = None
        self._transfer_amount = None
        self._unfreeze_balance_flag = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def transfer_amount(self):
        return self._transfer_amount

    @transfer_amount.setter
    def transfer_amount(self, value):
        self._transfer_amount = value
    @property
    def unfreeze_balance_flag(self):
        return self._unfreeze_balance_flag

    @unfreeze_balance_flag.setter
    def unfreeze_balance_flag(self, value):
        self._unfreeze_balance_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_task_id:
            if hasattr(self.fund_supv_task_id, 'to_alipay_dict'):
                params['fund_supv_task_id'] = self.fund_supv_task_id.to_alipay_dict()
            else:
                params['fund_supv_task_id'] = self.fund_supv_task_id
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.transfer_amount:
            if hasattr(self.transfer_amount, 'to_alipay_dict'):
                params['transfer_amount'] = self.transfer_amount.to_alipay_dict()
            else:
                params['transfer_amount'] = self.transfer_amount
        if self.unfreeze_balance_flag:
            if hasattr(self.unfreeze_balance_flag, 'to_alipay_dict'):
                params['unfreeze_balance_flag'] = self.unfreeze_balance_flag.to_alipay_dict()
            else:
                params['unfreeze_balance_flag'] = self.unfreeze_balance_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvFundTransferModel()
        if 'fund_supv_task_id' in d:
            o.fund_supv_task_id = d['fund_supv_task_id']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'transfer_amount' in d:
            o.transfer_amount = d['transfer_amount']
        if 'unfreeze_balance_flag' in d:
            o.unfreeze_balance_flag = d['unfreeze_balance_flag']
        return o


