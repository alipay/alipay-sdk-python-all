#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetEcoIotOrderInfo(object):

    def __init__(self):
        self._apply_date = None
        self._apply_order_id = None
        self._first_bind_date = None
        self._is_active = None
        self._is_rebate_eligible = None
        self._out_biz_no = None
        self._sn = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def first_bind_date(self):
        return self._first_bind_date

    @first_bind_date.setter
    def first_bind_date(self, value):
        self._first_bind_date = value
    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value
    @property
    def is_rebate_eligible(self):
        return self._is_rebate_eligible

    @is_rebate_eligible.setter
    def is_rebate_eligible(self, value):
        self._is_rebate_eligible = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_order_id:
            if hasattr(self.apply_order_id, 'to_alipay_dict'):
                params['apply_order_id'] = self.apply_order_id.to_alipay_dict()
            else:
                params['apply_order_id'] = self.apply_order_id
        if self.first_bind_date:
            if hasattr(self.first_bind_date, 'to_alipay_dict'):
                params['first_bind_date'] = self.first_bind_date.to_alipay_dict()
            else:
                params['first_bind_date'] = self.first_bind_date
        if self.is_active:
            if hasattr(self.is_active, 'to_alipay_dict'):
                params['is_active'] = self.is_active.to_alipay_dict()
            else:
                params['is_active'] = self.is_active
        if self.is_rebate_eligible:
            if hasattr(self.is_rebate_eligible, 'to_alipay_dict'):
                params['is_rebate_eligible'] = self.is_rebate_eligible.to_alipay_dict()
            else:
                params['is_rebate_eligible'] = self.is_rebate_eligible
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoIotOrderInfo()
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_order_id' in d:
            o.apply_order_id = d['apply_order_id']
        if 'first_bind_date' in d:
            o.first_bind_date = d['first_bind_date']
        if 'is_active' in d:
            o.is_active = d['is_active']
        if 'is_rebate_eligible' in d:
            o.is_rebate_eligible = d['is_rebate_eligible']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sn' in d:
            o.sn = d['sn']
        return o


