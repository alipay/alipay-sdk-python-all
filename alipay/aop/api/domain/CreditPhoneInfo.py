#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditPhoneInfo(object):

    def __init__(self):
        self._busi_level = None
        self._busi_name = None
        self._busi_type = None
        self._due_date = None
        self._first_month_price = None
        self._installment_numbers = None
        self._isp_abbr_cn = None
        self._max_amount_per_installment = None
        self._overdue_days = None
        self._pay_date = None
        self._pre_busi_level = None
        self._province = None
        self._require_month_count = None
        self._service_mobile = None
        self._spu_id = None
        self._total_bonus = None

    @property
    def busi_level(self):
        return self._busi_level

    @busi_level.setter
    def busi_level(self, value):
        self._busi_level = value
    @property
    def busi_name(self):
        return self._busi_name

    @busi_name.setter
    def busi_name(self, value):
        self._busi_name = value
    @property
    def busi_type(self):
        return self._busi_type

    @busi_type.setter
    def busi_type(self, value):
        self._busi_type = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def first_month_price(self):
        return self._first_month_price

    @first_month_price.setter
    def first_month_price(self, value):
        self._first_month_price = value
    @property
    def installment_numbers(self):
        return self._installment_numbers

    @installment_numbers.setter
    def installment_numbers(self, value):
        self._installment_numbers = value
    @property
    def isp_abbr_cn(self):
        return self._isp_abbr_cn

    @isp_abbr_cn.setter
    def isp_abbr_cn(self, value):
        self._isp_abbr_cn = value
    @property
    def max_amount_per_installment(self):
        return self._max_amount_per_installment

    @max_amount_per_installment.setter
    def max_amount_per_installment(self, value):
        self._max_amount_per_installment = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pre_busi_level(self):
        return self._pre_busi_level

    @pre_busi_level.setter
    def pre_busi_level(self, value):
        self._pre_busi_level = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def require_month_count(self):
        return self._require_month_count

    @require_month_count.setter
    def require_month_count(self, value):
        self._require_month_count = value
    @property
    def service_mobile(self):
        return self._service_mobile

    @service_mobile.setter
    def service_mobile(self, value):
        self._service_mobile = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def total_bonus(self):
        return self._total_bonus

    @total_bonus.setter
    def total_bonus(self, value):
        self._total_bonus = value


    def to_alipay_dict(self):
        params = dict()
        if self.busi_level:
            if hasattr(self.busi_level, 'to_alipay_dict'):
                params['busi_level'] = self.busi_level.to_alipay_dict()
            else:
                params['busi_level'] = self.busi_level
        if self.busi_name:
            if hasattr(self.busi_name, 'to_alipay_dict'):
                params['busi_name'] = self.busi_name.to_alipay_dict()
            else:
                params['busi_name'] = self.busi_name
        if self.busi_type:
            if hasattr(self.busi_type, 'to_alipay_dict'):
                params['busi_type'] = self.busi_type.to_alipay_dict()
            else:
                params['busi_type'] = self.busi_type
        if self.due_date:
            if hasattr(self.due_date, 'to_alipay_dict'):
                params['due_date'] = self.due_date.to_alipay_dict()
            else:
                params['due_date'] = self.due_date
        if self.first_month_price:
            if hasattr(self.first_month_price, 'to_alipay_dict'):
                params['first_month_price'] = self.first_month_price.to_alipay_dict()
            else:
                params['first_month_price'] = self.first_month_price
        if self.installment_numbers:
            if hasattr(self.installment_numbers, 'to_alipay_dict'):
                params['installment_numbers'] = self.installment_numbers.to_alipay_dict()
            else:
                params['installment_numbers'] = self.installment_numbers
        if self.isp_abbr_cn:
            if hasattr(self.isp_abbr_cn, 'to_alipay_dict'):
                params['isp_abbr_cn'] = self.isp_abbr_cn.to_alipay_dict()
            else:
                params['isp_abbr_cn'] = self.isp_abbr_cn
        if self.max_amount_per_installment:
            if hasattr(self.max_amount_per_installment, 'to_alipay_dict'):
                params['max_amount_per_installment'] = self.max_amount_per_installment.to_alipay_dict()
            else:
                params['max_amount_per_installment'] = self.max_amount_per_installment
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pre_busi_level:
            if hasattr(self.pre_busi_level, 'to_alipay_dict'):
                params['pre_busi_level'] = self.pre_busi_level.to_alipay_dict()
            else:
                params['pre_busi_level'] = self.pre_busi_level
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.require_month_count:
            if hasattr(self.require_month_count, 'to_alipay_dict'):
                params['require_month_count'] = self.require_month_count.to_alipay_dict()
            else:
                params['require_month_count'] = self.require_month_count
        if self.service_mobile:
            if hasattr(self.service_mobile, 'to_alipay_dict'):
                params['service_mobile'] = self.service_mobile.to_alipay_dict()
            else:
                params['service_mobile'] = self.service_mobile
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
        if self.total_bonus:
            if hasattr(self.total_bonus, 'to_alipay_dict'):
                params['total_bonus'] = self.total_bonus.to_alipay_dict()
            else:
                params['total_bonus'] = self.total_bonus
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditPhoneInfo()
        if 'busi_level' in d:
            o.busi_level = d['busi_level']
        if 'busi_name' in d:
            o.busi_name = d['busi_name']
        if 'busi_type' in d:
            o.busi_type = d['busi_type']
        if 'due_date' in d:
            o.due_date = d['due_date']
        if 'first_month_price' in d:
            o.first_month_price = d['first_month_price']
        if 'installment_numbers' in d:
            o.installment_numbers = d['installment_numbers']
        if 'isp_abbr_cn' in d:
            o.isp_abbr_cn = d['isp_abbr_cn']
        if 'max_amount_per_installment' in d:
            o.max_amount_per_installment = d['max_amount_per_installment']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pre_busi_level' in d:
            o.pre_busi_level = d['pre_busi_level']
        if 'province' in d:
            o.province = d['province']
        if 'require_month_count' in d:
            o.require_month_count = d['require_month_count']
        if 'service_mobile' in d:
            o.service_mobile = d['service_mobile']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'total_bonus' in d:
            o.total_bonus = d['total_bonus']
        return o


