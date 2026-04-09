#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SyllabusStructuredQueryVO import SyllabusStructuredQueryVO
from alipay.aop.api.domain.TeacherVO import TeacherVO


class AlipayEbppIndustryCareertrainingNewcourseQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingNewcourseQueryResponse, self).__init__()
        self._applicable_population_list = None
        self._as_custom_name = None
        self._as_times = None
        self._audit_status = None
        self._category_id_list = None
        self._certificate_code_list = None
        self._certificate_desc_list = None
        self._city_code_list = None
        self._consultation_hook = None
        self._container_type_list = None
        self._course_cover_video = None
        self._course_id = None
        self._course_introduction = None
        self._course_name = None
        self._course_status = None
        self._course_type = None
        self._cover_image = None
        self._description = None
        self._discount_method = None
        self._head_image_list = None
        self._industry_show_status = None
        self._lm_description = None
        self._lsc_sessions = None
        self._market_price = None
        self._oc_hours = None
        self._oc_students_per_class = None
        self._org_code = None
        self._out_course_id = None
        self._pt_hours = None
        self._pt_provide_venue_and_equipment = None
        self._relation_degree = None
        self._remark = None
        self._sale_price = None
        self._separate_syllabus = None
        self._separate_syllabus_structured = None
        self._service_url = None
        self._syllabus_rich_text = None
        self._syllabus_structured = None
        self._teacher_info = None
        self._vc_hours = None
        self._vc_minutes = None
        self._vc_validity_unit = None
        self._vc_validity_value = None

    @property
    def applicable_population_list(self):
        return self._applicable_population_list

    @applicable_population_list.setter
    def applicable_population_list(self, value):
        if isinstance(value, list):
            self._applicable_population_list = list()
            for i in value:
                self._applicable_population_list.append(i)
    @property
    def as_custom_name(self):
        return self._as_custom_name

    @as_custom_name.setter
    def as_custom_name(self, value):
        self._as_custom_name = value
    @property
    def as_times(self):
        return self._as_times

    @as_times.setter
    def as_times(self, value):
        self._as_times = value
    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def category_id_list(self):
        return self._category_id_list

    @category_id_list.setter
    def category_id_list(self, value):
        if isinstance(value, list):
            self._category_id_list = list()
            for i in value:
                self._category_id_list.append(i)
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
    def certificate_desc_list(self):
        return self._certificate_desc_list

    @certificate_desc_list.setter
    def certificate_desc_list(self, value):
        if isinstance(value, list):
            self._certificate_desc_list = list()
            for i in value:
                self._certificate_desc_list.append(i)
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
    def consultation_hook(self):
        return self._consultation_hook

    @consultation_hook.setter
    def consultation_hook(self, value):
        self._consultation_hook = value
    @property
    def container_type_list(self):
        return self._container_type_list

    @container_type_list.setter
    def container_type_list(self, value):
        if isinstance(value, list):
            self._container_type_list = list()
            for i in value:
                self._container_type_list.append(i)
    @property
    def course_cover_video(self):
        return self._course_cover_video

    @course_cover_video.setter
    def course_cover_video(self, value):
        self._course_cover_video = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_introduction(self):
        return self._course_introduction

    @course_introduction.setter
    def course_introduction(self, value):
        self._course_introduction = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def course_status(self):
        return self._course_status

    @course_status.setter
    def course_status(self, value):
        self._course_status = value
    @property
    def course_type(self):
        return self._course_type

    @course_type.setter
    def course_type(self, value):
        self._course_type = value
    @property
    def cover_image(self):
        return self._cover_image

    @cover_image.setter
    def cover_image(self, value):
        self._cover_image = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def discount_method(self):
        return self._discount_method

    @discount_method.setter
    def discount_method(self, value):
        self._discount_method = value
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
    def industry_show_status(self):
        return self._industry_show_status

    @industry_show_status.setter
    def industry_show_status(self, value):
        self._industry_show_status = value
    @property
    def lm_description(self):
        return self._lm_description

    @lm_description.setter
    def lm_description(self, value):
        self._lm_description = value
    @property
    def lsc_sessions(self):
        return self._lsc_sessions

    @lsc_sessions.setter
    def lsc_sessions(self, value):
        self._lsc_sessions = value
    @property
    def market_price(self):
        return self._market_price

    @market_price.setter
    def market_price(self, value):
        self._market_price = value
    @property
    def oc_hours(self):
        return self._oc_hours

    @oc_hours.setter
    def oc_hours(self, value):
        self._oc_hours = value
    @property
    def oc_students_per_class(self):
        return self._oc_students_per_class

    @oc_students_per_class.setter
    def oc_students_per_class(self, value):
        self._oc_students_per_class = value
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
    def pt_hours(self):
        return self._pt_hours

    @pt_hours.setter
    def pt_hours(self, value):
        self._pt_hours = value
    @property
    def pt_provide_venue_and_equipment(self):
        return self._pt_provide_venue_and_equipment

    @pt_provide_venue_and_equipment.setter
    def pt_provide_venue_and_equipment(self, value):
        self._pt_provide_venue_and_equipment = value
    @property
    def relation_degree(self):
        return self._relation_degree

    @relation_degree.setter
    def relation_degree(self, value):
        self._relation_degree = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value
    @property
    def separate_syllabus(self):
        return self._separate_syllabus

    @separate_syllabus.setter
    def separate_syllabus(self, value):
        self._separate_syllabus = value
    @property
    def separate_syllabus_structured(self):
        return self._separate_syllabus_structured

    @separate_syllabus_structured.setter
    def separate_syllabus_structured(self, value):
        self._separate_syllabus_structured = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
    @property
    def syllabus_rich_text(self):
        return self._syllabus_rich_text

    @syllabus_rich_text.setter
    def syllabus_rich_text(self, value):
        self._syllabus_rich_text = value
    @property
    def syllabus_structured(self):
        return self._syllabus_structured

    @syllabus_structured.setter
    def syllabus_structured(self, value):
        if isinstance(value, list):
            self._syllabus_structured = list()
            for i in value:
                if isinstance(i, SyllabusStructuredQueryVO):
                    self._syllabus_structured.append(i)
                else:
                    self._syllabus_structured.append(SyllabusStructuredQueryVO.from_alipay_dict(i))
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
    @property
    def vc_hours(self):
        return self._vc_hours

    @vc_hours.setter
    def vc_hours(self, value):
        self._vc_hours = value
    @property
    def vc_minutes(self):
        return self._vc_minutes

    @vc_minutes.setter
    def vc_minutes(self, value):
        self._vc_minutes = value
    @property
    def vc_validity_unit(self):
        return self._vc_validity_unit

    @vc_validity_unit.setter
    def vc_validity_unit(self, value):
        self._vc_validity_unit = value
    @property
    def vc_validity_value(self):
        return self._vc_validity_value

    @vc_validity_value.setter
    def vc_validity_value(self, value):
        self._vc_validity_value = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingNewcourseQueryResponse, self).parse_response_content(response_content)
        if 'applicable_population_list' in response:
            self.applicable_population_list = response['applicable_population_list']
        if 'as_custom_name' in response:
            self.as_custom_name = response['as_custom_name']
        if 'as_times' in response:
            self.as_times = response['as_times']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'category_id_list' in response:
            self.category_id_list = response['category_id_list']
        if 'certificate_code_list' in response:
            self.certificate_code_list = response['certificate_code_list']
        if 'certificate_desc_list' in response:
            self.certificate_desc_list = response['certificate_desc_list']
        if 'city_code_list' in response:
            self.city_code_list = response['city_code_list']
        if 'consultation_hook' in response:
            self.consultation_hook = response['consultation_hook']
        if 'container_type_list' in response:
            self.container_type_list = response['container_type_list']
        if 'course_cover_video' in response:
            self.course_cover_video = response['course_cover_video']
        if 'course_id' in response:
            self.course_id = response['course_id']
        if 'course_introduction' in response:
            self.course_introduction = response['course_introduction']
        if 'course_name' in response:
            self.course_name = response['course_name']
        if 'course_status' in response:
            self.course_status = response['course_status']
        if 'course_type' in response:
            self.course_type = response['course_type']
        if 'cover_image' in response:
            self.cover_image = response['cover_image']
        if 'description' in response:
            self.description = response['description']
        if 'discount_method' in response:
            self.discount_method = response['discount_method']
        if 'head_image_list' in response:
            self.head_image_list = response['head_image_list']
        if 'industry_show_status' in response:
            self.industry_show_status = response['industry_show_status']
        if 'lm_description' in response:
            self.lm_description = response['lm_description']
        if 'lsc_sessions' in response:
            self.lsc_sessions = response['lsc_sessions']
        if 'market_price' in response:
            self.market_price = response['market_price']
        if 'oc_hours' in response:
            self.oc_hours = response['oc_hours']
        if 'oc_students_per_class' in response:
            self.oc_students_per_class = response['oc_students_per_class']
        if 'org_code' in response:
            self.org_code = response['org_code']
        if 'out_course_id' in response:
            self.out_course_id = response['out_course_id']
        if 'pt_hours' in response:
            self.pt_hours = response['pt_hours']
        if 'pt_provide_venue_and_equipment' in response:
            self.pt_provide_venue_and_equipment = response['pt_provide_venue_and_equipment']
        if 'relation_degree' in response:
            self.relation_degree = response['relation_degree']
        if 'remark' in response:
            self.remark = response['remark']
        if 'sale_price' in response:
            self.sale_price = response['sale_price']
        if 'separate_syllabus' in response:
            self.separate_syllabus = response['separate_syllabus']
        if 'separate_syllabus_structured' in response:
            self.separate_syllabus_structured = response['separate_syllabus_structured']
        if 'service_url' in response:
            self.service_url = response['service_url']
        if 'syllabus_rich_text' in response:
            self.syllabus_rich_text = response['syllabus_rich_text']
        if 'syllabus_structured' in response:
            self.syllabus_structured = response['syllabus_structured']
        if 'teacher_info' in response:
            self.teacher_info = response['teacher_info']
        if 'vc_hours' in response:
            self.vc_hours = response['vc_hours']
        if 'vc_minutes' in response:
            self.vc_minutes = response['vc_minutes']
        if 'vc_validity_unit' in response:
            self.vc_validity_unit = response['vc_validity_unit']
        if 'vc_validity_value' in response:
            self.vc_validity_value = response['vc_validity_value']
