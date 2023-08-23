#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrePayOperationInfoViewData(object):

    def __init__(self):
        self._logo = None
        self._operation_desc = None
        self._operation_tip = None
        self._pay_operation_info = None
        self._promo_price = None
        self._promo_type = None
        self._threshold_amount = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def operation_desc(self):
        return self._operation_desc

    @operation_desc.setter
    def operation_desc(self, value):
        self._operation_desc = value
    @property
    def operation_tip(self):
        return self._operation_tip

    @operation_tip.setter
    def operation_tip(self, value):
        self._operation_tip = value
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value
    @property
    def promo_price(self):
        return self._promo_price

    @promo_price.setter
    def promo_price(self, value):
        self._promo_price = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.operation_desc:
            if hasattr(self.operation_desc, 'to_alipay_dict'):
                params['operation_desc'] = self.operation_desc.to_alipay_dict()
            else:
                params['operation_desc'] = self.operation_desc
        if self.operation_tip:
            if hasattr(self.operation_tip, 'to_alipay_dict'):
                params['operation_tip'] = self.operation_tip.to_alipay_dict()
            else:
                params['operation_tip'] = self.operation_tip
        if self.pay_operation_info:
            if hasattr(self.pay_operation_info, 'to_alipay_dict'):
                params['pay_operation_info'] = self.pay_operation_info.to_alipay_dict()
            else:
                params['pay_operation_info'] = self.pay_operation_info
        if self.promo_price:
            if hasattr(self.promo_price, 'to_alipay_dict'):
                params['promo_price'] = self.promo_price.to_alipay_dict()
            else:
                params['promo_price'] = self.promo_price
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrePayOperationInfoViewData()
        if 'logo' in d:
            o.logo = d['logo']
        if 'operation_desc' in d:
            o.operation_desc = d['operation_desc']
        if 'operation_tip' in d:
            o.operation_tip = d['operation_tip']
        if 'pay_operation_info' in d:
            o.pay_operation_info = d['pay_operation_info']
        if 'promo_price' in d:
            o.promo_price = d['promo_price']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        return o


