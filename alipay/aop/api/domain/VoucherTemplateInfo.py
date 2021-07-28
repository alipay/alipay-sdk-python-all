#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TimePeriodRule import TimePeriodRule
from alipay.aop.api.domain.TimePeriodRule import TimePeriodRule


class VoucherTemplateInfo(object):

    def __init__(self):
        self._amount = None
        self._ceiling_amount = None
        self._disable_detail_periods = None
        self._discount = None
        self._discount_calc_type = None
        self._floor_amount = None
        self._goods_id = None
        self._template_id = None
        self._usable_detail_period = None
        self._usable_end_time = None
        self._usable_start_time = None
        self._usable_time_type = None
        self._voucher_description = None
        self._voucher_name = None
        self._voucher_quantity = None
        self._voucher_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def disable_detail_periods(self):
        return self._disable_detail_periods

    @disable_detail_periods.setter
    def disable_detail_periods(self, value):
        if isinstance(value, list):
            self._disable_detail_periods = list()
            for i in value:
                if isinstance(i, TimePeriodRule):
                    self._disable_detail_periods.append(i)
                else:
                    self._disable_detail_periods.append(TimePeriodRule.from_alipay_dict(i))
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def discount_calc_type(self):
        return self._discount_calc_type

    @discount_calc_type.setter
    def discount_calc_type(self, value):
        self._discount_calc_type = value
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        self._floor_amount = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        if isinstance(value, list):
            self._goods_id = list()
            for i in value:
                self._goods_id.append(i)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def usable_detail_period(self):
        return self._usable_detail_period

    @usable_detail_period.setter
    def usable_detail_period(self, value):
        if isinstance(value, list):
            self._usable_detail_period = list()
            for i in value:
                if isinstance(i, TimePeriodRule):
                    self._usable_detail_period.append(i)
                else:
                    self._usable_detail_period.append(TimePeriodRule.from_alipay_dict(i))
    @property
    def usable_end_time(self):
        return self._usable_end_time

    @usable_end_time.setter
    def usable_end_time(self, value):
        self._usable_end_time = value
    @property
    def usable_start_time(self):
        return self._usable_start_time

    @usable_start_time.setter
    def usable_start_time(self, value):
        self._usable_start_time = value
    @property
    def usable_time_type(self):
        return self._usable_time_type

    @usable_time_type.setter
    def usable_time_type(self, value):
        self._usable_time_type = value
    @property
    def voucher_description(self):
        return self._voucher_description

    @voucher_description.setter
    def voucher_description(self, value):
        self._voucher_description = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.disable_detail_periods:
            if isinstance(self.disable_detail_periods, list):
                for i in range(0, len(self.disable_detail_periods)):
                    element = self.disable_detail_periods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disable_detail_periods[i] = element.to_alipay_dict()
            if hasattr(self.disable_detail_periods, 'to_alipay_dict'):
                params['disable_detail_periods'] = self.disable_detail_periods.to_alipay_dict()
            else:
                params['disable_detail_periods'] = self.disable_detail_periods
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.discount_calc_type:
            if hasattr(self.discount_calc_type, 'to_alipay_dict'):
                params['discount_calc_type'] = self.discount_calc_type.to_alipay_dict()
            else:
                params['discount_calc_type'] = self.discount_calc_type
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        if self.goods_id:
            if isinstance(self.goods_id, list):
                for i in range(0, len(self.goods_id)):
                    element = self.goods_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_id[i] = element.to_alipay_dict()
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.usable_detail_period:
            if isinstance(self.usable_detail_period, list):
                for i in range(0, len(self.usable_detail_period)):
                    element = self.usable_detail_period[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.usable_detail_period[i] = element.to_alipay_dict()
            if hasattr(self.usable_detail_period, 'to_alipay_dict'):
                params['usable_detail_period'] = self.usable_detail_period.to_alipay_dict()
            else:
                params['usable_detail_period'] = self.usable_detail_period
        if self.usable_end_time:
            if hasattr(self.usable_end_time, 'to_alipay_dict'):
                params['usable_end_time'] = self.usable_end_time.to_alipay_dict()
            else:
                params['usable_end_time'] = self.usable_end_time
        if self.usable_start_time:
            if hasattr(self.usable_start_time, 'to_alipay_dict'):
                params['usable_start_time'] = self.usable_start_time.to_alipay_dict()
            else:
                params['usable_start_time'] = self.usable_start_time
        if self.usable_time_type:
            if hasattr(self.usable_time_type, 'to_alipay_dict'):
                params['usable_time_type'] = self.usable_time_type.to_alipay_dict()
            else:
                params['usable_time_type'] = self.usable_time_type
        if self.voucher_description:
            if hasattr(self.voucher_description, 'to_alipay_dict'):
                params['voucher_description'] = self.voucher_description.to_alipay_dict()
            else:
                params['voucher_description'] = self.voucher_description
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
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
        o = VoucherTemplateInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'disable_detail_periods' in d:
            o.disable_detail_periods = d['disable_detail_periods']
        if 'discount' in d:
            o.discount = d['discount']
        if 'discount_calc_type' in d:
            o.discount_calc_type = d['discount_calc_type']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'usable_detail_period' in d:
            o.usable_detail_period = d['usable_detail_period']
        if 'usable_end_time' in d:
            o.usable_end_time = d['usable_end_time']
        if 'usable_start_time' in d:
            o.usable_start_time = d['usable_start_time']
        if 'usable_time_type' in d:
            o.usable_time_type = d['usable_time_type']
        if 'voucher_description' in d:
            o.voucher_description = d['voucher_description']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


