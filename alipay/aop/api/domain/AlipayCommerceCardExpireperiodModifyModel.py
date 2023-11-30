#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCardExpireperiodModifyModel(object):

    def __init__(self):
        self._appoint_date = None
        self._card_id = None
        self._industry_solution_type = None
        self._open_id = None
        self._out_biz_no = None
        self._period = None
        self._period_type = None
        self._period_value = None
        self._update_type = None
        self._user_id = None

    @property
    def appoint_date(self):
        return self._appoint_date

    @appoint_date.setter
    def appoint_date(self, value):
        self._appoint_date = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def industry_solution_type(self):
        return self._industry_solution_type

    @industry_solution_type.setter
    def industry_solution_type(self, value):
        self._industry_solution_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def period_value(self):
        return self._period_value

    @period_value.setter
    def period_value(self, value):
        self._period_value = value
    @property
    def update_type(self):
        return self._update_type

    @update_type.setter
    def update_type(self, value):
        self._update_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_date:
            if hasattr(self.appoint_date, 'to_alipay_dict'):
                params['appoint_date'] = self.appoint_date.to_alipay_dict()
            else:
                params['appoint_date'] = self.appoint_date
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.industry_solution_type:
            if hasattr(self.industry_solution_type, 'to_alipay_dict'):
                params['industry_solution_type'] = self.industry_solution_type.to_alipay_dict()
            else:
                params['industry_solution_type'] = self.industry_solution_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.period_value:
            if hasattr(self.period_value, 'to_alipay_dict'):
                params['period_value'] = self.period_value.to_alipay_dict()
            else:
                params['period_value'] = self.period_value
        if self.update_type:
            if hasattr(self.update_type, 'to_alipay_dict'):
                params['update_type'] = self.update_type.to_alipay_dict()
            else:
                params['update_type'] = self.update_type
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
        o = AlipayCommerceCardExpireperiodModifyModel()
        if 'appoint_date' in d:
            o.appoint_date = d['appoint_date']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'industry_solution_type' in d:
            o.industry_solution_type = d['industry_solution_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'period' in d:
            o.period = d['period']
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'period_value' in d:
            o.period_value = d['period_value']
        if 'update_type' in d:
            o.update_type = d['update_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


