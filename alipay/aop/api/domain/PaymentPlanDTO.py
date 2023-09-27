#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentPlanItemDTO import PaymentPlanItemDTO


class PaymentPlanDTO(object):

    def __init__(self):
        self._pay_on_percent = None
        self._payment_name = None
        self._payment_plan_item_list = None
        self._payment_type = None
        self._purchase_order_id = None

    @property
    def pay_on_percent(self):
        return self._pay_on_percent

    @pay_on_percent.setter
    def pay_on_percent(self, value):
        self._pay_on_percent = value
    @property
    def payment_name(self):
        return self._payment_name

    @payment_name.setter
    def payment_name(self, value):
        self._payment_name = value
    @property
    def payment_plan_item_list(self):
        return self._payment_plan_item_list

    @payment_plan_item_list.setter
    def payment_plan_item_list(self, value):
        if isinstance(value, list):
            self._payment_plan_item_list = list()
            for i in value:
                if isinstance(i, PaymentPlanItemDTO):
                    self._payment_plan_item_list.append(i)
                else:
                    self._payment_plan_item_list.append(PaymentPlanItemDTO.from_alipay_dict(i))
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, value):
        self._purchase_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_on_percent:
            if hasattr(self.pay_on_percent, 'to_alipay_dict'):
                params['pay_on_percent'] = self.pay_on_percent.to_alipay_dict()
            else:
                params['pay_on_percent'] = self.pay_on_percent
        if self.payment_name:
            if hasattr(self.payment_name, 'to_alipay_dict'):
                params['payment_name'] = self.payment_name.to_alipay_dict()
            else:
                params['payment_name'] = self.payment_name
        if self.payment_plan_item_list:
            if isinstance(self.payment_plan_item_list, list):
                for i in range(0, len(self.payment_plan_item_list)):
                    element = self.payment_plan_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_plan_item_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_plan_item_list, 'to_alipay_dict'):
                params['payment_plan_item_list'] = self.payment_plan_item_list.to_alipay_dict()
            else:
                params['payment_plan_item_list'] = self.payment_plan_item_list
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.purchase_order_id:
            if hasattr(self.purchase_order_id, 'to_alipay_dict'):
                params['purchase_order_id'] = self.purchase_order_id.to_alipay_dict()
            else:
                params['purchase_order_id'] = self.purchase_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentPlanDTO()
        if 'pay_on_percent' in d:
            o.pay_on_percent = d['pay_on_percent']
        if 'payment_name' in d:
            o.payment_name = d['payment_name']
        if 'payment_plan_item_list' in d:
            o.payment_plan_item_list = d['payment_plan_item_list']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'purchase_order_id' in d:
            o.purchase_order_id = d['purchase_order_id']
        return o


