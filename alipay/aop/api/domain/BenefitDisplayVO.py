#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO
from alipay.aop.api.domain.MultiCurrencyMoneyDTO import MultiCurrencyMoneyDTO


class BenefitDisplayVO(object):

    def __init__(self):
        self._active_time = None
        self._benefit_id = None
        self._benefit_source = None
        self._benefit_type = None
        self._discount_amount = None
        self._discount_desc = None
        self._discount_icon_url = None
        self._discount_name = None
        self._discount_percentage = None
        self._expired_time = None
        self._extend_info = None
        self._goods_id = None
        self._threshold_amount = None
        self._usage_condition = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_source(self):
        return self._benefit_source

    @benefit_source.setter
    def benefit_source(self, value):
        self._benefit_source = value
    @property
    def benefit_type(self):
        return self._benefit_type

    @benefit_type.setter
    def benefit_type(self, value):
        self._benefit_type = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._discount_amount = value
        else:
            self._discount_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
    @property
    def discount_icon_url(self):
        return self._discount_icon_url

    @discount_icon_url.setter
    def discount_icon_url(self, value):
        self._discount_icon_url = value
    @property
    def discount_name(self):
        return self._discount_name

    @discount_name.setter
    def discount_name(self, value):
        self._discount_name = value
    @property
    def discount_percentage(self):
        return self._discount_percentage

    @discount_percentage.setter
    def discount_percentage(self, value):
        self._discount_percentage = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, value):
        self._goods_id = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyDTO):
            self._threshold_amount = value
        else:
            self._threshold_amount = MultiCurrencyMoneyDTO.from_alipay_dict(value)
    @property
    def usage_condition(self):
        return self._usage_condition

    @usage_condition.setter
    def usage_condition(self, value):
        self._usage_condition = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_source:
            if hasattr(self.benefit_source, 'to_alipay_dict'):
                params['benefit_source'] = self.benefit_source.to_alipay_dict()
            else:
                params['benefit_source'] = self.benefit_source
        if self.benefit_type:
            if hasattr(self.benefit_type, 'to_alipay_dict'):
                params['benefit_type'] = self.benefit_type.to_alipay_dict()
            else:
                params['benefit_type'] = self.benefit_type
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
        if self.discount_icon_url:
            if hasattr(self.discount_icon_url, 'to_alipay_dict'):
                params['discount_icon_url'] = self.discount_icon_url.to_alipay_dict()
            else:
                params['discount_icon_url'] = self.discount_icon_url
        if self.discount_name:
            if hasattr(self.discount_name, 'to_alipay_dict'):
                params['discount_name'] = self.discount_name.to_alipay_dict()
            else:
                params['discount_name'] = self.discount_name
        if self.discount_percentage:
            if hasattr(self.discount_percentage, 'to_alipay_dict'):
                params['discount_percentage'] = self.discount_percentage.to_alipay_dict()
            else:
                params['discount_percentage'] = self.discount_percentage
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.goods_id:
            if hasattr(self.goods_id, 'to_alipay_dict'):
                params['goods_id'] = self.goods_id.to_alipay_dict()
            else:
                params['goods_id'] = self.goods_id
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.usage_condition:
            if hasattr(self.usage_condition, 'to_alipay_dict'):
                params['usage_condition'] = self.usage_condition.to_alipay_dict()
            else:
                params['usage_condition'] = self.usage_condition
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDisplayVO()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_source' in d:
            o.benefit_source = d['benefit_source']
        if 'benefit_type' in d:
            o.benefit_type = d['benefit_type']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'discount_icon_url' in d:
            o.discount_icon_url = d['discount_icon_url']
        if 'discount_name' in d:
            o.discount_name = d['discount_name']
        if 'discount_percentage' in d:
            o.discount_percentage = d['discount_percentage']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'goods_id' in d:
            o.goods_id = d['goods_id']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'usage_condition' in d:
            o.usage_condition = d['usage_condition']
        return o


