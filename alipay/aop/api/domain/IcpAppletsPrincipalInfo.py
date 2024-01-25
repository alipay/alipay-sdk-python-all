#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcpAppletsPrincipalInfo(object):

    def __init__(self):
        self._authorization_materials = None
        self._certificate_number = None
        self._certificate_photo_back = None
        self._certificate_photo_front = None
        self._certificate_type = None
        self._certificate_validate_end = None
        self._certificate_validate_start = None
        self._commit_letter_materials = None
        self._contact_email = None
        self._contact_emergency_phone_number = None
        self._contact_phone_number = None
        self._name = None

    @property
    def authorization_materials(self):
        return self._authorization_materials

    @authorization_materials.setter
    def authorization_materials(self, value):
        if isinstance(value, list):
            self._authorization_materials = list()
            for i in value:
                self._authorization_materials.append(i)
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def certificate_photo_back(self):
        return self._certificate_photo_back

    @certificate_photo_back.setter
    def certificate_photo_back(self, value):
        self._certificate_photo_back = value
    @property
    def certificate_photo_front(self):
        return self._certificate_photo_front

    @certificate_photo_front.setter
    def certificate_photo_front(self, value):
        self._certificate_photo_front = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def certificate_validate_end(self):
        return self._certificate_validate_end

    @certificate_validate_end.setter
    def certificate_validate_end(self, value):
        self._certificate_validate_end = value
    @property
    def certificate_validate_start(self):
        return self._certificate_validate_start

    @certificate_validate_start.setter
    def certificate_validate_start(self, value):
        self._certificate_validate_start = value
    @property
    def commit_letter_materials(self):
        return self._commit_letter_materials

    @commit_letter_materials.setter
    def commit_letter_materials(self, value):
        if isinstance(value, list):
            self._commit_letter_materials = list()
            for i in value:
                self._commit_letter_materials.append(i)
    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_emergency_phone_number(self):
        return self._contact_emergency_phone_number

    @contact_emergency_phone_number.setter
    def contact_emergency_phone_number(self, value):
        self._contact_emergency_phone_number = value
    @property
    def contact_phone_number(self):
        return self._contact_phone_number

    @contact_phone_number.setter
    def contact_phone_number(self, value):
        self._contact_phone_number = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorization_materials:
            if isinstance(self.authorization_materials, list):
                for i in range(0, len(self.authorization_materials)):
                    element = self.authorization_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.authorization_materials[i] = element.to_alipay_dict()
            if hasattr(self.authorization_materials, 'to_alipay_dict'):
                params['authorization_materials'] = self.authorization_materials.to_alipay_dict()
            else:
                params['authorization_materials'] = self.authorization_materials
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.certificate_photo_back:
            if hasattr(self.certificate_photo_back, 'to_alipay_dict'):
                params['certificate_photo_back'] = self.certificate_photo_back.to_alipay_dict()
            else:
                params['certificate_photo_back'] = self.certificate_photo_back
        if self.certificate_photo_front:
            if hasattr(self.certificate_photo_front, 'to_alipay_dict'):
                params['certificate_photo_front'] = self.certificate_photo_front.to_alipay_dict()
            else:
                params['certificate_photo_front'] = self.certificate_photo_front
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.certificate_validate_end:
            if hasattr(self.certificate_validate_end, 'to_alipay_dict'):
                params['certificate_validate_end'] = self.certificate_validate_end.to_alipay_dict()
            else:
                params['certificate_validate_end'] = self.certificate_validate_end
        if self.certificate_validate_start:
            if hasattr(self.certificate_validate_start, 'to_alipay_dict'):
                params['certificate_validate_start'] = self.certificate_validate_start.to_alipay_dict()
            else:
                params['certificate_validate_start'] = self.certificate_validate_start
        if self.commit_letter_materials:
            if isinstance(self.commit_letter_materials, list):
                for i in range(0, len(self.commit_letter_materials)):
                    element = self.commit_letter_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.commit_letter_materials[i] = element.to_alipay_dict()
            if hasattr(self.commit_letter_materials, 'to_alipay_dict'):
                params['commit_letter_materials'] = self.commit_letter_materials.to_alipay_dict()
            else:
                params['commit_letter_materials'] = self.commit_letter_materials
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_emergency_phone_number:
            if hasattr(self.contact_emergency_phone_number, 'to_alipay_dict'):
                params['contact_emergency_phone_number'] = self.contact_emergency_phone_number.to_alipay_dict()
            else:
                params['contact_emergency_phone_number'] = self.contact_emergency_phone_number
        if self.contact_phone_number:
            if hasattr(self.contact_phone_number, 'to_alipay_dict'):
                params['contact_phone_number'] = self.contact_phone_number.to_alipay_dict()
            else:
                params['contact_phone_number'] = self.contact_phone_number
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcpAppletsPrincipalInfo()
        if 'authorization_materials' in d:
            o.authorization_materials = d['authorization_materials']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'certificate_photo_back' in d:
            o.certificate_photo_back = d['certificate_photo_back']
        if 'certificate_photo_front' in d:
            o.certificate_photo_front = d['certificate_photo_front']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'certificate_validate_end' in d:
            o.certificate_validate_end = d['certificate_validate_end']
        if 'certificate_validate_start' in d:
            o.certificate_validate_start = d['certificate_validate_start']
        if 'commit_letter_materials' in d:
            o.commit_letter_materials = d['commit_letter_materials']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_emergency_phone_number' in d:
            o.contact_emergency_phone_number = d['contact_emergency_phone_number']
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        if 'name' in d:
            o.name = d['name']
        return o


