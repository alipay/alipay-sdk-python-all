#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CourseQueryVO(object):

    def __init__(self):
        self._as_custom_name = None
        self._as_times = None
        self._audit_status = None
        self._category_id_list = None
        self._certificate_code_list = None
        self._certificate_desc_list = None
        self._city_code_list = None
        self._consultation_hook = None
        self._container_type_list = None
        self._course_id = None
        self._course_name = None
        self._course_status = None
        self._course_type = None
        self._cover_image = None
        self._description = None
        self._discount_method = None
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
        self._service_url = None
        self._vc_hours = None
        self._vc_minutes = None
        self._vc_validity_unit = None
        self._vc_validity_value = None

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
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        self._service_url = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.as_custom_name:
            if hasattr(self.as_custom_name, 'to_alipay_dict'):
                params['as_custom_name'] = self.as_custom_name.to_alipay_dict()
            else:
                params['as_custom_name'] = self.as_custom_name
        if self.as_times:
            if hasattr(self.as_times, 'to_alipay_dict'):
                params['as_times'] = self.as_times.to_alipay_dict()
            else:
                params['as_times'] = self.as_times
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.category_id_list:
            if isinstance(self.category_id_list, list):
                for i in range(0, len(self.category_id_list)):
                    element = self.category_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_id_list[i] = element.to_alipay_dict()
            if hasattr(self.category_id_list, 'to_alipay_dict'):
                params['category_id_list'] = self.category_id_list.to_alipay_dict()
            else:
                params['category_id_list'] = self.category_id_list
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
        if self.certificate_desc_list:
            if isinstance(self.certificate_desc_list, list):
                for i in range(0, len(self.certificate_desc_list)):
                    element = self.certificate_desc_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.certificate_desc_list[i] = element.to_alipay_dict()
            if hasattr(self.certificate_desc_list, 'to_alipay_dict'):
                params['certificate_desc_list'] = self.certificate_desc_list.to_alipay_dict()
            else:
                params['certificate_desc_list'] = self.certificate_desc_list
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
        if self.consultation_hook:
            if hasattr(self.consultation_hook, 'to_alipay_dict'):
                params['consultation_hook'] = self.consultation_hook.to_alipay_dict()
            else:
                params['consultation_hook'] = self.consultation_hook
        if self.container_type_list:
            if isinstance(self.container_type_list, list):
                for i in range(0, len(self.container_type_list)):
                    element = self.container_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.container_type_list[i] = element.to_alipay_dict()
            if hasattr(self.container_type_list, 'to_alipay_dict'):
                params['container_type_list'] = self.container_type_list.to_alipay_dict()
            else:
                params['container_type_list'] = self.container_type_list
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
        if self.course_status:
            if hasattr(self.course_status, 'to_alipay_dict'):
                params['course_status'] = self.course_status.to_alipay_dict()
            else:
                params['course_status'] = self.course_status
        if self.course_type:
            if hasattr(self.course_type, 'to_alipay_dict'):
                params['course_type'] = self.course_type.to_alipay_dict()
            else:
                params['course_type'] = self.course_type
        if self.cover_image:
            if hasattr(self.cover_image, 'to_alipay_dict'):
                params['cover_image'] = self.cover_image.to_alipay_dict()
            else:
                params['cover_image'] = self.cover_image
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.discount_method:
            if hasattr(self.discount_method, 'to_alipay_dict'):
                params['discount_method'] = self.discount_method.to_alipay_dict()
            else:
                params['discount_method'] = self.discount_method
        if self.industry_show_status:
            if hasattr(self.industry_show_status, 'to_alipay_dict'):
                params['industry_show_status'] = self.industry_show_status.to_alipay_dict()
            else:
                params['industry_show_status'] = self.industry_show_status
        if self.lm_description:
            if hasattr(self.lm_description, 'to_alipay_dict'):
                params['lm_description'] = self.lm_description.to_alipay_dict()
            else:
                params['lm_description'] = self.lm_description
        if self.lsc_sessions:
            if hasattr(self.lsc_sessions, 'to_alipay_dict'):
                params['lsc_sessions'] = self.lsc_sessions.to_alipay_dict()
            else:
                params['lsc_sessions'] = self.lsc_sessions
        if self.market_price:
            if hasattr(self.market_price, 'to_alipay_dict'):
                params['market_price'] = self.market_price.to_alipay_dict()
            else:
                params['market_price'] = self.market_price
        if self.oc_hours:
            if hasattr(self.oc_hours, 'to_alipay_dict'):
                params['oc_hours'] = self.oc_hours.to_alipay_dict()
            else:
                params['oc_hours'] = self.oc_hours
        if self.oc_students_per_class:
            if hasattr(self.oc_students_per_class, 'to_alipay_dict'):
                params['oc_students_per_class'] = self.oc_students_per_class.to_alipay_dict()
            else:
                params['oc_students_per_class'] = self.oc_students_per_class
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
        if self.pt_hours:
            if hasattr(self.pt_hours, 'to_alipay_dict'):
                params['pt_hours'] = self.pt_hours.to_alipay_dict()
            else:
                params['pt_hours'] = self.pt_hours
        if self.pt_provide_venue_and_equipment:
            if hasattr(self.pt_provide_venue_and_equipment, 'to_alipay_dict'):
                params['pt_provide_venue_and_equipment'] = self.pt_provide_venue_and_equipment.to_alipay_dict()
            else:
                params['pt_provide_venue_and_equipment'] = self.pt_provide_venue_and_equipment
        if self.relation_degree:
            if hasattr(self.relation_degree, 'to_alipay_dict'):
                params['relation_degree'] = self.relation_degree.to_alipay_dict()
            else:
                params['relation_degree'] = self.relation_degree
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        if self.service_url:
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        if self.vc_hours:
            if hasattr(self.vc_hours, 'to_alipay_dict'):
                params['vc_hours'] = self.vc_hours.to_alipay_dict()
            else:
                params['vc_hours'] = self.vc_hours
        if self.vc_minutes:
            if hasattr(self.vc_minutes, 'to_alipay_dict'):
                params['vc_minutes'] = self.vc_minutes.to_alipay_dict()
            else:
                params['vc_minutes'] = self.vc_minutes
        if self.vc_validity_unit:
            if hasattr(self.vc_validity_unit, 'to_alipay_dict'):
                params['vc_validity_unit'] = self.vc_validity_unit.to_alipay_dict()
            else:
                params['vc_validity_unit'] = self.vc_validity_unit
        if self.vc_validity_value:
            if hasattr(self.vc_validity_value, 'to_alipay_dict'):
                params['vc_validity_value'] = self.vc_validity_value.to_alipay_dict()
            else:
                params['vc_validity_value'] = self.vc_validity_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CourseQueryVO()
        if 'as_custom_name' in d:
            o.as_custom_name = d['as_custom_name']
        if 'as_times' in d:
            o.as_times = d['as_times']
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'category_id_list' in d:
            o.category_id_list = d['category_id_list']
        if 'certificate_code_list' in d:
            o.certificate_code_list = d['certificate_code_list']
        if 'certificate_desc_list' in d:
            o.certificate_desc_list = d['certificate_desc_list']
        if 'city_code_list' in d:
            o.city_code_list = d['city_code_list']
        if 'consultation_hook' in d:
            o.consultation_hook = d['consultation_hook']
        if 'container_type_list' in d:
            o.container_type_list = d['container_type_list']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'course_status' in d:
            o.course_status = d['course_status']
        if 'course_type' in d:
            o.course_type = d['course_type']
        if 'cover_image' in d:
            o.cover_image = d['cover_image']
        if 'description' in d:
            o.description = d['description']
        if 'discount_method' in d:
            o.discount_method = d['discount_method']
        if 'industry_show_status' in d:
            o.industry_show_status = d['industry_show_status']
        if 'lm_description' in d:
            o.lm_description = d['lm_description']
        if 'lsc_sessions' in d:
            o.lsc_sessions = d['lsc_sessions']
        if 'market_price' in d:
            o.market_price = d['market_price']
        if 'oc_hours' in d:
            o.oc_hours = d['oc_hours']
        if 'oc_students_per_class' in d:
            o.oc_students_per_class = d['oc_students_per_class']
        if 'org_code' in d:
            o.org_code = d['org_code']
        if 'out_course_id' in d:
            o.out_course_id = d['out_course_id']
        if 'pt_hours' in d:
            o.pt_hours = d['pt_hours']
        if 'pt_provide_venue_and_equipment' in d:
            o.pt_provide_venue_and_equipment = d['pt_provide_venue_and_equipment']
        if 'relation_degree' in d:
            o.relation_degree = d['relation_degree']
        if 'remark' in d:
            o.remark = d['remark']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        if 'service_url' in d:
            o.service_url = d['service_url']
        if 'vc_hours' in d:
            o.vc_hours = d['vc_hours']
        if 'vc_minutes' in d:
            o.vc_minutes = d['vc_minutes']
        if 'vc_validity_unit' in d:
            o.vc_validity_unit = d['vc_validity_unit']
        if 'vc_validity_value' in d:
            o.vc_validity_value = d['vc_validity_value']
        return o


