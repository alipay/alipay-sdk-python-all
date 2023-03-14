#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.JobWorthCourseChapter import JobWorthCourseChapter
from alipay.aop.api.domain.JobWorthCourseTeacher import JobWorthCourseTeacher


class ZhimaCustomerJobworthCourseCreateModel(object):

    def __init__(self):
        self._course_chapter_list = None
        self._course_desc = None
        self._course_desc_pic = None
        self._course_id = None
        self._course_pic = None
        self._course_title = None
        self._public_id = None
        self._teacher_list = None

    @property
    def course_chapter_list(self):
        return self._course_chapter_list

    @course_chapter_list.setter
    def course_chapter_list(self, value):
        if isinstance(value, list):
            self._course_chapter_list = list()
            for i in value:
                if isinstance(i, JobWorthCourseChapter):
                    self._course_chapter_list.append(i)
                else:
                    self._course_chapter_list.append(JobWorthCourseChapter.from_alipay_dict(i))
    @property
    def course_desc(self):
        return self._course_desc

    @course_desc.setter
    def course_desc(self, value):
        self._course_desc = value
    @property
    def course_desc_pic(self):
        return self._course_desc_pic

    @course_desc_pic.setter
    def course_desc_pic(self, value):
        if isinstance(value, list):
            self._course_desc_pic = list()
            for i in value:
                self._course_desc_pic.append(i)
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_pic(self):
        return self._course_pic

    @course_pic.setter
    def course_pic(self, value):
        self._course_pic = value
    @property
    def course_title(self):
        return self._course_title

    @course_title.setter
    def course_title(self, value):
        self._course_title = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def teacher_list(self):
        return self._teacher_list

    @teacher_list.setter
    def teacher_list(self, value):
        if isinstance(value, list):
            self._teacher_list = list()
            for i in value:
                if isinstance(i, JobWorthCourseTeacher):
                    self._teacher_list.append(i)
                else:
                    self._teacher_list.append(JobWorthCourseTeacher.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.course_chapter_list:
            if isinstance(self.course_chapter_list, list):
                for i in range(0, len(self.course_chapter_list)):
                    element = self.course_chapter_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_chapter_list[i] = element.to_alipay_dict()
            if hasattr(self.course_chapter_list, 'to_alipay_dict'):
                params['course_chapter_list'] = self.course_chapter_list.to_alipay_dict()
            else:
                params['course_chapter_list'] = self.course_chapter_list
        if self.course_desc:
            if hasattr(self.course_desc, 'to_alipay_dict'):
                params['course_desc'] = self.course_desc.to_alipay_dict()
            else:
                params['course_desc'] = self.course_desc
        if self.course_desc_pic:
            if isinstance(self.course_desc_pic, list):
                for i in range(0, len(self.course_desc_pic)):
                    element = self.course_desc_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_desc_pic[i] = element.to_alipay_dict()
            if hasattr(self.course_desc_pic, 'to_alipay_dict'):
                params['course_desc_pic'] = self.course_desc_pic.to_alipay_dict()
            else:
                params['course_desc_pic'] = self.course_desc_pic
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_pic:
            if hasattr(self.course_pic, 'to_alipay_dict'):
                params['course_pic'] = self.course_pic.to_alipay_dict()
            else:
                params['course_pic'] = self.course_pic
        if self.course_title:
            if hasattr(self.course_title, 'to_alipay_dict'):
                params['course_title'] = self.course_title.to_alipay_dict()
            else:
                params['course_title'] = self.course_title
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
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
        o = ZhimaCustomerJobworthCourseCreateModel()
        if 'course_chapter_list' in d:
            o.course_chapter_list = d['course_chapter_list']
        if 'course_desc' in d:
            o.course_desc = d['course_desc']
        if 'course_desc_pic' in d:
            o.course_desc_pic = d['course_desc_pic']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_pic' in d:
            o.course_pic = d['course_pic']
        if 'course_title' in d:
            o.course_title = d['course_title']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'teacher_list' in d:
            o.teacher_list = d['teacher_list']
        return o


