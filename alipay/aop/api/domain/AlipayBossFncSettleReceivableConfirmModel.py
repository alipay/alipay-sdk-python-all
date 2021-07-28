#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceivableConfirmOrder import ReceivableConfirmOrder


class AlipayBossFncSettleReceivableConfirmModel(object):

    def __init__(self):
        self._receivable_confirm_order_list = None

    @property
    def receivable_confirm_order_list(self):
        return self._receivable_confirm_order_list

    @receivable_confirm_order_list.setter
    def receivable_confirm_order_list(self, value):
        if isinstance(value, list):
            self._receivable_confirm_order_list = list()
            for i in value:
                if isinstance(i, ReceivableConfirmOrder):
                    self._receivable_confirm_order_list.append(i)
                else:
                    self._receivable_confirm_order_list.append(ReceivableConfirmOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.receivable_confirm_order_list:
            if isinstance(self.receivable_confirm_order_list, list):
                for i in range(0, len(self.receivable_confirm_order_list)):
                    element = self.receivable_confirm_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receivable_confirm_order_list[i] = element.to_alipay_dict()
            if hasattr(self.receivable_confirm_order_list, 'to_alipay_dict'):
                params['receivable_confirm_order_list'] = self.receivable_confirm_order_list.to_alipay_dict()
            else:
                params['receivable_confirm_order_list'] = self.receivable_confirm_order_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncSettleReceivableConfirmModel()
        if 'receivable_confirm_order_list' in d:
            o.receivable_confirm_order_list = d['receivable_confirm_order_list']
        return o


