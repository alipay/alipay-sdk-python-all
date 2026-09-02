#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryDepartmentSyncModel(object):

    def __init__(self):
        self._address = None
        self._age_restriction = None
        self._data_version = None
        self._department_id = None
        self._department_name = None
        self._department_status = None
        self._dept_phone = None
        self._dept_sort = None
        self._dept_special = None
        self._description = None
        self._gender_restriction = None
        self._hospital_id = None
        self._isv_code = None
        self._level = None
        self._member_count = None
        self._parent_department_id = None
        self._parent_dept_name = None
        self._platform_code = None
        self._short_name = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self._age_restriction = value
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
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, value):
        self._department_name = value
    @property
    def department_status(self):
        return self._department_status

    @department_status.setter
    def department_status(self, value):
        self._department_status = value
    @property
    def dept_phone(self):
        return self._dept_phone

    @dept_phone.setter
    def dept_phone(self, value):
        self._dept_phone = value
    @property
    def dept_sort(self):
        return self._dept_sort

    @dept_sort.setter
    def dept_sort(self, value):
        self._dept_sort = value
    @property
    def dept_special(self):
        return self._dept_special

    @dept_special.setter
    def dept_special(self, value):
        self._dept_special = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def gender_restriction(self):
        return self._gender_restriction

    @gender_restriction.setter
    def gender_restriction(self, value):
        self._gender_restriction = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def member_count(self):
        return self._member_count

    @member_count.setter
    def member_count(self, value):
        self._member_count = value
    @property
    def parent_department_id(self):
        return self._parent_department_id

    @parent_department_id.setter
    def parent_department_id(self, value):
        self._parent_department_id = value
    @property
    def parent_dept_name(self):
        return self._parent_dept_name

    @parent_dept_name.setter
    def parent_dept_name(self, value):
        self._parent_dept_name = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.age_restriction:
            if hasattr(self.age_restriction, 'to_alipay_dict'):
                params['age_restriction'] = self.age_restriction.to_alipay_dict()
            else:
                params['age_restriction'] = self.age_restriction
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
        if self.department_name:
            if hasattr(self.department_name, 'to_alipay_dict'):
                params['department_name'] = self.department_name.to_alipay_dict()
            else:
                params['department_name'] = self.department_name
        if self.department_status:
            if hasattr(self.department_status, 'to_alipay_dict'):
                params['department_status'] = self.department_status.to_alipay_dict()
            else:
                params['department_status'] = self.department_status
        if self.dept_phone:
            if hasattr(self.dept_phone, 'to_alipay_dict'):
                params['dept_phone'] = self.dept_phone.to_alipay_dict()
            else:
                params['dept_phone'] = self.dept_phone
        if self.dept_sort:
            if hasattr(self.dept_sort, 'to_alipay_dict'):
                params['dept_sort'] = self.dept_sort.to_alipay_dict()
            else:
                params['dept_sort'] = self.dept_sort
        if self.dept_special:
            if hasattr(self.dept_special, 'to_alipay_dict'):
                params['dept_special'] = self.dept_special.to_alipay_dict()
            else:
                params['dept_special'] = self.dept_special
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.gender_restriction:
            if hasattr(self.gender_restriction, 'to_alipay_dict'):
                params['gender_restriction'] = self.gender_restriction.to_alipay_dict()
            else:
                params['gender_restriction'] = self.gender_restriction
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.member_count:
            if hasattr(self.member_count, 'to_alipay_dict'):
                params['member_count'] = self.member_count.to_alipay_dict()
            else:
                params['member_count'] = self.member_count
        if self.parent_department_id:
            if hasattr(self.parent_department_id, 'to_alipay_dict'):
                params['parent_department_id'] = self.parent_department_id.to_alipay_dict()
            else:
                params['parent_department_id'] = self.parent_department_id
        if self.parent_dept_name:
            if hasattr(self.parent_dept_name, 'to_alipay_dict'):
                params['parent_dept_name'] = self.parent_dept_name.to_alipay_dict()
            else:
                params['parent_dept_name'] = self.parent_dept_name
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryDepartmentSyncModel()
        if 'address' in d:
            o.address = d['address']
        if 'age_restriction' in d:
            o.age_restriction = d['age_restriction']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'department_id' in d:
            o.department_id = d['department_id']
        if 'department_name' in d:
            o.department_name = d['department_name']
        if 'department_status' in d:
            o.department_status = d['department_status']
        if 'dept_phone' in d:
            o.dept_phone = d['dept_phone']
        if 'dept_sort' in d:
            o.dept_sort = d['dept_sort']
        if 'dept_special' in d:
            o.dept_special = d['dept_special']
        if 'description' in d:
            o.description = d['description']
        if 'gender_restriction' in d:
            o.gender_restriction = d['gender_restriction']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'level' in d:
            o.level = d['level']
        if 'member_count' in d:
            o.member_count = d['member_count']
        if 'parent_department_id' in d:
            o.parent_department_id = d['parent_department_id']
        if 'parent_dept_name' in d:
            o.parent_dept_name = d['parent_dept_name']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'short_name' in d:
            o.short_name = d['short_name']
        return o


