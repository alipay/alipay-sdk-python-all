#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipayItemDescription import AlipayItemDescription
from alipay.aop.api.domain.AlipayItemGoodsList import AlipayItemGoodsList
from alipay.aop.api.domain.AlipayItemLimitPeriodInfo import AlipayItemLimitPeriodInfo


class AlipayItemVoucherTemplete(object):

    def __init__(self):
        self._delay_minute = None
        self._desc_details = None
        self._discount_rate = None
        self._external_goods_list = None
        self._limit_period_info_list = None
        self._original_amount = None
        self._original_rate = None
        self._reduce_to_amount = None
        self._rounding_rule = None
        self._threshold_amount = None
        self._threshold_quantity = None
        self._valid_period = None
        self._value_amount = None
        self._voucher_desc = None
        self._voucher_type = None

    @property
    def delay_minute(self):
        return self._delay_minute

    @delay_minute.setter
    def delay_minute(self, value):
        self._delay_minute = value
    @property
    def desc_details(self):
        return self._desc_details

    @desc_details.setter
    def desc_details(self, value):
        if isinstance(value, list):
            self._desc_details = list()
            for i in value:
                if isinstance(i, AlipayItemDescription):
                    self._desc_details.append(i)
                else:
                    self._desc_details.append(AlipayItemDescription.from_alipay_dict(i))
    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value):
        self._discount_rate = value
    @property
    def external_goods_list(self):
        return self._external_goods_list

    @external_goods_list.setter
    def external_goods_list(self, value):
        if isinstance(value, AlipayItemGoodsList):
            self._external_goods_list = value
        else:
            self._external_goods_list = AlipayItemGoodsList.from_alipay_dict(value)
    @property
    def limit_period_info_list(self):
        return self._limit_period_info_list

    @limit_period_info_list.setter
    def limit_period_info_list(self, value):
        if isinstance(value, list):
            self._limit_period_info_list = list()
            for i in value:
                if isinstance(i, AlipayItemLimitPeriodInfo):
                    self._limit_period_info_list.append(i)
                else:
                    self._limit_period_info_list.append(AlipayItemLimitPeriodInfo.from_alipay_dict(i))
    @property
    def original_amount(self):
        return self._original_amount

    @original_amount.setter
    def original_amount(self, value):
        self._original_amount = value
    @property
    def original_rate(self):
        return self._original_rate

    @original_rate.setter
    def original_rate(self, value):
        self._original_rate = value
    @property
    def reduce_to_amount(self):
        return self._reduce_to_amount

    @reduce_to_amount.setter
    def reduce_to_amount(self, value):
        self._reduce_to_amount = value
    @property
    def rounding_rule(self):
        return self._rounding_rule

    @rounding_rule.setter
    def rounding_rule(self, value):
        self._rounding_rule = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def threshold_quantity(self):
        return self._threshold_quantity

    @threshold_quantity.setter
    def threshold_quantity(self, value):
        self._threshold_quantity = value
    @property
    def valid_period(self):
        return self._valid_period

    @valid_period.setter
    def valid_period(self, value):
        self._valid_period = value
    @property
    def value_amount(self):
        return self._value_amount

    @value_amount.setter
    def value_amount(self, value):
        self._value_amount = value
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delay_minute:
            if hasattr(self.delay_minute, 'to_alipay_dict'):
                params['delay_minute'] = self.delay_minute.to_alipay_dict()
            else:
                params['delay_minute'] = self.delay_minute
        if self.desc_details:
            if isinstance(self.desc_details, list):
                for i in range(0, len(self.desc_details)):
                    element = self.desc_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.desc_details[i] = element.to_alipay_dict()
            if hasattr(self.desc_details, 'to_alipay_dict'):
                params['desc_details'] = self.desc_details.to_alipay_dict()
            else:
                params['desc_details'] = self.desc_details
        if self.discount_rate:
            if hasattr(self.discount_rate, 'to_alipay_dict'):
                params['discount_rate'] = self.discount_rate.to_alipay_dict()
            else:
                params['discount_rate'] = self.discount_rate
        if self.external_goods_list:
            if hasattr(self.external_goods_list, 'to_alipay_dict'):
                params['external_goods_list'] = self.external_goods_list.to_alipay_dict()
            else:
                params['external_goods_list'] = self.external_goods_list
        if self.limit_period_info_list:
            if isinstance(self.limit_period_info_list, list):
                for i in range(0, len(self.limit_period_info_list)):
                    element = self.limit_period_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.limit_period_info_list[i] = element.to_alipay_dict()
            if hasattr(self.limit_period_info_list, 'to_alipay_dict'):
                params['limit_period_info_list'] = self.limit_period_info_list.to_alipay_dict()
            else:
                params['limit_period_info_list'] = self.limit_period_info_list
        if self.original_amount:
            if hasattr(self.original_amount, 'to_alipay_dict'):
                params['original_amount'] = self.original_amount.to_alipay_dict()
            else:
                params['original_amount'] = self.original_amount
        if self.original_rate:
            if hasattr(self.original_rate, 'to_alipay_dict'):
                params['original_rate'] = self.original_rate.to_alipay_dict()
            else:
                params['original_rate'] = self.original_rate
        if self.reduce_to_amount:
            if hasattr(self.reduce_to_amount, 'to_alipay_dict'):
                params['reduce_to_amount'] = self.reduce_to_amount.to_alipay_dict()
            else:
                params['reduce_to_amount'] = self.reduce_to_amount
        if self.rounding_rule:
            if hasattr(self.rounding_rule, 'to_alipay_dict'):
                params['rounding_rule'] = self.rounding_rule.to_alipay_dict()
            else:
                params['rounding_rule'] = self.rounding_rule
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.threshold_quantity:
            if hasattr(self.threshold_quantity, 'to_alipay_dict'):
                params['threshold_quantity'] = self.threshold_quantity.to_alipay_dict()
            else:
                params['threshold_quantity'] = self.threshold_quantity
        if self.valid_period:
            if hasattr(self.valid_period, 'to_alipay_dict'):
                params['valid_period'] = self.valid_period.to_alipay_dict()
            else:
                params['valid_period'] = self.valid_period
        if self.value_amount:
            if hasattr(self.value_amount, 'to_alipay_dict'):
                params['value_amount'] = self.value_amount.to_alipay_dict()
            else:
                params['value_amount'] = self.value_amount
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayItemVoucherTemplete()
        if 'delay_minute' in d:
            o.delay_minute = d['delay_minute']
        if 'desc_details' in d:
            o.desc_details = d['desc_details']
        if 'discount_rate' in d:
            o.discount_rate = d['discount_rate']
        if 'external_goods_list' in d:
            o.external_goods_list = d['external_goods_list']
        if 'limit_period_info_list' in d:
            o.limit_period_info_list = d['limit_period_info_list']
        if 'original_amount' in d:
            o.original_amount = d['original_amount']
        if 'original_rate' in d:
            o.original_rate = d['original_rate']
        if 'reduce_to_amount' in d:
            o.reduce_to_amount = d['reduce_to_amount']
        if 'rounding_rule' in d:
            o.rounding_rule = d['rounding_rule']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'threshold_quantity' in d:
            o.threshold_quantity = d['threshold_quantity']
        if 'valid_period' in d:
            o.valid_period = d['valid_period']
        if 'value_amount' in d:
            o.value_amount = d['value_amount']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


