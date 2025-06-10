#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduNodeInfo import EduNodeInfo
from alipay.aop.api.domain.EduPeriodInfo import EduPeriodInfo


class EduCourseInfo(object):

    def __init__(self):
        self._course_desc = None
        self._course_id = None
        self._course_name = None
        self._day_of_week = None
        self._inst_id = None
        self._node_list = None
        self._period_info = None
        self._period_no_list = None
        self._place_id = None
        self._place_name = None
        self._place_out_biz_no = None
        self._semester_id = None
        self._semester_name = None
        self._teacher_employee_no = None
        self._teacher_roster_id = None
        self._teacher_roster_name = None
        self._week_list = None

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
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        self._day_of_week = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def node_list(self):
        return self._node_list

    @node_list.setter
    def node_list(self, value):
        if isinstance(value, list):
            self._node_list = list()
            for i in value:
                if isinstance(i, EduNodeInfo):
                    self._node_list.append(i)
                else:
                    self._node_list.append(EduNodeInfo.from_alipay_dict(i))
    @property
    def period_info(self):
        return self._period_info

    @period_info.setter
    def period_info(self, value):
        if isinstance(value, EduPeriodInfo):
            self._period_info = value
        else:
            self._period_info = EduPeriodInfo.from_alipay_dict(value)
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
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
    @property
    def place_name(self):
        return self._place_name

    @place_name.setter
    def place_name(self, value):
        self._place_name = value
    @property
    def place_out_biz_no(self):
        return self._place_out_biz_no

    @place_out_biz_no.setter
    def place_out_biz_no(self, value):
        self._place_out_biz_no = value
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
    def teacher_employee_no(self):
        return self._teacher_employee_no

    @teacher_employee_no.setter
    def teacher_employee_no(self, value):
        self._teacher_employee_no = value
    @property
    def teacher_roster_id(self):
        return self._teacher_roster_id

    @teacher_roster_id.setter
    def teacher_roster_id(self, value):
        self._teacher_roster_id = value
    @property
    def teacher_roster_name(self):
        return self._teacher_roster_name

    @teacher_roster_name.setter
    def teacher_roster_name(self, value):
        self._teacher_roster_name = value
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
        if self.day_of_week:
            if hasattr(self.day_of_week, 'to_alipay_dict'):
                params['day_of_week'] = self.day_of_week.to_alipay_dict()
            else:
                params['day_of_week'] = self.day_of_week
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.node_list:
            if isinstance(self.node_list, list):
                for i in range(0, len(self.node_list)):
                    element = self.node_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_list[i] = element.to_alipay_dict()
            if hasattr(self.node_list, 'to_alipay_dict'):
                params['node_list'] = self.node_list.to_alipay_dict()
            else:
                params['node_list'] = self.node_list
        if self.period_info:
            if hasattr(self.period_info, 'to_alipay_dict'):
                params['period_info'] = self.period_info.to_alipay_dict()
            else:
                params['period_info'] = self.period_info
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
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        if self.place_name:
            if hasattr(self.place_name, 'to_alipay_dict'):
                params['place_name'] = self.place_name.to_alipay_dict()
            else:
                params['place_name'] = self.place_name
        if self.place_out_biz_no:
            if hasattr(self.place_out_biz_no, 'to_alipay_dict'):
                params['place_out_biz_no'] = self.place_out_biz_no.to_alipay_dict()
            else:
                params['place_out_biz_no'] = self.place_out_biz_no
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
        if self.teacher_employee_no:
            if hasattr(self.teacher_employee_no, 'to_alipay_dict'):
                params['teacher_employee_no'] = self.teacher_employee_no.to_alipay_dict()
            else:
                params['teacher_employee_no'] = self.teacher_employee_no
        if self.teacher_roster_id:
            if hasattr(self.teacher_roster_id, 'to_alipay_dict'):
                params['teacher_roster_id'] = self.teacher_roster_id.to_alipay_dict()
            else:
                params['teacher_roster_id'] = self.teacher_roster_id
        if self.teacher_roster_name:
            if hasattr(self.teacher_roster_name, 'to_alipay_dict'):
                params['teacher_roster_name'] = self.teacher_roster_name.to_alipay_dict()
            else:
                params['teacher_roster_name'] = self.teacher_roster_name
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
        o = EduCourseInfo()
        if 'course_desc' in d:
            o.course_desc = d['course_desc']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'day_of_week' in d:
            o.day_of_week = d['day_of_week']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'node_list' in d:
            o.node_list = d['node_list']
        if 'period_info' in d:
            o.period_info = d['period_info']
        if 'period_no_list' in d:
            o.period_no_list = d['period_no_list']
        if 'place_id' in d:
            o.place_id = d['place_id']
        if 'place_name' in d:
            o.place_name = d['place_name']
        if 'place_out_biz_no' in d:
            o.place_out_biz_no = d['place_out_biz_no']
        if 'semester_id' in d:
            o.semester_id = d['semester_id']
        if 'semester_name' in d:
            o.semester_name = d['semester_name']
        if 'teacher_employee_no' in d:
            o.teacher_employee_no = d['teacher_employee_no']
        if 'teacher_roster_id' in d:
            o.teacher_roster_id = d['teacher_roster_id']
        if 'teacher_roster_name' in d:
            o.teacher_roster_name = d['teacher_roster_name']
        if 'week_list' in d:
            o.week_list = d['week_list']
        return o


