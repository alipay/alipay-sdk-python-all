#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiPcreditbenefitHuabeijinPreconsultModel(object):

    def __init__(self):
        self._activity_id = None
        self._actual_amount = None
        self._camp_consult = None
        self._industry_value = None
        self._open_id = None
        self._order_desc = None
        self._precise_by_level = None
        self._user_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def actual_amount(self):
        return self._actual_amount

    @actual_amount.setter
    def actual_amount(self, value):
        self._actual_amount = value
    @property
    def camp_consult(self):
        return self._camp_consult

    @camp_consult.setter
    def camp_consult(self, value):
        self._camp_consult = value
    @property
    def industry_value(self):
        return self._industry_value

    @industry_value.setter
    def industry_value(self, value):
        self._industry_value = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_desc(self):
        return self._order_desc

    @order_desc.setter
    def order_desc(self, value):
        self._order_desc = value
    @property
    def precise_by_level(self):
        return self._precise_by_level

    @precise_by_level.setter
    def precise_by_level(self, value):
        self._precise_by_level = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.actual_amount:
            if hasattr(self.actual_amount, 'to_alipay_dict'):
                params['actual_amount'] = self.actual_amount.to_alipay_dict()
            else:
                params['actual_amount'] = self.actual_amount
        if self.camp_consult:
            if hasattr(self.camp_consult, 'to_alipay_dict'):
                params['camp_consult'] = self.camp_consult.to_alipay_dict()
            else:
                params['camp_consult'] = self.camp_consult
        if self.industry_value:
            if hasattr(self.industry_value, 'to_alipay_dict'):
                params['industry_value'] = self.industry_value.to_alipay_dict()
            else:
                params['industry_value'] = self.industry_value
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_desc:
            if hasattr(self.order_desc, 'to_alipay_dict'):
                params['order_desc'] = self.order_desc.to_alipay_dict()
            else:
                params['order_desc'] = self.order_desc
        if self.precise_by_level:
            if hasattr(self.precise_by_level, 'to_alipay_dict'):
                params['precise_by_level'] = self.precise_by_level.to_alipay_dict()
            else:
                params['precise_by_level'] = self.precise_by_level
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiPcreditbenefitHuabeijinPreconsultModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'actual_amount' in d:
            o.actual_amount = d['actual_amount']
        if 'camp_consult' in d:
            o.camp_consult = d['camp_consult']
        if 'industry_value' in d:
            o.industry_value = d['industry_value']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_desc' in d:
            o.order_desc = d['order_desc']
        if 'precise_by_level' in d:
            o.precise_by_level = d['precise_by_level']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


