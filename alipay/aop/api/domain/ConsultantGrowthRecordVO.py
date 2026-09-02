#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultantGrowthRecordVO(object):

    def __init__(self):
        self._age_in_months = None
        self._bmi = None
        self._growth_height = None
        self._growth_weight = None
        self._head_circumference = None
        self._record_biz_id = None
        self._record_date = None

    @property
    def age_in_months(self):
        return self._age_in_months

    @age_in_months.setter
    def age_in_months(self, value):
        self._age_in_months = value
    @property
    def bmi(self):
        return self._bmi

    @bmi.setter
    def bmi(self, value):
        self._bmi = value
    @property
    def growth_height(self):
        return self._growth_height

    @growth_height.setter
    def growth_height(self, value):
        self._growth_height = value
    @property
    def growth_weight(self):
        return self._growth_weight

    @growth_weight.setter
    def growth_weight(self, value):
        self._growth_weight = value
    @property
    def head_circumference(self):
        return self._head_circumference

    @head_circumference.setter
    def head_circumference(self, value):
        self._head_circumference = value
    @property
    def record_biz_id(self):
        return self._record_biz_id

    @record_biz_id.setter
    def record_biz_id(self, value):
        self._record_biz_id = value
    @property
    def record_date(self):
        return self._record_date

    @record_date.setter
    def record_date(self, value):
        self._record_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_in_months:
            if hasattr(self.age_in_months, 'to_alipay_dict'):
                params['age_in_months'] = self.age_in_months.to_alipay_dict()
            else:
                params['age_in_months'] = self.age_in_months
        if self.bmi:
            if hasattr(self.bmi, 'to_alipay_dict'):
                params['bmi'] = self.bmi.to_alipay_dict()
            else:
                params['bmi'] = self.bmi
        if self.growth_height:
            if hasattr(self.growth_height, 'to_alipay_dict'):
                params['growth_height'] = self.growth_height.to_alipay_dict()
            else:
                params['growth_height'] = self.growth_height
        if self.growth_weight:
            if hasattr(self.growth_weight, 'to_alipay_dict'):
                params['growth_weight'] = self.growth_weight.to_alipay_dict()
            else:
                params['growth_weight'] = self.growth_weight
        if self.head_circumference:
            if hasattr(self.head_circumference, 'to_alipay_dict'):
                params['head_circumference'] = self.head_circumference.to_alipay_dict()
            else:
                params['head_circumference'] = self.head_circumference
        if self.record_biz_id:
            if hasattr(self.record_biz_id, 'to_alipay_dict'):
                params['record_biz_id'] = self.record_biz_id.to_alipay_dict()
            else:
                params['record_biz_id'] = self.record_biz_id
        if self.record_date:
            if hasattr(self.record_date, 'to_alipay_dict'):
                params['record_date'] = self.record_date.to_alipay_dict()
            else:
                params['record_date'] = self.record_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultantGrowthRecordVO()
        if 'age_in_months' in d:
            o.age_in_months = d['age_in_months']
        if 'bmi' in d:
            o.bmi = d['bmi']
        if 'growth_height' in d:
            o.growth_height = d['growth_height']
        if 'growth_weight' in d:
            o.growth_weight = d['growth_weight']
        if 'head_circumference' in d:
            o.head_circumference = d['head_circumference']
        if 'record_biz_id' in d:
            o.record_biz_id = d['record_biz_id']
        if 'record_date' in d:
            o.record_date = d['record_date']
        return o


