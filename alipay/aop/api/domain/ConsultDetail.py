#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultDetail(object):

    def __init__(self):
        self._area_preference = None
        self._budget_range = None
        self._move_in_date = None
        self._other_requirements = None
        self._room_type = None

    @property
    def area_preference(self):
        return self._area_preference

    @area_preference.setter
    def area_preference(self, value):
        self._area_preference = value
    @property
    def budget_range(self):
        return self._budget_range

    @budget_range.setter
    def budget_range(self, value):
        self._budget_range = value
    @property
    def move_in_date(self):
        return self._move_in_date

    @move_in_date.setter
    def move_in_date(self, value):
        self._move_in_date = value
    @property
    def other_requirements(self):
        return self._other_requirements

    @other_requirements.setter
    def other_requirements(self, value):
        self._other_requirements = value
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_preference:
            if hasattr(self.area_preference, 'to_alipay_dict'):
                params['area_preference'] = self.area_preference.to_alipay_dict()
            else:
                params['area_preference'] = self.area_preference
        if self.budget_range:
            if hasattr(self.budget_range, 'to_alipay_dict'):
                params['budget_range'] = self.budget_range.to_alipay_dict()
            else:
                params['budget_range'] = self.budget_range
        if self.move_in_date:
            if hasattr(self.move_in_date, 'to_alipay_dict'):
                params['move_in_date'] = self.move_in_date.to_alipay_dict()
            else:
                params['move_in_date'] = self.move_in_date
        if self.other_requirements:
            if hasattr(self.other_requirements, 'to_alipay_dict'):
                params['other_requirements'] = self.other_requirements.to_alipay_dict()
            else:
                params['other_requirements'] = self.other_requirements
        if self.room_type:
            if hasattr(self.room_type, 'to_alipay_dict'):
                params['room_type'] = self.room_type.to_alipay_dict()
            else:
                params['room_type'] = self.room_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultDetail()
        if 'area_preference' in d:
            o.area_preference = d['area_preference']
        if 'budget_range' in d:
            o.budget_range = d['budget_range']
        if 'move_in_date' in d:
            o.move_in_date = d['move_in_date']
        if 'other_requirements' in d:
            o.other_requirements = d['other_requirements']
        if 'room_type' in d:
            o.room_type = d['room_type']
        return o


