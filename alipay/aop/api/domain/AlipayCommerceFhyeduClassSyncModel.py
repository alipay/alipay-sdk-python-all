#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduClassTeacher import EduClassTeacher


class AlipayCommerceFhyeduClassSyncModel(object):

    def __init__(self):
        self._address = None
        self._class_name = None
        self._class_room_name = None
        self._course_id = None
        self._course_name = None
        self._inst_id = None
        self._plan_consume_lessions = None
        self._sched_begin_time = None
        self._sched_content = None
        self._sched_end_time = None
        self._sched_id = None
        self._student_id = None
        self._teacher_list = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = value
    @property
    def class_room_name(self):
        return self._class_room_name

    @class_room_name.setter
    def class_room_name(self, value):
        self._class_room_name = value
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
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def plan_consume_lessions(self):
        return self._plan_consume_lessions

    @plan_consume_lessions.setter
    def plan_consume_lessions(self, value):
        self._plan_consume_lessions = value
    @property
    def sched_begin_time(self):
        return self._sched_begin_time

    @sched_begin_time.setter
    def sched_begin_time(self, value):
        self._sched_begin_time = value
    @property
    def sched_content(self):
        return self._sched_content

    @sched_content.setter
    def sched_content(self, value):
        self._sched_content = value
    @property
    def sched_end_time(self):
        return self._sched_end_time

    @sched_end_time.setter
    def sched_end_time(self, value):
        self._sched_end_time = value
    @property
    def sched_id(self):
        return self._sched_id

    @sched_id.setter
    def sched_id(self, value):
        self._sched_id = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value
    @property
    def teacher_list(self):
        return self._teacher_list

    @teacher_list.setter
    def teacher_list(self, value):
        if isinstance(value, list):
            self._teacher_list = list()
            for i in value:
                if isinstance(i, EduClassTeacher):
                    self._teacher_list.append(i)
                else:
                    self._teacher_list.append(EduClassTeacher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.class_name:
            if hasattr(self.class_name, 'to_alipay_dict'):
                params['class_name'] = self.class_name.to_alipay_dict()
            else:
                params['class_name'] = self.class_name
        if self.class_room_name:
            if hasattr(self.class_room_name, 'to_alipay_dict'):
                params['class_room_name'] = self.class_room_name.to_alipay_dict()
            else:
                params['class_room_name'] = self.class_room_name
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
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.plan_consume_lessions:
            if hasattr(self.plan_consume_lessions, 'to_alipay_dict'):
                params['plan_consume_lessions'] = self.plan_consume_lessions.to_alipay_dict()
            else:
                params['plan_consume_lessions'] = self.plan_consume_lessions
        if self.sched_begin_time:
            if hasattr(self.sched_begin_time, 'to_alipay_dict'):
                params['sched_begin_time'] = self.sched_begin_time.to_alipay_dict()
            else:
                params['sched_begin_time'] = self.sched_begin_time
        if self.sched_content:
            if hasattr(self.sched_content, 'to_alipay_dict'):
                params['sched_content'] = self.sched_content.to_alipay_dict()
            else:
                params['sched_content'] = self.sched_content
        if self.sched_end_time:
            if hasattr(self.sched_end_time, 'to_alipay_dict'):
                params['sched_end_time'] = self.sched_end_time.to_alipay_dict()
            else:
                params['sched_end_time'] = self.sched_end_time
        if self.sched_id:
            if hasattr(self.sched_id, 'to_alipay_dict'):
                params['sched_id'] = self.sched_id.to_alipay_dict()
            else:
                params['sched_id'] = self.sched_id
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        if self.teacher_list:
            if isinstance(self.teacher_list, list):
                for i in range(0, len(self.teacher_list)):
                    element = self.teacher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.teacher_list[i] = element.to_alipay_dict()
            if hasattr(self.teacher_list, 'to_alipay_dict'):
                params['teacher_list'] = self.teacher_list.to_alipay_dict()
            else:
                params['teacher_list'] = self.teacher_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFhyeduClassSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'class_name' in d:
            o.class_name = d['class_name']
        if 'class_room_name' in d:
            o.class_room_name = d['class_room_name']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'plan_consume_lessions' in d:
            o.plan_consume_lessions = d['plan_consume_lessions']
        if 'sched_begin_time' in d:
            o.sched_begin_time = d['sched_begin_time']
        if 'sched_content' in d:
            o.sched_content = d['sched_content']
        if 'sched_end_time' in d:
            o.sched_end_time = d['sched_end_time']
        if 'sched_id' in d:
            o.sched_id = d['sched_id']
        if 'student_id' in d:
            o.student_id = d['student_id']
        if 'teacher_list' in d:
            o.teacher_list = d['teacher_list']
        return o


