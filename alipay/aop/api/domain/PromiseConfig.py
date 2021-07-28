#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromiseConfig(object):

    def __init__(self):
        self._action_operation_type = None
        self._action_operation_value = None
        self._button_buy = None
        self._button_end = None
        self._button_installment = None
        self._button_postpone = None
        self._button_repair = None
        self._button_replace = None
        self._fulfillment_days = None
        self._merchant_service_phone = None
        self._merchant_service_url = None
        self._money_operation_type = None
        self._money_operation_value = None
        self._product_operation_type = None
        self._product_operation_value = None

    @property
    def action_operation_type(self):
        return self._action_operation_type

    @action_operation_type.setter
    def action_operation_type(self, value):
        self._action_operation_type = value
    @property
    def action_operation_value(self):
        return self._action_operation_value

    @action_operation_value.setter
    def action_operation_value(self, value):
        self._action_operation_value = value
    @property
    def button_buy(self):
        return self._button_buy

    @button_buy.setter
    def button_buy(self, value):
        self._button_buy = value
    @property
    def button_end(self):
        return self._button_end

    @button_end.setter
    def button_end(self, value):
        self._button_end = value
    @property
    def button_installment(self):
        return self._button_installment

    @button_installment.setter
    def button_installment(self, value):
        self._button_installment = value
    @property
    def button_postpone(self):
        return self._button_postpone

    @button_postpone.setter
    def button_postpone(self, value):
        self._button_postpone = value
    @property
    def button_repair(self):
        return self._button_repair

    @button_repair.setter
    def button_repair(self, value):
        self._button_repair = value
    @property
    def button_replace(self):
        return self._button_replace

    @button_replace.setter
    def button_replace(self, value):
        self._button_replace = value
    @property
    def fulfillment_days(self):
        return self._fulfillment_days

    @fulfillment_days.setter
    def fulfillment_days(self, value):
        self._fulfillment_days = value
    @property
    def merchant_service_phone(self):
        return self._merchant_service_phone

    @merchant_service_phone.setter
    def merchant_service_phone(self, value):
        self._merchant_service_phone = value
    @property
    def merchant_service_url(self):
        return self._merchant_service_url

    @merchant_service_url.setter
    def merchant_service_url(self, value):
        self._merchant_service_url = value
    @property
    def money_operation_type(self):
        return self._money_operation_type

    @money_operation_type.setter
    def money_operation_type(self, value):
        self._money_operation_type = value
    @property
    def money_operation_value(self):
        return self._money_operation_value

    @money_operation_value.setter
    def money_operation_value(self, value):
        self._money_operation_value = value
    @property
    def product_operation_type(self):
        return self._product_operation_type

    @product_operation_type.setter
    def product_operation_type(self, value):
        self._product_operation_type = value
    @property
    def product_operation_value(self):
        return self._product_operation_value

    @product_operation_value.setter
    def product_operation_value(self, value):
        self._product_operation_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_operation_type:
            if hasattr(self.action_operation_type, 'to_alipay_dict'):
                params['action_operation_type'] = self.action_operation_type.to_alipay_dict()
            else:
                params['action_operation_type'] = self.action_operation_type
        if self.action_operation_value:
            if hasattr(self.action_operation_value, 'to_alipay_dict'):
                params['action_operation_value'] = self.action_operation_value.to_alipay_dict()
            else:
                params['action_operation_value'] = self.action_operation_value
        if self.button_buy:
            if hasattr(self.button_buy, 'to_alipay_dict'):
                params['button_buy'] = self.button_buy.to_alipay_dict()
            else:
                params['button_buy'] = self.button_buy
        if self.button_end:
            if hasattr(self.button_end, 'to_alipay_dict'):
                params['button_end'] = self.button_end.to_alipay_dict()
            else:
                params['button_end'] = self.button_end
        if self.button_installment:
            if hasattr(self.button_installment, 'to_alipay_dict'):
                params['button_installment'] = self.button_installment.to_alipay_dict()
            else:
                params['button_installment'] = self.button_installment
        if self.button_postpone:
            if hasattr(self.button_postpone, 'to_alipay_dict'):
                params['button_postpone'] = self.button_postpone.to_alipay_dict()
            else:
                params['button_postpone'] = self.button_postpone
        if self.button_repair:
            if hasattr(self.button_repair, 'to_alipay_dict'):
                params['button_repair'] = self.button_repair.to_alipay_dict()
            else:
                params['button_repair'] = self.button_repair
        if self.button_replace:
            if hasattr(self.button_replace, 'to_alipay_dict'):
                params['button_replace'] = self.button_replace.to_alipay_dict()
            else:
                params['button_replace'] = self.button_replace
        if self.fulfillment_days:
            if hasattr(self.fulfillment_days, 'to_alipay_dict'):
                params['fulfillment_days'] = self.fulfillment_days.to_alipay_dict()
            else:
                params['fulfillment_days'] = self.fulfillment_days
        if self.merchant_service_phone:
            if hasattr(self.merchant_service_phone, 'to_alipay_dict'):
                params['merchant_service_phone'] = self.merchant_service_phone.to_alipay_dict()
            else:
                params['merchant_service_phone'] = self.merchant_service_phone
        if self.merchant_service_url:
            if hasattr(self.merchant_service_url, 'to_alipay_dict'):
                params['merchant_service_url'] = self.merchant_service_url.to_alipay_dict()
            else:
                params['merchant_service_url'] = self.merchant_service_url
        if self.money_operation_type:
            if hasattr(self.money_operation_type, 'to_alipay_dict'):
                params['money_operation_type'] = self.money_operation_type.to_alipay_dict()
            else:
                params['money_operation_type'] = self.money_operation_type
        if self.money_operation_value:
            if hasattr(self.money_operation_value, 'to_alipay_dict'):
                params['money_operation_value'] = self.money_operation_value.to_alipay_dict()
            else:
                params['money_operation_value'] = self.money_operation_value
        if self.product_operation_type:
            if hasattr(self.product_operation_type, 'to_alipay_dict'):
                params['product_operation_type'] = self.product_operation_type.to_alipay_dict()
            else:
                params['product_operation_type'] = self.product_operation_type
        if self.product_operation_value:
            if hasattr(self.product_operation_value, 'to_alipay_dict'):
                params['product_operation_value'] = self.product_operation_value.to_alipay_dict()
            else:
                params['product_operation_value'] = self.product_operation_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromiseConfig()
        if 'action_operation_type' in d:
            o.action_operation_type = d['action_operation_type']
        if 'action_operation_value' in d:
            o.action_operation_value = d['action_operation_value']
        if 'button_buy' in d:
            o.button_buy = d['button_buy']
        if 'button_end' in d:
            o.button_end = d['button_end']
        if 'button_installment' in d:
            o.button_installment = d['button_installment']
        if 'button_postpone' in d:
            o.button_postpone = d['button_postpone']
        if 'button_repair' in d:
            o.button_repair = d['button_repair']
        if 'button_replace' in d:
            o.button_replace = d['button_replace']
        if 'fulfillment_days' in d:
            o.fulfillment_days = d['fulfillment_days']
        if 'merchant_service_phone' in d:
            o.merchant_service_phone = d['merchant_service_phone']
        if 'merchant_service_url' in d:
            o.merchant_service_url = d['merchant_service_url']
        if 'money_operation_type' in d:
            o.money_operation_type = d['money_operation_type']
        if 'money_operation_value' in d:
            o.money_operation_value = d['money_operation_value']
        if 'product_operation_type' in d:
            o.product_operation_type = d['product_operation_type']
        if 'product_operation_value' in d:
            o.product_operation_value = d['product_operation_value']
        return o


