#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JointAccountQuotaRespDTO(object):

    def __init__(self):
        self._custom_begin_date = None
        self._custom_end_date = None
        self._quota_dimension = None
        self._quota_remain = None
        self._quota_remain_count = None
        self._quota_total = None
        self._quota_used = None

    @property
    def custom_begin_date(self):
        return self._custom_begin_date

    @custom_begin_date.setter
    def custom_begin_date(self, value):
        self._custom_begin_date = value
    @property
    def custom_end_date(self):
        return self._custom_end_date

    @custom_end_date.setter
    def custom_end_date(self, value):
        self._custom_end_date = value
    @property
    def quota_dimension(self):
        return self._quota_dimension

    @quota_dimension.setter
    def quota_dimension(self, value):
        self._quota_dimension = value
    @property
    def quota_remain(self):
        return self._quota_remain

    @quota_remain.setter
    def quota_remain(self, value):
        self._quota_remain = value
    @property
    def quota_remain_count(self):
        return self._quota_remain_count

    @quota_remain_count.setter
    def quota_remain_count(self, value):
        self._quota_remain_count = value
    @property
    def quota_total(self):
        return self._quota_total

    @quota_total.setter
    def quota_total(self, value):
        self._quota_total = value
    @property
    def quota_used(self):
        return self._quota_used

    @quota_used.setter
    def quota_used(self, value):
        self._quota_used = value


    def to_alipay_dict(self):
        params = dict()
        if self.custom_begin_date:
            if hasattr(self.custom_begin_date, 'to_alipay_dict'):
                params['custom_begin_date'] = self.custom_begin_date.to_alipay_dict()
            else:
                params['custom_begin_date'] = self.custom_begin_date
        if self.custom_end_date:
            if hasattr(self.custom_end_date, 'to_alipay_dict'):
                params['custom_end_date'] = self.custom_end_date.to_alipay_dict()
            else:
                params['custom_end_date'] = self.custom_end_date
        if self.quota_dimension:
            if hasattr(self.quota_dimension, 'to_alipay_dict'):
                params['quota_dimension'] = self.quota_dimension.to_alipay_dict()
            else:
                params['quota_dimension'] = self.quota_dimension
        if self.quota_remain:
            if hasattr(self.quota_remain, 'to_alipay_dict'):
                params['quota_remain'] = self.quota_remain.to_alipay_dict()
            else:
                params['quota_remain'] = self.quota_remain
        if self.quota_remain_count:
            if hasattr(self.quota_remain_count, 'to_alipay_dict'):
                params['quota_remain_count'] = self.quota_remain_count.to_alipay_dict()
            else:
                params['quota_remain_count'] = self.quota_remain_count
        if self.quota_total:
            if hasattr(self.quota_total, 'to_alipay_dict'):
                params['quota_total'] = self.quota_total.to_alipay_dict()
            else:
                params['quota_total'] = self.quota_total
        if self.quota_used:
            if hasattr(self.quota_used, 'to_alipay_dict'):
                params['quota_used'] = self.quota_used.to_alipay_dict()
            else:
                params['quota_used'] = self.quota_used
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JointAccountQuotaRespDTO()
        if 'custom_begin_date' in d:
            o.custom_begin_date = d['custom_begin_date']
        if 'custom_end_date' in d:
            o.custom_end_date = d['custom_end_date']
        if 'quota_dimension' in d:
            o.quota_dimension = d['quota_dimension']
        if 'quota_remain' in d:
            o.quota_remain = d['quota_remain']
        if 'quota_remain_count' in d:
            o.quota_remain_count = d['quota_remain_count']
        if 'quota_total' in d:
            o.quota_total = d['quota_total']
        if 'quota_used' in d:
            o.quota_used = d['quota_used']
        return o


