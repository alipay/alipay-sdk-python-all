#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IcpSubjectInfo(object):

    def __init__(self):
        self._address = None
        self._attachement_materials = None
        self._authorization_material = None
        self._certificate_address = None
        self._certificate_number = None
        self._certificate_photo = None
        self._certificate_type = None
        self._certify_id = None
        self._city = None
        self._comment = None
        self._contact_email = None
        self._contact_emergency_phone_number = None
        self._contact_phone_number = None
        self._directer_certificate_number = None
        self._directer_certificate_photo_back = None
        self._directer_certificate_photo_front = None
        self._directer_certificate_type = None
        self._directer_certificate_validate_end = None
        self._directer_certificate_validate_start = None
        self._directer_name = None
        self._district = None
        self._name = None
        self._province = None
        self._type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def attachement_materials(self):
        return self._attachement_materials

    @attachement_materials.setter
    def attachement_materials(self, value):
        if isinstance(value, list):
            self._attachement_materials = list()
            for i in value:
                self._attachement_materials.append(i)
    @property
    def authorization_material(self):
        return self._authorization_material

    @authorization_material.setter
    def authorization_material(self, value):
        self._authorization_material = value
    @property
    def certificate_address(self):
        return self._certificate_address

    @certificate_address.setter
    def certificate_address(self, value):
        self._certificate_address = value
    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def certificate_photo(self):
        return self._certificate_photo

    @certificate_photo.setter
    def certificate_photo(self, value):
        self._certificate_photo = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
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
    def directer_certificate_number(self):
        return self._directer_certificate_number

    @directer_certificate_number.setter
    def directer_certificate_number(self, value):
        self._directer_certificate_number = value
    @property
    def directer_certificate_photo_back(self):
        return self._directer_certificate_photo_back

    @directer_certificate_photo_back.setter
    def directer_certificate_photo_back(self, value):
        self._directer_certificate_photo_back = value
    @property
    def directer_certificate_photo_front(self):
        return self._directer_certificate_photo_front

    @directer_certificate_photo_front.setter
    def directer_certificate_photo_front(self, value):
        self._directer_certificate_photo_front = value
    @property
    def directer_certificate_type(self):
        return self._directer_certificate_type

    @directer_certificate_type.setter
    def directer_certificate_type(self, value):
        self._directer_certificate_type = value
    @property
    def directer_certificate_validate_end(self):
        return self._directer_certificate_validate_end

    @directer_certificate_validate_end.setter
    def directer_certificate_validate_end(self, value):
        self._directer_certificate_validate_end = value
    @property
    def directer_certificate_validate_start(self):
        return self._directer_certificate_validate_start

    @directer_certificate_validate_start.setter
    def directer_certificate_validate_start(self, value):
        self._directer_certificate_validate_start = value
    @property
    def directer_name(self):
        return self._directer_name

    @directer_name.setter
    def directer_name(self, value):
        self._directer_name = value
    @property
    def district(self):
        return self._district

    @district.setter
    def district(self, value):
        self._district = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.attachement_materials:
            if isinstance(self.attachement_materials, list):
                for i in range(0, len(self.attachement_materials)):
                    element = self.attachement_materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachement_materials[i] = element.to_alipay_dict()
            if hasattr(self.attachement_materials, 'to_alipay_dict'):
                params['attachement_materials'] = self.attachement_materials.to_alipay_dict()
            else:
                params['attachement_materials'] = self.attachement_materials
        if self.authorization_material:
            if hasattr(self.authorization_material, 'to_alipay_dict'):
                params['authorization_material'] = self.authorization_material.to_alipay_dict()
            else:
                params['authorization_material'] = self.authorization_material
        if self.certificate_address:
            if hasattr(self.certificate_address, 'to_alipay_dict'):
                params['certificate_address'] = self.certificate_address.to_alipay_dict()
            else:
                params['certificate_address'] = self.certificate_address
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.certificate_photo:
            if hasattr(self.certificate_photo, 'to_alipay_dict'):
                params['certificate_photo'] = self.certificate_photo.to_alipay_dict()
            else:
                params['certificate_photo'] = self.certificate_photo
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.certify_id:
            if hasattr(self.certify_id, 'to_alipay_dict'):
                params['certify_id'] = self.certify_id.to_alipay_dict()
            else:
                params['certify_id'] = self.certify_id
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
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
        if self.directer_certificate_number:
            if hasattr(self.directer_certificate_number, 'to_alipay_dict'):
                params['directer_certificate_number'] = self.directer_certificate_number.to_alipay_dict()
            else:
                params['directer_certificate_number'] = self.directer_certificate_number
        if self.directer_certificate_photo_back:
            if hasattr(self.directer_certificate_photo_back, 'to_alipay_dict'):
                params['directer_certificate_photo_back'] = self.directer_certificate_photo_back.to_alipay_dict()
            else:
                params['directer_certificate_photo_back'] = self.directer_certificate_photo_back
        if self.directer_certificate_photo_front:
            if hasattr(self.directer_certificate_photo_front, 'to_alipay_dict'):
                params['directer_certificate_photo_front'] = self.directer_certificate_photo_front.to_alipay_dict()
            else:
                params['directer_certificate_photo_front'] = self.directer_certificate_photo_front
        if self.directer_certificate_type:
            if hasattr(self.directer_certificate_type, 'to_alipay_dict'):
                params['directer_certificate_type'] = self.directer_certificate_type.to_alipay_dict()
            else:
                params['directer_certificate_type'] = self.directer_certificate_type
        if self.directer_certificate_validate_end:
            if hasattr(self.directer_certificate_validate_end, 'to_alipay_dict'):
                params['directer_certificate_validate_end'] = self.directer_certificate_validate_end.to_alipay_dict()
            else:
                params['directer_certificate_validate_end'] = self.directer_certificate_validate_end
        if self.directer_certificate_validate_start:
            if hasattr(self.directer_certificate_validate_start, 'to_alipay_dict'):
                params['directer_certificate_validate_start'] = self.directer_certificate_validate_start.to_alipay_dict()
            else:
                params['directer_certificate_validate_start'] = self.directer_certificate_validate_start
        if self.directer_name:
            if hasattr(self.directer_name, 'to_alipay_dict'):
                params['directer_name'] = self.directer_name.to_alipay_dict()
            else:
                params['directer_name'] = self.directer_name
        if self.district:
            if hasattr(self.district, 'to_alipay_dict'):
                params['district'] = self.district.to_alipay_dict()
            else:
                params['district'] = self.district
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IcpSubjectInfo()
        if 'address' in d:
            o.address = d['address']
        if 'attachement_materials' in d:
            o.attachement_materials = d['attachement_materials']
        if 'authorization_material' in d:
            o.authorization_material = d['authorization_material']
        if 'certificate_address' in d:
            o.certificate_address = d['certificate_address']
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'certificate_photo' in d:
            o.certificate_photo = d['certificate_photo']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'certify_id' in d:
            o.certify_id = d['certify_id']
        if 'city' in d:
            o.city = d['city']
        if 'comment' in d:
            o.comment = d['comment']
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_emergency_phone_number' in d:
            o.contact_emergency_phone_number = d['contact_emergency_phone_number']
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        if 'directer_certificate_number' in d:
            o.directer_certificate_number = d['directer_certificate_number']
        if 'directer_certificate_photo_back' in d:
            o.directer_certificate_photo_back = d['directer_certificate_photo_back']
        if 'directer_certificate_photo_front' in d:
            o.directer_certificate_photo_front = d['directer_certificate_photo_front']
        if 'directer_certificate_type' in d:
            o.directer_certificate_type = d['directer_certificate_type']
        if 'directer_certificate_validate_end' in d:
            o.directer_certificate_validate_end = d['directer_certificate_validate_end']
        if 'directer_certificate_validate_start' in d:
            o.directer_certificate_validate_start = d['directer_certificate_validate_start']
        if 'directer_name' in d:
            o.directer_name = d['directer_name']
        if 'district' in d:
            o.district = d['district']
        if 'name' in d:
            o.name = d['name']
        if 'province' in d:
            o.province = d['province']
        if 'type' in d:
            o.type = d['type']
        return o


