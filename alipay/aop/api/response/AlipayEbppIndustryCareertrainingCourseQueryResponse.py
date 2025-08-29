#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CourseTagVO import CourseTagVO
from alipay.aop.api.domain.CourseItemRiskVO import CourseItemRiskVO
from alipay.aop.api.domain.TeacherVO import TeacherVO


class AlipayEbppIndustryCareertrainingCourseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingCourseQueryResponse, self).__init__()
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
        self._risk_info = None
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
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        if isinstance(value, CourseItemRiskVO):
            self._risk_info = value
        else:
            self._risk_info = CourseItemRiskVO.from_alipay_dict(value)
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

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingCourseQueryResponse, self).parse_response_content(response_content)
        if 'category_id' in response:
            self.category_id = response['category_id']
        if 'certificate_code_list' in response:
            self.certificate_code_list = response['certificate_code_list']
        if 'city_code_list' in response:
            self.city_code_list = response['city_code_list']
        if 'course_cover_video' in response:
            self.course_cover_video = response['course_cover_video']
        if 'course_end_date' in response:
            self.course_end_date = response['course_end_date']
        if 'course_id' in response:
            self.course_id = response['course_id']
        if 'course_max_price' in response:
            self.course_max_price = response['course_max_price']
        if 'course_min_price' in response:
            self.course_min_price = response['course_min_price']
        if 'course_name' in response:
            self.course_name = response['course_name']
        if 'course_notes' in response:
            self.course_notes = response['course_notes']
        if 'course_selling_points' in response:
            self.course_selling_points = response['course_selling_points']
        if 'course_start_date' in response:
            self.course_start_date = response['course_start_date']
        if 'course_status' in response:
            self.course_status = response['course_status']
        if 'course_tags' in response:
            self.course_tags = response['course_tags']
        if 'description' in response:
            self.description = response['description']
        if 'details_image_list' in response:
            self.details_image_list = response['details_image_list']
        if 'head_image_list' in response:
            self.head_image_list = response['head_image_list']
        if 'org_code' in response:
            self.org_code = response['org_code']
        if 'out_course_id' in response:
            self.out_course_id = response['out_course_id']
        if 'remark' in response:
            self.remark = response['remark']
        if 'risk_info' in response:
            self.risk_info = response['risk_info']
        if 'service_url' in response:
            self.service_url = response['service_url']
        if 'student_requirement' in response:
            self.student_requirement = response['student_requirement']
        if 'teacher_info' in response:
            self.teacher_info = response['teacher_info']
