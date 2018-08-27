#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BenefitGradeConfig import BenefitGradeConfig


class AlipayUserNewbenefitModifyModel(object):

    def __init__(self):
        self._area_code = None
        self._benefit_id = None
        self._benefit_name = None
        self._benefit_sub_title = None
        self._description = None
        self._eligible_grade_desc = None
        self._end_dt = None
        self._exchange_rule_ids = None
        self._grade_config = None
        self._icon_url = None
        self._remove_grades = None
        self._start_dt = None

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_sub_title(self):
        return self._benefit_sub_title

    @benefit_sub_title.setter
    def benefit_sub_title(self, value):
        self._benefit_sub_title = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def eligible_grade_desc(self):
        return self._eligible_grade_desc

    @eligible_grade_desc.setter
    def eligible_grade_desc(self, value):
        self._eligible_grade_desc = value
    @property
    def end_dt(self):
        return self._end_dt

    @end_dt.setter
    def end_dt(self, value):
        self._end_dt = value
    @property
    def exchange_rule_ids(self):
        return self._exchange_rule_ids

    @exchange_rule_ids.setter
    def exchange_rule_ids(self, value):
        self._exchange_rule_ids = value
    @property
    def grade_config(self):
        return self._grade_config

    @grade_config.setter
    def grade_config(self, value):
        if isinstance(value, list):
            self._grade_config = list()
            for i in value:
                if isinstance(i, BenefitGradeConfig):
                    self._grade_config.append(i)
                else:
                    self._grade_config.append(BenefitGradeConfig.from_alipay_dict(i))
    @property
    def icon_url(self):
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        self._icon_url = value
    @property
    def remove_grades(self):
        return self._remove_grades

    @remove_grades.setter
    def remove_grades(self, value):
        self._remove_grades = value
    @property
    def start_dt(self):
        return self._start_dt

    @start_dt.setter
    def start_dt(self, value):
        self._start_dt = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_code:
            if hasattr(self.area_code, 'to_alipay_dict'):
                params['area_code'] = self.area_code.to_alipay_dict()
            else:
                params['area_code'] = self.area_code
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_sub_title:
            if hasattr(self.benefit_sub_title, 'to_alipay_dict'):
                params['benefit_sub_title'] = self.benefit_sub_title.to_alipay_dict()
            else:
                params['benefit_sub_title'] = self.benefit_sub_title
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.eligible_grade_desc:
            if hasattr(self.eligible_grade_desc, 'to_alipay_dict'):
                params['eligible_grade_desc'] = self.eligible_grade_desc.to_alipay_dict()
            else:
                params['eligible_grade_desc'] = self.eligible_grade_desc
        if self.end_dt:
            if hasattr(self.end_dt, 'to_alipay_dict'):
                params['end_dt'] = self.end_dt.to_alipay_dict()
            else:
                params['end_dt'] = self.end_dt
        if self.exchange_rule_ids:
            if hasattr(self.exchange_rule_ids, 'to_alipay_dict'):
                params['exchange_rule_ids'] = self.exchange_rule_ids.to_alipay_dict()
            else:
                params['exchange_rule_ids'] = self.exchange_rule_ids
        if self.grade_config:
            if isinstance(self.grade_config, list):
                for i in range(0, len(self.grade_config)):
                    element = self.grade_config[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.grade_config[i] = element.to_alipay_dict()
            if hasattr(self.grade_config, 'to_alipay_dict'):
                params['grade_config'] = self.grade_config.to_alipay_dict()
            else:
                params['grade_config'] = self.grade_config
        if self.icon_url:
            if hasattr(self.icon_url, 'to_alipay_dict'):
                params['icon_url'] = self.icon_url.to_alipay_dict()
            else:
                params['icon_url'] = self.icon_url
        if self.remove_grades:
            if hasattr(self.remove_grades, 'to_alipay_dict'):
                params['remove_grades'] = self.remove_grades.to_alipay_dict()
            else:
                params['remove_grades'] = self.remove_grades
        if self.start_dt:
            if hasattr(self.start_dt, 'to_alipay_dict'):
                params['start_dt'] = self.start_dt.to_alipay_dict()
            else:
                params['start_dt'] = self.start_dt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserNewbenefitModifyModel()
        if 'area_code' in d:
            o.area_code = d['area_code']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_sub_title' in d:
            o.benefit_sub_title = d['benefit_sub_title']
        if 'description' in d:
            o.description = d['description']
        if 'eligible_grade_desc' in d:
            o.eligible_grade_desc = d['eligible_grade_desc']
        if 'end_dt' in d:
            o.end_dt = d['end_dt']
        if 'exchange_rule_ids' in d:
            o.exchange_rule_ids = d['exchange_rule_ids']
        if 'grade_config' in d:
            o.grade_config = d['grade_config']
        if 'icon_url' in d:
            o.icon_url = d['icon_url']
        if 'remove_grades' in d:
            o.remove_grades = d['remove_grades']
        if 'start_dt' in d:
            o.start_dt = d['start_dt']
        return o


