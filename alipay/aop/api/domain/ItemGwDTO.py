#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemContactVo import ItemContactVo


class ItemGwDTO(object):

    def __init__(self):
        self._accept_conditions = None
        self._category = None
        self._checklist = None
        self._code = None
        self._contact = None
        self._district = None
        self._implementation_subject = None
        self._link = None
        self._name = None
        self._online_support = None
        self._palm_support = None
        self._palm_url = None
        self._rel_service = None
        self._scene = None
        self._service_object = None
        self._subject_juridical = None
        self._subject_nature = None
        self._working_schedule = None

    @property
    def accept_conditions(self):
        return self._accept_conditions

    @accept_conditions.setter
    def accept_conditions(self, value):
        self._accept_conditions = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, list):
            self._category = list()
            for i in value:
                self._category.append(i)
    @property
    def checklist(self):
        return self._checklist

    @checklist.setter
    def checklist(self, value):
        if isinstance(value, list):
            self._checklist = list()
            for i in value:
                self._checklist.append(i)
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):
        if isinstance(value, list):
            self._contact = list()
            for i in value:
                if isinstance(i, ItemContactVo):
                    self._contact.append(i)
                else:
                    self._contact.append(ItemContactVo.from_alipay_dict(i))
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def implementation_subject(self):
        return self._implementation_subject

    @implementation_subject.setter
    def implementation_subject(self, value):
        self._implementation_subject = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def online_support(self):
        return self._online_support

    @online_support.setter
    def online_support(self, value):
        self._online_support = value
    @property
    def palm_support(self):
        return self._palm_support

    @palm_support.setter
    def palm_support(self, value):
        self._palm_support = value
    @property
    def palm_url(self):
        return self._palm_url

    @palm_url.setter
    def palm_url(self, value):
        self._palm_url = value
    @property
    def rel_service(self):
        return self._rel_service

    @rel_service.setter
    def rel_service(self, value):
        self._rel_service = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
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
        if isinstance(value, list):
            self._subject_juridical = list()
            for i in value:
                self._subject_juridical.append(i)
    @property
    def subject_nature(self):
        return self._subject_nature

    @subject_nature.setter
    def subject_nature(self, value):
        if isinstance(value, list):
            self._subject_nature = list()
            for i in value:
                self._subject_nature.append(i)
    @property
    def working_schedule(self):
        return self._working_schedule

    @working_schedule.setter
    def working_schedule(self, value):
        self._working_schedule = value


    def to_alipay_dict(self):
        params = dict()
        if self.accept_conditions:
            if hasattr(self.accept_conditions, 'to_alipay_dict'):
                params['accept_conditions'] = self.accept_conditions.to_alipay_dict()
            else:
                params['accept_conditions'] = self.accept_conditions
        if self.category:
            if isinstance(self.category, list):
                for i in range(0, len(self.category)):
                    element = self.category[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category[i] = element.to_alipay_dict()
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.checklist:
            if isinstance(self.checklist, list):
                for i in range(0, len(self.checklist)):
                    element = self.checklist[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.checklist[i] = element.to_alipay_dict()
            if hasattr(self.checklist, 'to_alipay_dict'):
                params['checklist'] = self.checklist.to_alipay_dict()
            else:
                params['checklist'] = self.checklist
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.contact:
            if isinstance(self.contact, list):
                for i in range(0, len(self.contact)):
                    element = self.contact[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact[i] = element.to_alipay_dict()
            if hasattr(self.contact, 'to_alipay_dict'):
                params['contact'] = self.contact.to_alipay_dict()
            else:
                params['contact'] = self.contact
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.implementation_subject:
            if hasattr(self.implementation_subject, 'to_alipay_dict'):
                params['implementation_subject'] = self.implementation_subject.to_alipay_dict()
            else:
                params['implementation_subject'] = self.implementation_subject
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.online_support:
            if hasattr(self.online_support, 'to_alipay_dict'):
                params['online_support'] = self.online_support.to_alipay_dict()
            else:
                params['online_support'] = self.online_support
        if self.palm_support:
            if hasattr(self.palm_support, 'to_alipay_dict'):
                params['palm_support'] = self.palm_support.to_alipay_dict()
            else:
                params['palm_support'] = self.palm_support
        if self.palm_url:
            if hasattr(self.palm_url, 'to_alipay_dict'):
                params['palm_url'] = self.palm_url.to_alipay_dict()
            else:
                params['palm_url'] = self.palm_url
        if self.rel_service:
            if hasattr(self.rel_service, 'to_alipay_dict'):
                params['rel_service'] = self.rel_service.to_alipay_dict()
            else:
                params['rel_service'] = self.rel_service
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.service_object:
            if hasattr(self.service_object, 'to_alipay_dict'):
                params['service_object'] = self.service_object.to_alipay_dict()
            else:
                params['service_object'] = self.service_object
        if self.subject_juridical:
            if isinstance(self.subject_juridical, list):
                for i in range(0, len(self.subject_juridical)):
                    element = self.subject_juridical[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subject_juridical[i] = element.to_alipay_dict()
            if hasattr(self.subject_juridical, 'to_alipay_dict'):
                params['subject_juridical'] = self.subject_juridical.to_alipay_dict()
            else:
                params['subject_juridical'] = self.subject_juridical
        if self.subject_nature:
            if isinstance(self.subject_nature, list):
                for i in range(0, len(self.subject_nature)):
                    element = self.subject_nature[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.subject_nature[i] = element.to_alipay_dict()
            if hasattr(self.subject_nature, 'to_alipay_dict'):
                params['subject_nature'] = self.subject_nature.to_alipay_dict()
            else:
                params['subject_nature'] = self.subject_nature
        if self.working_schedule:
            if hasattr(self.working_schedule, 'to_alipay_dict'):
                params['working_schedule'] = self.working_schedule.to_alipay_dict()
            else:
                params['working_schedule'] = self.working_schedule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemGwDTO()
        if 'accept_conditions' in d:
            o.accept_conditions = d['accept_conditions']
        if 'category' in d:
            o.category = d['category']
        if 'checklist' in d:
            o.checklist = d['checklist']
        if 'code' in d:
            o.code = d['code']
        if 'contact' in d:
            o.contact = d['contact']
        if 'district' in d:
            o.district = d['district']
        if 'implementation_subject' in d:
            o.implementation_subject = d['implementation_subject']
        if 'link' in d:
            o.link = d['link']
        if 'name' in d:
            o.name = d['name']
        if 'online_support' in d:
            o.online_support = d['online_support']
        if 'palm_support' in d:
            o.palm_support = d['palm_support']
        if 'palm_url' in d:
            o.palm_url = d['palm_url']
        if 'rel_service' in d:
            o.rel_service = d['rel_service']
        if 'scene' in d:
            o.scene = d['scene']
        if 'service_object' in d:
            o.service_object = d['service_object']
        if 'subject_juridical' in d:
            o.subject_juridical = d['subject_juridical']
        if 'subject_nature' in d:
            o.subject_nature = d['subject_nature']
        if 'working_schedule' in d:
            o.working_schedule = d['working_schedule']
        return o


