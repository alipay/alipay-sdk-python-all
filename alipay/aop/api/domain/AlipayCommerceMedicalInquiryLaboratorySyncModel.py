#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryLaboratorySyncModel(object):

    def __init__(self):
        self._data_status = None
        self._data_version = None
        self._hospital_id = None
        self._hospital_name = None
        self._isv_code = None
        self._laboratory_category = None
        self._laboratory_desc = None
        self._laboratory_id = None
        self._laboratory_name = None
        self._package_flag = None
        self._package_name = None
        self._platform_code = None
        self._precautions = None
        self._reference_range = None
        self._specimen_type = None

    @property
    def data_status(self):
        return self._data_status

    @data_status.setter
    def data_status(self, value):
        self._data_status = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def laboratory_category(self):
        return self._laboratory_category

    @laboratory_category.setter
    def laboratory_category(self, value):
        self._laboratory_category = value
    @property
    def laboratory_desc(self):
        return self._laboratory_desc

    @laboratory_desc.setter
    def laboratory_desc(self, value):
        self._laboratory_desc = value
    @property
    def laboratory_id(self):
        return self._laboratory_id

    @laboratory_id.setter
    def laboratory_id(self, value):
        self._laboratory_id = value
    @property
    def laboratory_name(self):
        return self._laboratory_name

    @laboratory_name.setter
    def laboratory_name(self, value):
        self._laboratory_name = value
    @property
    def package_flag(self):
        return self._package_flag

    @package_flag.setter
    def package_flag(self, value):
        self._package_flag = value
    @property
    def package_name(self):
        return self._package_name

    @package_name.setter
    def package_name(self, value):
        self._package_name = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def precautions(self):
        return self._precautions

    @precautions.setter
    def precautions(self, value):
        self._precautions = value
    @property
    def reference_range(self):
        return self._reference_range

    @reference_range.setter
    def reference_range(self, value):
        self._reference_range = value
    @property
    def specimen_type(self):
        return self._specimen_type

    @specimen_type.setter
    def specimen_type(self, value):
        self._specimen_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_status:
            if hasattr(self.data_status, 'to_alipay_dict'):
                params['data_status'] = self.data_status.to_alipay_dict()
            else:
                params['data_status'] = self.data_status
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.laboratory_category:
            if hasattr(self.laboratory_category, 'to_alipay_dict'):
                params['laboratory_category'] = self.laboratory_category.to_alipay_dict()
            else:
                params['laboratory_category'] = self.laboratory_category
        if self.laboratory_desc:
            if hasattr(self.laboratory_desc, 'to_alipay_dict'):
                params['laboratory_desc'] = self.laboratory_desc.to_alipay_dict()
            else:
                params['laboratory_desc'] = self.laboratory_desc
        if self.laboratory_id:
            if hasattr(self.laboratory_id, 'to_alipay_dict'):
                params['laboratory_id'] = self.laboratory_id.to_alipay_dict()
            else:
                params['laboratory_id'] = self.laboratory_id
        if self.laboratory_name:
            if hasattr(self.laboratory_name, 'to_alipay_dict'):
                params['laboratory_name'] = self.laboratory_name.to_alipay_dict()
            else:
                params['laboratory_name'] = self.laboratory_name
        if self.package_flag:
            if hasattr(self.package_flag, 'to_alipay_dict'):
                params['package_flag'] = self.package_flag.to_alipay_dict()
            else:
                params['package_flag'] = self.package_flag
        if self.package_name:
            if hasattr(self.package_name, 'to_alipay_dict'):
                params['package_name'] = self.package_name.to_alipay_dict()
            else:
                params['package_name'] = self.package_name
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.precautions:
            if hasattr(self.precautions, 'to_alipay_dict'):
                params['precautions'] = self.precautions.to_alipay_dict()
            else:
                params['precautions'] = self.precautions
        if self.reference_range:
            if hasattr(self.reference_range, 'to_alipay_dict'):
                params['reference_range'] = self.reference_range.to_alipay_dict()
            else:
                params['reference_range'] = self.reference_range
        if self.specimen_type:
            if hasattr(self.specimen_type, 'to_alipay_dict'):
                params['specimen_type'] = self.specimen_type.to_alipay_dict()
            else:
                params['specimen_type'] = self.specimen_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryLaboratorySyncModel()
        if 'data_status' in d:
            o.data_status = d['data_status']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'laboratory_category' in d:
            o.laboratory_category = d['laboratory_category']
        if 'laboratory_desc' in d:
            o.laboratory_desc = d['laboratory_desc']
        if 'laboratory_id' in d:
            o.laboratory_id = d['laboratory_id']
        if 'laboratory_name' in d:
            o.laboratory_name = d['laboratory_name']
        if 'package_flag' in d:
            o.package_flag = d['package_flag']
        if 'package_name' in d:
            o.package_name = d['package_name']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'precautions' in d:
            o.precautions = d['precautions']
        if 'reference_range' in d:
            o.reference_range = d['reference_range']
        if 'specimen_type' in d:
            o.specimen_type = d['specimen_type']
        return o


