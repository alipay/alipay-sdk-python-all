#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExamAttrsItemVO import ExamAttrsItemVO


class AlipayEbppIndustryCareertrainingExamQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryCareertrainingExamQueryResponse, self).__init__()
        self._certificate_code_list = None
        self._city_code_list = None
        self._description = None
        self._details = None
        self._exam_attrs = None
        self._exam_id = None
        self._exam_name = None
        self._exam_status = None
        self._exam_time_notes = None
        self._head_image_list = None
        self._max_price = None
        self._min_price = None
        self._org_code = None
        self._out_exam_id = None
        self._registration_end_date = None
        self._registration_notes = None
        self._registration_requirement = None
        self._registration_start_date = None
        self._registration_steps = None
        self._remark = None
        self._service_url = None

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value
    @property
    def exam_attrs(self):
        return self._exam_attrs

    @exam_attrs.setter
    def exam_attrs(self, value):
        if isinstance(value, list):
            self._exam_attrs = list()
            for i in value:
                if isinstance(i, ExamAttrsItemVO):
                    self._exam_attrs.append(i)
                else:
                    self._exam_attrs.append(ExamAttrsItemVO.from_alipay_dict(i))
    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value
    @property
    def exam_name(self):
        return self._exam_name

    @exam_name.setter
    def exam_name(self, value):
        self._exam_name = value
    @property
    def exam_status(self):
        return self._exam_status

    @exam_status.setter
    def exam_status(self, value):
        self._exam_status = value
    @property
    def exam_time_notes(self):
        return self._exam_time_notes

    @exam_time_notes.setter
    def exam_time_notes(self, value):
        self._exam_time_notes = value
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
    def max_price(self):
        return self._max_price

    @max_price.setter
    def max_price(self, value):
        self._max_price = value
    @property
    def min_price(self):
        return self._min_price

    @min_price.setter
    def min_price(self, value):
        self._min_price = value
    @property
    def org_code(self):
        return self._org_code

    @org_code.setter
    def org_code(self, value):
        self._org_code = value
    @property
    def out_exam_id(self):
        return self._out_exam_id

    @out_exam_id.setter
    def out_exam_id(self, value):
        self._out_exam_id = value
    @property
    def registration_end_date(self):
        return self._registration_end_date

    @registration_end_date.setter
    def registration_end_date(self, value):
        self._registration_end_date = value
    @property
    def registration_notes(self):
        return self._registration_notes

    @registration_notes.setter
    def registration_notes(self, value):
        self._registration_notes = value
    @property
    def registration_requirement(self):
        return self._registration_requirement

    @registration_requirement.setter
    def registration_requirement(self, value):
        self._registration_requirement = value
    @property
    def registration_start_date(self):
        return self._registration_start_date

    @registration_start_date.setter
    def registration_start_date(self, value):
        self._registration_start_date = value
    @property
    def registration_steps(self):
        return self._registration_steps

    @registration_steps.setter
    def registration_steps(self, value):
        self._registration_steps = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryCareertrainingExamQueryResponse, self).parse_response_content(response_content)
        if 'certificate_code_list' in response:
            self.certificate_code_list = response['certificate_code_list']
        if 'city_code_list' in response:
            self.city_code_list = response['city_code_list']
        if 'description' in response:
            self.description = response['description']
        if 'details' in response:
            self.details = response['details']
        if 'exam_attrs' in response:
            self.exam_attrs = response['exam_attrs']
        if 'exam_id' in response:
            self.exam_id = response['exam_id']
        if 'exam_name' in response:
            self.exam_name = response['exam_name']
        if 'exam_status' in response:
            self.exam_status = response['exam_status']
        if 'exam_time_notes' in response:
            self.exam_time_notes = response['exam_time_notes']
        if 'head_image_list' in response:
            self.head_image_list = response['head_image_list']
        if 'max_price' in response:
            self.max_price = response['max_price']
        if 'min_price' in response:
            self.min_price = response['min_price']
        if 'org_code' in response:
            self.org_code = response['org_code']
        if 'out_exam_id' in response:
            self.out_exam_id = response['out_exam_id']
        if 'registration_end_date' in response:
            self.registration_end_date = response['registration_end_date']
        if 'registration_notes' in response:
            self.registration_notes = response['registration_notes']
        if 'registration_requirement' in response:
            self.registration_requirement = response['registration_requirement']
        if 'registration_start_date' in response:
            self.registration_start_date = response['registration_start_date']
        if 'registration_steps' in response:
            self.registration_steps = response['registration_steps']
        if 'remark' in response:
            self.remark = response['remark']
        if 'service_url' in response:
            self.service_url = response['service_url']
