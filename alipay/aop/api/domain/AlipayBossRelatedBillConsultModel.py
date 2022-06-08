#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossRelatedBillConsultModel(object):

    def __init__(self):
        self._biz_date = None
        self._extra_infos = None
        self._is_whole_month_valid = None
        self._opposite_fund_type = None
        self._opposite_fund_value = None
        self._opposite_settle_type = None
        self._opposite_settle_value = None
        self._self_type = None
        self._self_value = None

    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def extra_infos(self):
        return self._extra_infos

    @extra_infos.setter
    def extra_infos(self, value):
        self._extra_infos = value
    @property
    def is_whole_month_valid(self):
        return self._is_whole_month_valid

    @is_whole_month_valid.setter
    def is_whole_month_valid(self, value):
        self._is_whole_month_valid = value
    @property
    def opposite_fund_type(self):
        return self._opposite_fund_type

    @opposite_fund_type.setter
    def opposite_fund_type(self, value):
        self._opposite_fund_type = value
    @property
    def opposite_fund_value(self):
        return self._opposite_fund_value

    @opposite_fund_value.setter
    def opposite_fund_value(self, value):
        self._opposite_fund_value = value
    @property
    def opposite_settle_type(self):
        return self._opposite_settle_type

    @opposite_settle_type.setter
    def opposite_settle_type(self, value):
        self._opposite_settle_type = value
    @property
    def opposite_settle_value(self):
        return self._opposite_settle_value

    @opposite_settle_value.setter
    def opposite_settle_value(self, value):
        self._opposite_settle_value = value
    @property
    def self_type(self):
        return self._self_type

    @self_type.setter
    def self_type(self, value):
        self._self_type = value
    @property
    def self_value(self):
        return self._self_value

    @self_value.setter
    def self_value(self, value):
        self._self_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.extra_infos:
            if hasattr(self.extra_infos, 'to_alipay_dict'):
                params['extra_infos'] = self.extra_infos.to_alipay_dict()
            else:
                params['extra_infos'] = self.extra_infos
        if self.is_whole_month_valid:
            if hasattr(self.is_whole_month_valid, 'to_alipay_dict'):
                params['is_whole_month_valid'] = self.is_whole_month_valid.to_alipay_dict()
            else:
                params['is_whole_month_valid'] = self.is_whole_month_valid
        if self.opposite_fund_type:
            if hasattr(self.opposite_fund_type, 'to_alipay_dict'):
                params['opposite_fund_type'] = self.opposite_fund_type.to_alipay_dict()
            else:
                params['opposite_fund_type'] = self.opposite_fund_type
        if self.opposite_fund_value:
            if hasattr(self.opposite_fund_value, 'to_alipay_dict'):
                params['opposite_fund_value'] = self.opposite_fund_value.to_alipay_dict()
            else:
                params['opposite_fund_value'] = self.opposite_fund_value
        if self.opposite_settle_type:
            if hasattr(self.opposite_settle_type, 'to_alipay_dict'):
                params['opposite_settle_type'] = self.opposite_settle_type.to_alipay_dict()
            else:
                params['opposite_settle_type'] = self.opposite_settle_type
        if self.opposite_settle_value:
            if hasattr(self.opposite_settle_value, 'to_alipay_dict'):
                params['opposite_settle_value'] = self.opposite_settle_value.to_alipay_dict()
            else:
                params['opposite_settle_value'] = self.opposite_settle_value
        if self.self_type:
            if hasattr(self.self_type, 'to_alipay_dict'):
                params['self_type'] = self.self_type.to_alipay_dict()
            else:
                params['self_type'] = self.self_type
        if self.self_value:
            if hasattr(self.self_value, 'to_alipay_dict'):
                params['self_value'] = self.self_value.to_alipay_dict()
            else:
                params['self_value'] = self.self_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossRelatedBillConsultModel()
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'extra_infos' in d:
            o.extra_infos = d['extra_infos']
        if 'is_whole_month_valid' in d:
            o.is_whole_month_valid = d['is_whole_month_valid']
        if 'opposite_fund_type' in d:
            o.opposite_fund_type = d['opposite_fund_type']
        if 'opposite_fund_value' in d:
            o.opposite_fund_value = d['opposite_fund_value']
        if 'opposite_settle_type' in d:
            o.opposite_settle_type = d['opposite_settle_type']
        if 'opposite_settle_value' in d:
            o.opposite_settle_value = d['opposite_settle_value']
        if 'self_type' in d:
            o.self_type = d['self_type']
        if 'self_value' in d:
            o.self_value = d['self_value']
        return o


