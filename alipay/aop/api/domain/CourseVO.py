#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CourseTagVO import CourseTagVO
from alipay.aop.api.domain.TeacherVO import TeacherVO


class CourseVO(object):

    def __init__(self):
        self._category_id = None
        self._certificate_code_list = None
        self._city_code_list = None
        self._course_cover_video = None
        self._course_end_date = None
        self._course_id = None
        self._course_max_price = None
        self._course_min_price = None
        self._course_name = None
        self._course_notes = None
        self._course_selling_points = None
        self._course_start_date = None
        self._course_status = None
        self._course_tags = None
        self._description = None
        self._details_image_list = None
        self._head_image_list = None
        self._org_code = None
        self._out_course_id = None
        self._remark = None
        self._service_url = None
        self._student_requirement = None
        self._teacher_info = None

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self._category_id = value
    @property
    def certificate_code_list(self):
        return self._certificate_code_list

    @certificate_code_list.setter
    def certificate_code_list(self, value):
        if isinstance(value, list):
            self._certificate_code_list = list()
            for i in value:
                self._certificate_code_list.append(i)
    @property
    def city_code_list(self):
        return self._city_code_list

    @city_code_list.setter
    def city_code_list(self, value):
        if isinstance(value, list):
            self._city_code_list = list()
            for i in value:
                self._city_code_list.append(i)
    @property
    def course_cover_video(self):
        return self._course_cover_video

    @course_cover_video.setter
    def course_cover_video(self, value):
        self._course_cover_video = value
    @property
    def course_end_date(self):
        return self._course_end_date

    @course_end_date.setter
    def course_end_date(self, value):
        self._course_end_date = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_max_price(self):
        return self._course_max_price

    @course_max_price.setter
    def course_max_price(self, value):
        self._course_max_price = value
    @property
    def course_min_price(self):
        return self._course_min_price

    @course_min_price.setter
    def course_min_price(self, value):
        self._course_min_price = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_notes(self):
        return self._course_notes

    @course_notes.setter
    def course_notes(self, value):
        self._course_notes = value
    @property
    def course_selling_points(self):
        return self._course_selling_points

    @course_selling_points.setter
    def course_selling_points(self, value):
        if isinstance(value, list):
            self._course_selling_points = list()
            for i in value:
                self._course_selling_points.append(i)
    @property
    def course_start_date(self):
        return self._course_start_date

    @course_start_date.setter
    def course_start_date(self, value):
        self._course_start_date = value
    @property
    def course_status(self):
        return self._course_status

    @course_status.setter
    def course_status(self, value):
        self._course_status = value
    @property
    def course_tags(self):
        return self._course_tags

    @course_tags.setter
    def course_tags(self, value):
        if isinstance(value, list):
            self._course_tags = list()
            for i in value:
                if isinstance(i, CourseTagVO):
                    self._course_tags.append(i)
                else:
                    self._course_tags.append(CourseTagVO.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def details_image_list(self):
        return self._details_image_list

    @details_image_list.setter
    def details_image_list(self, value):
        if isinstance(value, list):
            self._details_image_list = list()
            for i in value:
                self._details_image_list.append(i)
    @property
    def head_image_list(self):
        return self._head_image_list

    @head_image_list.setter
    def head_image_list(self, value):
        if isinstance(value, list):
            self._head_image_list = list()
            for i in value:
                self._head_image_list.append(i)
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_course_id(self):
        return self._out_course_id

    @out_course_id.setter
    def out_course_id(self, value):
        self._out_course_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def student_requirement(self):
        return self._student_requirement

    @student_requirement.setter
    def student_requirement(self, value):
        self._student_requirement = value
    @property
    def teacher_info(self):
        return self._teacher_info

    @teacher_info.setter
    def teacher_info(self, value):
        if isinstance(value, list):
            self._teacher_info = list()
            for i in value:
                if isinstance(i, TeacherVO):
                    self._teacher_info.append(i)
                else:
                    self._teacher_info.append(TeacherVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.category_id:
            if hasattr(self.category_id, 'to_alipay_dict'):
                params['category_id'] = self.category_id.to_alipay_dict()
            else:
                params['category_id'] = self.category_id
        if self.certificate_code_list:
            if isinstance(self.certificate_code_list, list):
                for i in range(0, len(self.certificate_code_list)):
                    element = self.certificate_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_code_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_code_list, 'to_alipay_dict'):
                params['certificate_code_list'] = self.certificate_code_list.to_alipay_dict()
            else:
                params['certificate_code_list'] = self.certificate_code_list
        if self.city_code_list:
            if isinstance(self.city_code_list, list):
                for i in range(0, len(self.city_code_list)):
                    element = self.city_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.city_code_list[i] = element.to_alipay_dict()
            if hasattr(self.city_code_list, 'to_alipay_dict'):
                params['city_code_list'] = self.city_code_list.to_alipay_dict()
            else:
                params['city_code_list'] = self.city_code_list
        if self.course_cover_video:
            if hasattr(self.course_cover_video, 'to_alipay_dict'):
                params['course_cover_video'] = self.course_cover_video.to_alipay_dict()
            else:
                params['course_cover_video'] = self.course_cover_video
        if self.course_end_date:
            if hasattr(self.course_end_date, 'to_alipay_dict'):
                params['course_end_date'] = self.course_end_date.to_alipay_dict()
            else:
                params['course_end_date'] = self.course_end_date
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_max_price:
            if hasattr(self.course_max_price, 'to_alipay_dict'):
                params['course_max_price'] = self.course_max_price.to_alipay_dict()
            else:
                params['course_max_price'] = self.course_max_price
        if self.course_min_price:
            if hasattr(self.course_min_price, 'to_alipay_dict'):
                params['course_min_price'] = self.course_min_price.to_alipay_dict()
            else:
                params['course_min_price'] = self.course_min_price
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.course_notes:
            if hasattr(self.course_notes, 'to_alipay_dict'):
                params['course_notes'] = self.course_notes.to_alipay_dict()
            else:
                params['course_notes'] = self.course_notes
        if self.course_selling_points:
            if isinstance(self.course_selling_points, list):
                for i in range(0, len(self.course_selling_points)):
                    element = self.course_selling_points[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_selling_points[i] = element.to_alipay_dict()
            if hasattr(self.course_selling_points, 'to_alipay_dict'):
                params['course_selling_points'] = self.course_selling_points.to_alipay_dict()
            else:
                params['course_selling_points'] = self.course_selling_points
        if self.course_start_date:
            if hasattr(self.course_start_date, 'to_alipay_dict'):
                params['course_start_date'] = self.course_start_date.to_alipay_dict()
            else:
                params['course_start_date'] = self.course_start_date
        if self.course_status:
            if hasattr(self.course_status, 'to_alipay_dict'):
                params['course_status'] = self.course_status.to_alipay_dict()
            else:
                params['course_status'] = self.course_status
        if self.course_tags:
            if isinstance(self.course_tags, list):
                for i in range(0, len(self.course_tags)):
                    element = self.course_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.course_tags[i] = element.to_alipay_dict()
            if hasattr(self.course_tags, 'to_alipay_dict'):
                params['course_tags'] = self.course_tags.to_alipay_dict()
            else:
                params['course_tags'] = self.course_tags
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.details_image_list:
            if isinstance(self.details_image_list, list):
                for i in range(0, len(self.details_image_list)):
                    element = self.details_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details_image_list[i] = element.to_alipay_dict()
            if hasattr(self.details_image_list, 'to_alipay_dict'):
                params['details_image_list'] = self.details_image_list.to_alipay_dict()
            else:
                params['details_image_list'] = self.details_image_list
        if self.head_image_list:
            if isinstance(self.head_image_list, list):
                for i in range(0, len(self.head_image_list)):
                    element = self.head_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.head_image_list[i] = element.to_alipay_dict()
            if hasattr(self.head_image_list, 'to_alipay_dict'):
                params['head_image_list'] = self.head_image_list.to_alipay_dict()
            else:
                params['head_image_list'] = self.head_image_list
        if self.org_code:
            if hasattr(self.org_code, 'to_alipay_dict'):
                params['org_code'] = self.org_code.to_alipay_dict()
            else:
                params['org_code'] = self.org_code
        if self.out_course_id:
            if hasattr(self.out_course_id, 'to_alipay_dict'):
                params['out_course_id'] = self.out_course_id.to_alipay_dict()
            else:
                params['out_course_id'] = self.out_course_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.student_requirement:
            if hasattr(self.student_requirement, 'to_alipay_dict'):
                params['student_requirement'] = self.student_requirement.to_alipay_dict()
            else:
                params['student_requirement'] = self.student_requirement
        if self.teacher_info:
            if isinstance(self.teacher_info, list):
                for i in range(0, len(self.teacher_info)):
                    element = self.teacher_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.teacher_info[i] = element.to_alipay_dict()
            if hasattr(self.teacher_info, 'to_alipay_dict'):
                params['teacher_info'] = self.teacher_info.to_alipay_dict()
            else:
                params['teacher_info'] = self.teacher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CourseVO()
        if 'category_id' in d:
            o.category_id = d['category_id']
        if 'certificate_code_list' in d:
            o.certificate_code_list = d['certificate_code_list']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'course_cover_video' in d:
            o.course_cover_video = d['course_cover_video']
        if 'course_end_date' in d:
            o.course_end_date = d['course_end_date']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_max_price' in d:
            o.course_max_price = d['course_max_price']
        if 'course_min_price' in d:
            o.course_min_price = d['course_min_price']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_notes' in d:
            o.course_notes = d['course_notes']
        if 'course_selling_points' in d:
            o.course_selling_points = d['course_selling_points']
        if 'course_start_date' in d:
            o.course_start_date = d['course_start_date']
        if 'course_status' in d:
            o.course_status = d['course_status']
        if 'course_tags' in d:
            o.course_tags = d['course_tags']
        if 'description' in d:
            o.description = d['description']
        if 'details_image_list' in d:
            o.details_image_list = d['details_image_list']
        if 'head_image_list' in d:
            o.head_image_list = d['head_image_list']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_course_id' in d:
            o.out_course_id = d['out_course_id']
        if 'remark' in d:
            o.remark = d['remark']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'student_requirement' in d:
            o.student_requirement = d['student_requirement']
        if 'teacher_info' in d:
            o.teacher_info = d['teacher_info']
        return o


