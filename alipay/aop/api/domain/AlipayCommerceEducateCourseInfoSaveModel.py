#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCourseInfoSaveModel(object):

    def __init__(self):
        self._course_desc = None
        self._course_id = None
        self._course_name = None
        self._day_of_week = None
        self._inst_id = None
        self._node_id_list = None
        self._period_no_list = None
        self._place_out_biz_no = None
        self._semester_id = None
        self._status = None
        self._teacher_employee_no = None
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
    def node_id_list(self):
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, value):
        if isinstance(value, list):
            self._node_id_list = list()
            for i in value:
                self._node_id_list.append(i)
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
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def teacher_employee_no(self):
        return self._teacher_employee_no

    @teacher_employee_no.setter
    def teacher_employee_no(self, value):
        self._teacher_employee_no = value
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
        if self.node_id_list:
            if isinstance(self.node_id_list, list):
                for i in range(0, len(self.node_id_list)):
                    element = self.node_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_id_list[i] = element.to_alipay_dict()
            if hasattr(self.node_id_list, 'to_alipay_dict'):
                params['node_id_list'] = self.node_id_list.to_alipay_dict()
            else:
                params['node_id_list'] = self.node_id_list
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.teacher_employee_no:
            if hasattr(self.teacher_employee_no, 'to_alipay_dict'):
                params['teacher_employee_no'] = self.teacher_employee_no.to_alipay_dict()
            else:
                params['teacher_employee_no'] = self.teacher_employee_no
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
        o = AlipayCommerceEducateCourseInfoSaveModel()
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
        if 'node_id_list' in d:
            o.node_id_list = d['node_id_list']
        if 'period_no_list' in d:
            o.period_no_list = d['period_no_list']
        if 'place_out_biz_no' in d:
            o.place_out_biz_no = d['place_out_biz_no']
        if 'semester_id' in d:
            o.semester_id = d['semester_id']
        if 'status' in d:
            o.status = d['status']
        if 'teacher_employee_no' in d:
            o.teacher_employee_no = d['teacher_employee_no']
        if 'week_list' in d:
            o.week_list = d['week_list']
        return o


