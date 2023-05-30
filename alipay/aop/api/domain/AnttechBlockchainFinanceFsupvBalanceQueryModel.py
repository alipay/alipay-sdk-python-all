#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvBalanceQueryModel(object):

    def __init__(self):
        self._fund_supv_task_id = None

    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_task_id:
            if hasattr(self.fund_supv_task_id, 'to_alipay_dict'):
                params['fund_supv_task_id'] = self.fund_supv_task_id.to_alipay_dict()
            else:
                params['fund_supv_task_id'] = self.fund_supv_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvBalanceQueryModel()
        if 'fund_supv_task_id' in d:
            o.fund_supv_task_id = d['fund_supv_task_id']
        return o


