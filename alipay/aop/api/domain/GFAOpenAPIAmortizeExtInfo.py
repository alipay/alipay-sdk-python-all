#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GFAOpenAPIAmortizeExtInfo(object):

    def __init__(self):
        self._amortize_amount = None
        self._amortize_period_type = None
        self._amortize_type = None
        self._amortize_volume = None
        self._gmt_end = None
        self._gmt_valid = None
        self._total_amortize_amount = None

    @property
    def amortize_amount(self):
        return self._amortize_amount

    @amortize_amount.setter
    def amortize_amount(self, value):
        self._amortize_amount = value
    @property
    def amortize_period_type(self):
        return self._amortize_period_type

    @amortize_period_type.setter
    def amortize_period_type(self, value):
        self._amortize_period_type = value
    @property
    def amortize_type(self):
        return self._amortize_type

    @amortize_type.setter
    def amortize_type(self, value):
        self._amortize_type = value
    @property
    def amortize_volume(self):
        return self._amortize_volume

    @amortize_volume.setter
    def amortize_volume(self, value):
        self._amortize_volume = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def total_amortize_amount(self):
        return self._total_amortize_amount

    @total_amortize_amount.setter
    def total_amortize_amount(self, value):
        self._total_amortize_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amortize_amount:
            if hasattr(self.amortize_amount, 'to_alipay_dict'):
                params['amortize_amount'] = self.amortize_amount.to_alipay_dict()
            else:
                params['amortize_amount'] = self.amortize_amount
        if self.amortize_period_type:
            if hasattr(self.amortize_period_type, 'to_alipay_dict'):
                params['amortize_period_type'] = self.amortize_period_type.to_alipay_dict()
            else:
                params['amortize_period_type'] = self.amortize_period_type
        if self.amortize_type:
            if hasattr(self.amortize_type, 'to_alipay_dict'):
                params['amortize_type'] = self.amortize_type.to_alipay_dict()
            else:
                params['amortize_type'] = self.amortize_type
        if self.amortize_volume:
            if hasattr(self.amortize_volume, 'to_alipay_dict'):
                params['amortize_volume'] = self.amortize_volume.to_alipay_dict()
            else:
                params['amortize_volume'] = self.amortize_volume
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.total_amortize_amount:
            if hasattr(self.total_amortize_amount, 'to_alipay_dict'):
                params['total_amortize_amount'] = self.total_amortize_amount.to_alipay_dict()
            else:
                params['total_amortize_amount'] = self.total_amortize_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIAmortizeExtInfo()
        if 'amortize_amount' in d:
            o.amortize_amount = d['amortize_amount']
        if 'amortize_period_type' in d:
            o.amortize_period_type = d['amortize_period_type']
        if 'amortize_type' in d:
            o.amortize_type = d['amortize_type']
        if 'amortize_volume' in d:
            o.amortize_volume = d['amortize_volume']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'total_amortize_amount' in d:
            o.total_amortize_amount = d['total_amortize_amount']
        return o


