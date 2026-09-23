#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IntlEstimatedFee(object):

    def __init__(self):
        self._base_freight = None
        self._before_discount_fee = None
        self._fuel_fee = None
        self._insured_fee = None
        self._merchant_discount_fee = None
        self._operation_fee = None
        self._order_fee = None
        self._other_addvalue_fee = None
        self._other_freight = None
        self._other_surcharge_fee = None
        self._oversize_overweight_fee = None
        self._packaging_fee = None
        self._remote_area_surcharge = None
        self._sensitive_goods_addvalue_fee = None
        self._super_sensitive_addvalue_fee = None

    @property
    def base_freight(self):
        return self._base_freight

    @base_freight.setter
    def base_freight(self, value):
        self._base_freight = value
    @property
    def before_discount_fee(self):
        return self._before_discount_fee

    @before_discount_fee.setter
    def before_discount_fee(self, value):
        self._before_discount_fee = value
    @property
    def fuel_fee(self):
        return self._fuel_fee

    @fuel_fee.setter
    def fuel_fee(self, value):
        self._fuel_fee = value
    @property
    def insured_fee(self):
        return self._insured_fee

    @insured_fee.setter
    def insured_fee(self, value):
        self._insured_fee = value
    @property
    def merchant_discount_fee(self):
        return self._merchant_discount_fee

    @merchant_discount_fee.setter
    def merchant_discount_fee(self, value):
        self._merchant_discount_fee = value
    @property
    def operation_fee(self):
        return self._operation_fee

    @operation_fee.setter
    def operation_fee(self, value):
        self._operation_fee = value
    @property
    def order_fee(self):
        return self._order_fee

    @order_fee.setter
    def order_fee(self, value):
        self._order_fee = value
    @property
    def other_addvalue_fee(self):
        return self._other_addvalue_fee

    @other_addvalue_fee.setter
    def other_addvalue_fee(self, value):
        self._other_addvalue_fee = value
    @property
    def other_freight(self):
        return self._other_freight

    @other_freight.setter
    def other_freight(self, value):
        self._other_freight = value
    @property
    def other_surcharge_fee(self):
        return self._other_surcharge_fee

    @other_surcharge_fee.setter
    def other_surcharge_fee(self, value):
        self._other_surcharge_fee = value
    @property
    def oversize_overweight_fee(self):
        return self._oversize_overweight_fee

    @oversize_overweight_fee.setter
    def oversize_overweight_fee(self, value):
        self._oversize_overweight_fee = value
    @property
    def packaging_fee(self):
        return self._packaging_fee

    @packaging_fee.setter
    def packaging_fee(self, value):
        self._packaging_fee = value
    @property
    def remote_area_surcharge(self):
        return self._remote_area_surcharge

    @remote_area_surcharge.setter
    def remote_area_surcharge(self, value):
        self._remote_area_surcharge = value
    @property
    def sensitive_goods_addvalue_fee(self):
        return self._sensitive_goods_addvalue_fee

    @sensitive_goods_addvalue_fee.setter
    def sensitive_goods_addvalue_fee(self, value):
        self._sensitive_goods_addvalue_fee = value
    @property
    def super_sensitive_addvalue_fee(self):
        return self._super_sensitive_addvalue_fee

    @super_sensitive_addvalue_fee.setter
    def super_sensitive_addvalue_fee(self, value):
        self._super_sensitive_addvalue_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.base_freight:
            if hasattr(self.base_freight, 'to_alipay_dict'):
                params['base_freight'] = self.base_freight.to_alipay_dict()
            else:
                params['base_freight'] = self.base_freight
        if self.before_discount_fee:
            if hasattr(self.before_discount_fee, 'to_alipay_dict'):
                params['before_discount_fee'] = self.before_discount_fee.to_alipay_dict()
            else:
                params['before_discount_fee'] = self.before_discount_fee
        if self.fuel_fee:
            if hasattr(self.fuel_fee, 'to_alipay_dict'):
                params['fuel_fee'] = self.fuel_fee.to_alipay_dict()
            else:
                params['fuel_fee'] = self.fuel_fee
        if self.insured_fee:
            if hasattr(self.insured_fee, 'to_alipay_dict'):
                params['insured_fee'] = self.insured_fee.to_alipay_dict()
            else:
                params['insured_fee'] = self.insured_fee
        if self.merchant_discount_fee:
            if hasattr(self.merchant_discount_fee, 'to_alipay_dict'):
                params['merchant_discount_fee'] = self.merchant_discount_fee.to_alipay_dict()
            else:
                params['merchant_discount_fee'] = self.merchant_discount_fee
        if self.operation_fee:
            if hasattr(self.operation_fee, 'to_alipay_dict'):
                params['operation_fee'] = self.operation_fee.to_alipay_dict()
            else:
                params['operation_fee'] = self.operation_fee
        if self.order_fee:
            if hasattr(self.order_fee, 'to_alipay_dict'):
                params['order_fee'] = self.order_fee.to_alipay_dict()
            else:
                params['order_fee'] = self.order_fee
        if self.other_addvalue_fee:
            if hasattr(self.other_addvalue_fee, 'to_alipay_dict'):
                params['other_addvalue_fee'] = self.other_addvalue_fee.to_alipay_dict()
            else:
                params['other_addvalue_fee'] = self.other_addvalue_fee
        if self.other_freight:
            if hasattr(self.other_freight, 'to_alipay_dict'):
                params['other_freight'] = self.other_freight.to_alipay_dict()
            else:
                params['other_freight'] = self.other_freight
        if self.other_surcharge_fee:
            if hasattr(self.other_surcharge_fee, 'to_alipay_dict'):
                params['other_surcharge_fee'] = self.other_surcharge_fee.to_alipay_dict()
            else:
                params['other_surcharge_fee'] = self.other_surcharge_fee
        if self.oversize_overweight_fee:
            if hasattr(self.oversize_overweight_fee, 'to_alipay_dict'):
                params['oversize_overweight_fee'] = self.oversize_overweight_fee.to_alipay_dict()
            else:
                params['oversize_overweight_fee'] = self.oversize_overweight_fee
        if self.packaging_fee:
            if hasattr(self.packaging_fee, 'to_alipay_dict'):
                params['packaging_fee'] = self.packaging_fee.to_alipay_dict()
            else:
                params['packaging_fee'] = self.packaging_fee
        if self.remote_area_surcharge:
            if hasattr(self.remote_area_surcharge, 'to_alipay_dict'):
                params['remote_area_surcharge'] = self.remote_area_surcharge.to_alipay_dict()
            else:
                params['remote_area_surcharge'] = self.remote_area_surcharge
        if self.sensitive_goods_addvalue_fee:
            if hasattr(self.sensitive_goods_addvalue_fee, 'to_alipay_dict'):
                params['sensitive_goods_addvalue_fee'] = self.sensitive_goods_addvalue_fee.to_alipay_dict()
            else:
                params['sensitive_goods_addvalue_fee'] = self.sensitive_goods_addvalue_fee
        if self.super_sensitive_addvalue_fee:
            if hasattr(self.super_sensitive_addvalue_fee, 'to_alipay_dict'):
                params['super_sensitive_addvalue_fee'] = self.super_sensitive_addvalue_fee.to_alipay_dict()
            else:
                params['super_sensitive_addvalue_fee'] = self.super_sensitive_addvalue_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IntlEstimatedFee()
        if 'base_freight' in d:
            o.base_freight = d['base_freight']
        if 'before_discount_fee' in d:
            o.before_discount_fee = d['before_discount_fee']
        if 'fuel_fee' in d:
            o.fuel_fee = d['fuel_fee']
        if 'insured_fee' in d:
            o.insured_fee = d['insured_fee']
        if 'merchant_discount_fee' in d:
            o.merchant_discount_fee = d['merchant_discount_fee']
        if 'operation_fee' in d:
            o.operation_fee = d['operation_fee']
        if 'order_fee' in d:
            o.order_fee = d['order_fee']
        if 'other_addvalue_fee' in d:
            o.other_addvalue_fee = d['other_addvalue_fee']
        if 'other_freight' in d:
            o.other_freight = d['other_freight']
        if 'other_surcharge_fee' in d:
            o.other_surcharge_fee = d['other_surcharge_fee']
        if 'oversize_overweight_fee' in d:
            o.oversize_overweight_fee = d['oversize_overweight_fee']
        if 'packaging_fee' in d:
            o.packaging_fee = d['packaging_fee']
        if 'remote_area_surcharge' in d:
            o.remote_area_surcharge = d['remote_area_surcharge']
        if 'sensitive_goods_addvalue_fee' in d:
            o.sensitive_goods_addvalue_fee = d['sensitive_goods_addvalue_fee']
        if 'super_sensitive_addvalue_fee' in d:
            o.super_sensitive_addvalue_fee = d['super_sensitive_addvalue_fee']
        return o


