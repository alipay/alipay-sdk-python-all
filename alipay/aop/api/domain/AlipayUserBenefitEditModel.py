#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserBenefitEditModel(object):

    def __init__(self):
        self._benefit_area_code = None
        self._benefit_icon_url = None
        self._benefit_id = None
        self._benefit_name = None
        self._benefit_name_as_area_subtitle = None
        self._benefit_page_url = None
        self._benefit_point = None
        self._benefit_rec_biz_id = None
        self._benefit_rec_type = None
        self._benefit_subtitle = None
        self._camp_id = None
        self._eligible_grade = None
        self._end_time = None
        self._exchange_rule_ids = None
        self._grade_discount = None
        self._start_time = None

    @property
    def benefit_area_code(self):
        return self._benefit_area_code

    @benefit_area_code.setter
    def benefit_area_code(self, value):
        self._benefit_area_code = value
    @property
    def benefit_icon_url(self):
        return self._benefit_icon_url

    @benefit_icon_url.setter
    def benefit_icon_url(self, value):
        self._benefit_icon_url = value
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
    def benefit_name_as_area_subtitle(self):
        return self._benefit_name_as_area_subtitle

    @benefit_name_as_area_subtitle.setter
    def benefit_name_as_area_subtitle(self, value):
        self._benefit_name_as_area_subtitle = value
    @property
    def benefit_page_url(self):
        return self._benefit_page_url

    @benefit_page_url.setter
    def benefit_page_url(self, value):
        self._benefit_page_url = value
    @property
    def benefit_point(self):
        return self._benefit_point

    @benefit_point.setter
    def benefit_point(self, value):
        self._benefit_point = value
    @property
    def benefit_rec_biz_id(self):
        return self._benefit_rec_biz_id

    @benefit_rec_biz_id.setter
    def benefit_rec_biz_id(self, value):
        self._benefit_rec_biz_id = value
    @property
    def benefit_rec_type(self):
        return self._benefit_rec_type

    @benefit_rec_type.setter
    def benefit_rec_type(self, value):
        self._benefit_rec_type = value
    @property
    def benefit_subtitle(self):
        return self._benefit_subtitle

    @benefit_subtitle.setter
    def benefit_subtitle(self, value):
        self._benefit_subtitle = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def eligible_grade(self):
        return self._eligible_grade

    @eligible_grade.setter
    def eligible_grade(self, value):
        self._eligible_grade = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def exchange_rule_ids(self):
        return self._exchange_rule_ids

    @exchange_rule_ids.setter
    def exchange_rule_ids(self, value):
        self._exchange_rule_ids = value
    @property
    def grade_discount(self):
        return self._grade_discount

    @grade_discount.setter
    def grade_discount(self, value):
        self._grade_discount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_area_code:
            if hasattr(self.benefit_area_code, 'to_alipay_dict'):
                params['benefit_area_code'] = self.benefit_area_code.to_alipay_dict()
            else:
                params['benefit_area_code'] = self.benefit_area_code
        if self.benefit_icon_url:
            if hasattr(self.benefit_icon_url, 'to_alipay_dict'):
                params['benefit_icon_url'] = self.benefit_icon_url.to_alipay_dict()
            else:
                params['benefit_icon_url'] = self.benefit_icon_url
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
        if self.benefit_name_as_area_subtitle:
            if hasattr(self.benefit_name_as_area_subtitle, 'to_alipay_dict'):
                params['benefit_name_as_area_subtitle'] = self.benefit_name_as_area_subtitle.to_alipay_dict()
            else:
                params['benefit_name_as_area_subtitle'] = self.benefit_name_as_area_subtitle
        if self.benefit_page_url:
            if hasattr(self.benefit_page_url, 'to_alipay_dict'):
                params['benefit_page_url'] = self.benefit_page_url.to_alipay_dict()
            else:
                params['benefit_page_url'] = self.benefit_page_url
        if self.benefit_point:
            if hasattr(self.benefit_point, 'to_alipay_dict'):
                params['benefit_point'] = self.benefit_point.to_alipay_dict()
            else:
                params['benefit_point'] = self.benefit_point
        if self.benefit_rec_biz_id:
            if hasattr(self.benefit_rec_biz_id, 'to_alipay_dict'):
                params['benefit_rec_biz_id'] = self.benefit_rec_biz_id.to_alipay_dict()
            else:
                params['benefit_rec_biz_id'] = self.benefit_rec_biz_id
        if self.benefit_rec_type:
            if hasattr(self.benefit_rec_type, 'to_alipay_dict'):
                params['benefit_rec_type'] = self.benefit_rec_type.to_alipay_dict()
            else:
                params['benefit_rec_type'] = self.benefit_rec_type
        if self.benefit_subtitle:
            if hasattr(self.benefit_subtitle, 'to_alipay_dict'):
                params['benefit_subtitle'] = self.benefit_subtitle.to_alipay_dict()
            else:
                params['benefit_subtitle'] = self.benefit_subtitle
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.eligible_grade:
            if hasattr(self.eligible_grade, 'to_alipay_dict'):
                params['eligible_grade'] = self.eligible_grade.to_alipay_dict()
            else:
                params['eligible_grade'] = self.eligible_grade
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.exchange_rule_ids:
            if hasattr(self.exchange_rule_ids, 'to_alipay_dict'):
                params['exchange_rule_ids'] = self.exchange_rule_ids.to_alipay_dict()
            else:
                params['exchange_rule_ids'] = self.exchange_rule_ids
        if self.grade_discount:
            if hasattr(self.grade_discount, 'to_alipay_dict'):
                params['grade_discount'] = self.grade_discount.to_alipay_dict()
            else:
                params['grade_discount'] = self.grade_discount
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserBenefitEditModel()
        if 'benefit_area_code' in d:
            o.benefit_area_code = d['benefit_area_code']
        if 'benefit_icon_url' in d:
            o.benefit_icon_url = d['benefit_icon_url']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_name_as_area_subtitle' in d:
            o.benefit_name_as_area_subtitle = d['benefit_name_as_area_subtitle']
        if 'benefit_page_url' in d:
            o.benefit_page_url = d['benefit_page_url']
        if 'benefit_point' in d:
            o.benefit_point = d['benefit_point']
        if 'benefit_rec_biz_id' in d:
            o.benefit_rec_biz_id = d['benefit_rec_biz_id']
        if 'benefit_rec_type' in d:
            o.benefit_rec_type = d['benefit_rec_type']
        if 'benefit_subtitle' in d:
            o.benefit_subtitle = d['benefit_subtitle']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'eligible_grade' in d:
            o.eligible_grade = d['eligible_grade']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'exchange_rule_ids' in d:
            o.exchange_rule_ids = d['exchange_rule_ids']
        if 'grade_discount' in d:
            o.grade_discount = d['grade_discount']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


