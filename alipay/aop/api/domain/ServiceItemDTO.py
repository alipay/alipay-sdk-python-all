#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceItemDTO(object):

    def __init__(self):
        self._accept_conditions = None
        self._city_code = None
        self._consult_tel = None
        self._implementation_subject = None
        self._material_list = None
        self._name = None
        self._out_item_id = None
        self._process = None
        self._process_location = None
        self._process_time = None
        self._run_status = None
        self._service_object = None
        self._subject_juridical = None
        self._subject_nature = None
        self._url = None

    @property
    def accept_conditions(self):
        return self._accept_conditions

    @accept_conditions.setter
    def accept_conditions(self, value):
        self._accept_conditions = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def consult_tel(self):
        return self._consult_tel

    @consult_tel.setter
    def consult_tel(self, value):
        self._consult_tel = value
    @property
    def implementation_subject(self):
        return self._implementation_subject

    @implementation_subject.setter
    def implementation_subject(self, value):
        self._implementation_subject = value
    @property
    def material_list(self):
        return self._material_list

    @material_list.setter
    def material_list(self, value):
        self._material_list = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_item_id(self):
        return self._out_item_id

    @out_item_id.setter
    def out_item_id(self, value):
        self._out_item_id = value
    @property
    def process(self):
        return self._process

    @process.setter
    def process(self, value):
        self._process = value
    @property
    def process_location(self):
        return self._process_location

    @process_location.setter
    def process_location(self, value):
        self._process_location = value
    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value
    @property
    def run_status(self):
        return self._run_status

    @run_status.setter
    def run_status(self, value):
        self._run_status = value
    @property
    def service_object(self):
        return self._service_object

    @service_object.setter
    def service_object(self, value):
        self._service_object = value
    @property
    def subject_juridical(self):
        return self._subject_juridical

    @subject_juridical.setter
    def subject_juridical(self, value):
        self._subject_juridical = value
    @property
    def subject_nature(self):
        return self._subject_nature

    @subject_nature.setter
    def subject_nature(self, value):
        self._subject_nature = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_conditions:
            if hasattr(self.accept_conditions, 'to_alipay_dict'):
                params['accept_conditions'] = self.accept_conditions.to_alipay_dict()
            else:
                params['accept_conditions'] = self.accept_conditions
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.consult_tel:
            if hasattr(self.consult_tel, 'to_alipay_dict'):
                params['consult_tel'] = self.consult_tel.to_alipay_dict()
            else:
                params['consult_tel'] = self.consult_tel
        if self.implementation_subject:
            if hasattr(self.implementation_subject, 'to_alipay_dict'):
                params['implementation_subject'] = self.implementation_subject.to_alipay_dict()
            else:
                params['implementation_subject'] = self.implementation_subject
        if self.material_list:
            if hasattr(self.material_list, 'to_alipay_dict'):
                params['material_list'] = self.material_list.to_alipay_dict()
            else:
                params['material_list'] = self.material_list
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_item_id:
            if hasattr(self.out_item_id, 'to_alipay_dict'):
                params['out_item_id'] = self.out_item_id.to_alipay_dict()
            else:
                params['out_item_id'] = self.out_item_id
        if self.process:
            if hasattr(self.process, 'to_alipay_dict'):
                params['process'] = self.process.to_alipay_dict()
            else:
                params['process'] = self.process
        if self.process_location:
            if hasattr(self.process_location, 'to_alipay_dict'):
                params['process_location'] = self.process_location.to_alipay_dict()
            else:
                params['process_location'] = self.process_location
        if self.process_time:
            if hasattr(self.process_time, 'to_alipay_dict'):
                params['process_time'] = self.process_time.to_alipay_dict()
            else:
                params['process_time'] = self.process_time
        if self.run_status:
            if hasattr(self.run_status, 'to_alipay_dict'):
                params['run_status'] = self.run_status.to_alipay_dict()
            else:
                params['run_status'] = self.run_status
        if self.service_object:
            if hasattr(self.service_object, 'to_alipay_dict'):
                params['service_object'] = self.service_object.to_alipay_dict()
            else:
                params['service_object'] = self.service_object
        if self.subject_juridical:
            if hasattr(self.subject_juridical, 'to_alipay_dict'):
                params['subject_juridical'] = self.subject_juridical.to_alipay_dict()
            else:
                params['subject_juridical'] = self.subject_juridical
        if self.subject_nature:
            if hasattr(self.subject_nature, 'to_alipay_dict'):
                params['subject_nature'] = self.subject_nature.to_alipay_dict()
            else:
                params['subject_nature'] = self.subject_nature
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceItemDTO()
        if 'accept_conditions' in d:
            o.accept_conditions = d['accept_conditions']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'consult_tel' in d:
            o.consult_tel = d['consult_tel']
        if 'implementation_subject' in d:
            o.implementation_subject = d['implementation_subject']
        if 'material_list' in d:
            o.material_list = d['material_list']
        if 'name' in d:
            o.name = d['name']
        if 'out_item_id' in d:
            o.out_item_id = d['out_item_id']
        if 'process' in d:
            o.process = d['process']
        if 'process_location' in d:
            o.process_location = d['process_location']
        if 'process_time' in d:
            o.process_time = d['process_time']
        if 'run_status' in d:
            o.run_status = d['run_status']
        if 'service_object' in d:
            o.service_object = d['service_object']
        if 'subject_juridical' in d:
            o.subject_juridical = d['subject_juridical']
        if 'subject_nature' in d:
            o.subject_nature = d['subject_nature']
        if 'url' in d:
            o.url = d['url']
        return o


