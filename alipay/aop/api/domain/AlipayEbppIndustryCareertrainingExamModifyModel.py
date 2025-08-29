#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExamAttrsItemVO import ExamAttrsItemVO


class AlipayEbppIndustryCareertrainingExamModifyModel(object):

    def __init__(self):
        self._certificate_code_list = None
        self._city_code_list = None
        self._description = None
        self._details = None
        self._exam_attrs = None
        self._exam_id = None
        self._exam_name = None
        self._exam_time_notes = None
        self._head_image_list = None
        self._max_price = None
        self._min_price = None
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


    def to_alipay_dict(self):
        params = dict()
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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.details:
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.exam_attrs:
            if isinstance(self.exam_attrs, list):
                for i in range(0, len(self.exam_attrs)):
                    element = self.exam_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.exam_attrs[i] = element.to_alipay_dict()
            if hasattr(self.exam_attrs, 'to_alipay_dict'):
                params['exam_attrs'] = self.exam_attrs.to_alipay_dict()
            else:
                params['exam_attrs'] = self.exam_attrs
        if self.exam_id:
            if hasattr(self.exam_id, 'to_alipay_dict'):
                params['exam_id'] = self.exam_id.to_alipay_dict()
            else:
                params['exam_id'] = self.exam_id
        if self.exam_name:
            if hasattr(self.exam_name, 'to_alipay_dict'):
                params['exam_name'] = self.exam_name.to_alipay_dict()
            else:
                params['exam_name'] = self.exam_name
        if self.exam_time_notes:
            if hasattr(self.exam_time_notes, 'to_alipay_dict'):
                params['exam_time_notes'] = self.exam_time_notes.to_alipay_dict()
            else:
                params['exam_time_notes'] = self.exam_time_notes
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
        if self.max_price:
            if hasattr(self.max_price, 'to_alipay_dict'):
                params['max_price'] = self.max_price.to_alipay_dict()
            else:
                params['max_price'] = self.max_price
        if self.min_price:
            if hasattr(self.min_price, 'to_alipay_dict'):
                params['min_price'] = self.min_price.to_alipay_dict()
            else:
                params['min_price'] = self.min_price
        if self.registration_end_date:
            if hasattr(self.registration_end_date, 'to_alipay_dict'):
                params['registration_end_date'] = self.registration_end_date.to_alipay_dict()
            else:
                params['registration_end_date'] = self.registration_end_date
        if self.registration_notes:
            if hasattr(self.registration_notes, 'to_alipay_dict'):
                params['registration_notes'] = self.registration_notes.to_alipay_dict()
            else:
                params['registration_notes'] = self.registration_notes
        if self.registration_requirement:
            if hasattr(self.registration_requirement, 'to_alipay_dict'):
                params['registration_requirement'] = self.registration_requirement.to_alipay_dict()
            else:
                params['registration_requirement'] = self.registration_requirement
        if self.registration_start_date:
            if hasattr(self.registration_start_date, 'to_alipay_dict'):
                params['registration_start_date'] = self.registration_start_date.to_alipay_dict()
            else:
                params['registration_start_date'] = self.registration_start_date
        if self.registration_steps:
            if hasattr(self.registration_steps, 'to_alipay_dict'):
                params['registration_steps'] = self.registration_steps.to_alipay_dict()
            else:
                params['registration_steps'] = self.registration_steps
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamModifyModel()
        if 'certificate_code_list' in d:
            o.certificate_code_list = d['certificate_code_list']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'description' in d:
            o.description = d['description']
        if 'details' in d:
            o.details = d['details']
        if 'exam_attrs' in d:
            o.exam_attrs = d['exam_attrs']
        if 'exam_id' in d:
            o.exam_id = d['exam_id']
        if 'exam_name' in d:
            o.exam_name = d['exam_name']
        if 'exam_time_notes' in d:
            o.exam_time_notes = d['exam_time_notes']
        if 'head_image_list' in d:
            o.head_image_list = d['head_image_list']
        if 'max_price' in d:
            o.max_price = d['max_price']
        if 'min_price' in d:
            o.min_price = d['min_price']
        if 'registration_end_date' in d:
            o.registration_end_date = d['registration_end_date']
        if 'registration_notes' in d:
            o.registration_notes = d['registration_notes']
        if 'registration_requirement' in d:
            o.registration_requirement = d['registration_requirement']
        if 'registration_start_date' in d:
            o.registration_start_date = d['registration_start_date']
        if 'registration_steps' in d:
            o.registration_steps = d['registration_steps']
        if 'remark' in d:
            o.remark = d['remark']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


