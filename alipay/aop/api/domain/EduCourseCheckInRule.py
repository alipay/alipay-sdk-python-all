#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduCheckInRuleConfig import EduCheckInRuleConfig


class EduCourseCheckInRule(object):

    def __init__(self):
        self._automatic_refresh = None
        self._course_desc = None
        self._course_id = None
        self._course_name = None
        self._course_rule_id = None
        self._course_rule_name = None
        self._day_of_week = None
        self._edu_check_in_rule = None
        self._enable_course_rule = None
        self._inst_id = None
        self._manual_close = None
        self._period_no_list = None
        self._refresh_qr_code_frequency = None
        self._semester_desc = None
        self._semester_id = None
        self._semester_name = None
        self._week_list = None

    @property
    def automatic_refresh(self):
        return self._automatic_refresh

    @automatic_refresh.setter
    def automatic_refresh(self, value):
        self._automatic_refresh = value
    @property
    def course_desc(self):
        return self._course_desc

    @course_desc.setter
    def course_desc(self, value):
        self._course_desc = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_rule_id(self):
        return self._course_rule_id

    @course_rule_id.setter
    def course_rule_id(self, value):
        self._course_rule_id = value
    @property
    def course_rule_name(self):
        return self._course_rule_name

    @course_rule_name.setter
    def course_rule_name(self, value):
        self._course_rule_name = value
    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        self._day_of_week = value
    @property
    def edu_check_in_rule(self):
        return self._edu_check_in_rule

    @edu_check_in_rule.setter
    def edu_check_in_rule(self, value):
        if isinstance(value, EduCheckInRuleConfig):
            self._edu_check_in_rule = value
        else:
            self._edu_check_in_rule = EduCheckInRuleConfig.from_alipay_dict(value)
    @property
    def enable_course_rule(self):
        return self._enable_course_rule

    @enable_course_rule.setter
    def enable_course_rule(self, value):
        self._enable_course_rule = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def manual_close(self):
        return self._manual_close

    @manual_close.setter
    def manual_close(self, value):
        self._manual_close = value
    @property
    def period_no_list(self):
        return self._period_no_list

    @period_no_list.setter
    def period_no_list(self, value):
        if isinstance(value, list):
            self._period_no_list = list()
            for i in value:
                self._period_no_list.append(i)
    @property
    def refresh_qr_code_frequency(self):
        return self._refresh_qr_code_frequency

    @refresh_qr_code_frequency.setter
    def refresh_qr_code_frequency(self, value):
        self._refresh_qr_code_frequency = value
    @property
    def semester_desc(self):
        return self._semester_desc

    @semester_desc.setter
    def semester_desc(self, value):
        self._semester_desc = value
    @property
    def semester_id(self):
        return self._semester_id

    @semester_id.setter
    def semester_id(self, value):
        self._semester_id = value
    @property
    def semester_name(self):
        return self._semester_name

    @semester_name.setter
    def semester_name(self, value):
        self._semester_name = value
    @property
    def week_list(self):
        return self._week_list

    @week_list.setter
    def week_list(self, value):
        if isinstance(value, list):
            self._week_list = list()
            for i in value:
                self._week_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.automatic_refresh:
            if hasattr(self.automatic_refresh, 'to_alipay_dict'):
                params['automatic_refresh'] = self.automatic_refresh.to_alipay_dict()
            else:
                params['automatic_refresh'] = self.automatic_refresh
        if self.course_desc:
            if hasattr(self.course_desc, 'to_alipay_dict'):
                params['course_desc'] = self.course_desc.to_alipay_dict()
            else:
                params['course_desc'] = self.course_desc
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.course_rule_id:
            if hasattr(self.course_rule_id, 'to_alipay_dict'):
                params['course_rule_id'] = self.course_rule_id.to_alipay_dict()
            else:
                params['course_rule_id'] = self.course_rule_id
        if self.course_rule_name:
            if hasattr(self.course_rule_name, 'to_alipay_dict'):
                params['course_rule_name'] = self.course_rule_name.to_alipay_dict()
            else:
                params['course_rule_name'] = self.course_rule_name
        if self.day_of_week:
            if hasattr(self.day_of_week, 'to_alipay_dict'):
                params['day_of_week'] = self.day_of_week.to_alipay_dict()
            else:
                params['day_of_week'] = self.day_of_week
        if self.edu_check_in_rule:
            if hasattr(self.edu_check_in_rule, 'to_alipay_dict'):
                params['edu_check_in_rule'] = self.edu_check_in_rule.to_alipay_dict()
            else:
                params['edu_check_in_rule'] = self.edu_check_in_rule
        if self.enable_course_rule:
            if hasattr(self.enable_course_rule, 'to_alipay_dict'):
                params['enable_course_rule'] = self.enable_course_rule.to_alipay_dict()
            else:
                params['enable_course_rule'] = self.enable_course_rule
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.manual_close:
            if hasattr(self.manual_close, 'to_alipay_dict'):
                params['manual_close'] = self.manual_close.to_alipay_dict()
            else:
                params['manual_close'] = self.manual_close
        if self.period_no_list:
            if isinstance(self.period_no_list, list):
                for i in range(0, len(self.period_no_list)):
                    element = self.period_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.period_no_list[i] = element.to_alipay_dict()
            if hasattr(self.period_no_list, 'to_alipay_dict'):
                params['period_no_list'] = self.period_no_list.to_alipay_dict()
            else:
                params['period_no_list'] = self.period_no_list
        if self.refresh_qr_code_frequency:
            if hasattr(self.refresh_qr_code_frequency, 'to_alipay_dict'):
                params['refresh_qr_code_frequency'] = self.refresh_qr_code_frequency.to_alipay_dict()
            else:
                params['refresh_qr_code_frequency'] = self.refresh_qr_code_frequency
        if self.semester_desc:
            if hasattr(self.semester_desc, 'to_alipay_dict'):
                params['semester_desc'] = self.semester_desc.to_alipay_dict()
            else:
                params['semester_desc'] = self.semester_desc
        if self.semester_id:
            if hasattr(self.semester_id, 'to_alipay_dict'):
                params['semester_id'] = self.semester_id.to_alipay_dict()
            else:
                params['semester_id'] = self.semester_id
        if self.semester_name:
            if hasattr(self.semester_name, 'to_alipay_dict'):
                params['semester_name'] = self.semester_name.to_alipay_dict()
            else:
                params['semester_name'] = self.semester_name
        if self.week_list:
            if isinstance(self.week_list, list):
                for i in range(0, len(self.week_list)):
                    element = self.week_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.week_list[i] = element.to_alipay_dict()
            if hasattr(self.week_list, 'to_alipay_dict'):
                params['week_list'] = self.week_list.to_alipay_dict()
            else:
                params['week_list'] = self.week_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduCourseCheckInRule()
        if 'automatic_refresh' in d:
            o.automatic_refresh = d['automatic_refresh']
        if 'course_desc' in d:
            o.course_desc = d['course_desc']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_rule_id' in d:
            o.course_rule_id = d['course_rule_id']
        if 'course_rule_name' in d:
            o.course_rule_name = d['course_rule_name']
        if 'day_of_week' in d:
            o.day_of_week = d['day_of_week']
        if 'edu_check_in_rule' in d:
            o.edu_check_in_rule = d['edu_check_in_rule']
        if 'enable_course_rule' in d:
            o.enable_course_rule = d['enable_course_rule']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'manual_close' in d:
            o.manual_close = d['manual_close']
        if 'period_no_list' in d:
            o.period_no_list = d['period_no_list']
        if 'refresh_qr_code_frequency' in d:
            o.refresh_qr_code_frequency = d['refresh_qr_code_frequency']
        if 'semester_desc' in d:
            o.semester_desc = d['semester_desc']
        if 'semester_id' in d:
            o.semester_id = d['semester_id']
        if 'semester_name' in d:
            o.semester_name = d['semester_name']
        if 'week_list' in d:
            o.week_list = d['week_list']
        return o


