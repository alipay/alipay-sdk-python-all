#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryDoctorUploadModel(object):

    def __init__(self):
        self._city_code = None
        self._data_version = None
        self._department_id = None
        self._doctor_category = None
        self._doctor_credential_id = None
        self._doctor_desc = None
        self._doctor_id = None
        self._doctor_name = None
        self._doctor_proficiency = None
        self._doctor_status = None
        self._doctor_title = None
        self._gender = None
        self._hospital_id = None
        self._id_card_number = None
        self._id_card_type = None
        self._img_url = None
        self._isv_code = None
        self._platform_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def department_id(self):
        return self._department_id

    @department_id.setter
    def department_id(self, value):
        self._department_id = value
    @property
    def doctor_category(self):
        return self._doctor_category

    @doctor_category.setter
    def doctor_category(self, value):
        self._doctor_category = value
    @property
    def doctor_credential_id(self):
        return self._doctor_credential_id

    @doctor_credential_id.setter
    def doctor_credential_id(self, value):
        self._doctor_credential_id = value
    @property
    def doctor_desc(self):
        return self._doctor_desc

    @doctor_desc.setter
    def doctor_desc(self, value):
        self._doctor_desc = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def doctor_name(self):
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value):
        self._doctor_name = value
    @property
    def doctor_proficiency(self):
        return self._doctor_proficiency

    @doctor_proficiency.setter
    def doctor_proficiency(self, value):
        self._doctor_proficiency = value
    @property
    def doctor_status(self):
        return self._doctor_status

    @doctor_status.setter
    def doctor_status(self, value):
        self._doctor_status = value
    @property
    def doctor_title(self):
        return self._doctor_title

    @doctor_title.setter
    def doctor_title(self, value):
        self._doctor_title = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def id_card_number(self):
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, value):
        self._id_card_number = value
    @property
    def id_card_type(self):
        return self._id_card_type

    @id_card_type.setter
    def id_card_type(self, value):
        self._id_card_type = value
    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        self._img_url = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.department_id:
            if hasattr(self.department_id, 'to_alipay_dict'):
                params['department_id'] = self.department_id.to_alipay_dict()
            else:
                params['department_id'] = self.department_id
        if self.doctor_category:
            if hasattr(self.doctor_category, 'to_alipay_dict'):
                params['doctor_category'] = self.doctor_category.to_alipay_dict()
            else:
                params['doctor_category'] = self.doctor_category
        if self.doctor_credential_id:
            if hasattr(self.doctor_credential_id, 'to_alipay_dict'):
                params['doctor_credential_id'] = self.doctor_credential_id.to_alipay_dict()
            else:
                params['doctor_credential_id'] = self.doctor_credential_id
        if self.doctor_desc:
            if hasattr(self.doctor_desc, 'to_alipay_dict'):
                params['doctor_desc'] = self.doctor_desc.to_alipay_dict()
            else:
                params['doctor_desc'] = self.doctor_desc
        if self.doctor_id:
            if hasattr(self.doctor_id, 'to_alipay_dict'):
                params['doctor_id'] = self.doctor_id.to_alipay_dict()
            else:
                params['doctor_id'] = self.doctor_id
        if self.doctor_name:
            if hasattr(self.doctor_name, 'to_alipay_dict'):
                params['doctor_name'] = self.doctor_name.to_alipay_dict()
            else:
                params['doctor_name'] = self.doctor_name
        if self.doctor_proficiency:
            if hasattr(self.doctor_proficiency, 'to_alipay_dict'):
                params['doctor_proficiency'] = self.doctor_proficiency.to_alipay_dict()
            else:
                params['doctor_proficiency'] = self.doctor_proficiency
        if self.doctor_status:
            if hasattr(self.doctor_status, 'to_alipay_dict'):
                params['doctor_status'] = self.doctor_status.to_alipay_dict()
            else:
                params['doctor_status'] = self.doctor_status
        if self.doctor_title:
            if hasattr(self.doctor_title, 'to_alipay_dict'):
                params['doctor_title'] = self.doctor_title.to_alipay_dict()
            else:
                params['doctor_title'] = self.doctor_title
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.id_card_number:
            if hasattr(self.id_card_number, 'to_alipay_dict'):
                params['id_card_number'] = self.id_card_number.to_alipay_dict()
            else:
                params['id_card_number'] = self.id_card_number
        if self.id_card_type:
            if hasattr(self.id_card_type, 'to_alipay_dict'):
                params['id_card_type'] = self.id_card_type.to_alipay_dict()
            else:
                params['id_card_type'] = self.id_card_type
        if self.img_url:
            if hasattr(self.img_url, 'to_alipay_dict'):
                params['img_url'] = self.img_url.to_alipay_dict()
            else:
                params['img_url'] = self.img_url
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryDoctorUploadModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'doctor_category' in d:
            o.doctor_category = d['doctor_category']
        if 'doctor_credential_id' in d:
            o.doctor_credential_id = d['doctor_credential_id']
        if 'doctor_desc' in d:
            o.doctor_desc = d['doctor_desc']
        if 'doctor_id' in d:
            o.doctor_id = d['doctor_id']
        if 'doctor_name' in d:
            o.doctor_name = d['doctor_name']
        if 'doctor_proficiency' in d:
            o.doctor_proficiency = d['doctor_proficiency']
        if 'doctor_status' in d:
            o.doctor_status = d['doctor_status']
        if 'doctor_title' in d:
            o.doctor_title = d['doctor_title']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'id_card_number' in d:
            o.id_card_number = d['id_card_number']
        if 'id_card_type' in d:
            o.id_card_type = d['id_card_type']
        if 'img_url' in d:
            o.img_url = d['img_url']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        return o


