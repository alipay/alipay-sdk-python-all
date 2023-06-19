#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvTaskCancelModel(object):

    def __init__(self):
        self._fund_supv_product_code = None
        self._fund_supv_task_id = None
        self._supervisor_id_number = None

    @property
    def fund_supv_product_code(self):
        return self._fund_supv_product_code

    @fund_supv_product_code.setter
    def fund_supv_product_code(self, value):
        self._fund_supv_product_code = value
    @property
    def fund_supv_task_id(self):
        return self._fund_supv_task_id

    @fund_supv_task_id.setter
    def fund_supv_task_id(self, value):
        self._fund_supv_task_id = value
    @property
    def supervisor_id_number(self):
        return self._supervisor_id_number

    @supervisor_id_number.setter
    def supervisor_id_number(self, value):
        self._supervisor_id_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_product_code:
            if hasattr(self.fund_supv_product_code, 'to_alipay_dict'):
                params['fund_supv_product_code'] = self.fund_supv_product_code.to_alipay_dict()
            else:
                params['fund_supv_product_code'] = self.fund_supv_product_code
        if self.fund_supv_task_id:
            if hasattr(self.fund_supv_task_id, 'to_alipay_dict'):
                params['fund_supv_task_id'] = self.fund_supv_task_id.to_alipay_dict()
            else:
                params['fund_supv_task_id'] = self.fund_supv_task_id
        if self.supervisor_id_number:
            if hasattr(self.supervisor_id_number, 'to_alipay_dict'):
                params['supervisor_id_number'] = self.supervisor_id_number.to_alipay_dict()
            else:
                params['supervisor_id_number'] = self.supervisor_id_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvTaskCancelModel()
        if 'fund_supv_product_code' in d:
            o.fund_supv_product_code = d['fund_supv_product_code']
        if 'fund_supv_task_id' in d:
            o.fund_supv_task_id = d['fund_supv_task_id']
        if 'supervisor_id_number' in d:
            o.supervisor_id_number = d['supervisor_id_number']
        return o


