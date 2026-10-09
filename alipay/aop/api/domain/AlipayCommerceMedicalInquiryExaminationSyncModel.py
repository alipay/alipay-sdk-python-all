#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryExaminationSyncModel(object):

    def __init__(self):
        self._data_status = None
        self._data_version = None
        self._equipment_type = None
        self._examination_category = None
        self._examination_desc = None
        self._examination_id = None
        self._examination_name = None
        self._examination_site = None
        self._hospital_id = None
        self._hospital_name = None
        self._isv_code = None
        self._platform_code = None
        self._precautions = None
        self._standard_examination_name = None

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
    def equipment_type(self):
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, value):
        self._equipment_type = value
    @property
    def examination_category(self):
        return self._examination_category

    @examination_category.setter
    def examination_category(self, value):
        self._examination_category = value
    @property
    def examination_desc(self):
        return self._examination_desc

    @examination_desc.setter
    def examination_desc(self, value):
        self._examination_desc = value
    @property
    def examination_id(self):
        return self._examination_id

    @examination_id.setter
    def examination_id(self, value):
        self._examination_id = value
    @property
    def examination_name(self):
        return self._examination_name

    @examination_name.setter
    def examination_name(self, value):
        self._examination_name = value
    @property
    def examination_site(self):
        return self._examination_site

    @examination_site.setter
    def examination_site(self, value):
        self._examination_site = value
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
    def standard_examination_name(self):
        return self._standard_examination_name

    @standard_examination_name.setter
    def standard_examination_name(self, value):
        self._standard_examination_name = value


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
        if self.equipment_type:
            if hasattr(self.equipment_type, 'to_alipay_dict'):
                params['equipment_type'] = self.equipment_type.to_alipay_dict()
            else:
                params['equipment_type'] = self.equipment_type
        if self.examination_category:
            if hasattr(self.examination_category, 'to_alipay_dict'):
                params['examination_category'] = self.examination_category.to_alipay_dict()
            else:
                params['examination_category'] = self.examination_category
        if self.examination_desc:
            if hasattr(self.examination_desc, 'to_alipay_dict'):
                params['examination_desc'] = self.examination_desc.to_alipay_dict()
            else:
                params['examination_desc'] = self.examination_desc
        if self.examination_id:
            if hasattr(self.examination_id, 'to_alipay_dict'):
                params['examination_id'] = self.examination_id.to_alipay_dict()
            else:
                params['examination_id'] = self.examination_id
        if self.examination_name:
            if hasattr(self.examination_name, 'to_alipay_dict'):
                params['examination_name'] = self.examination_name.to_alipay_dict()
            else:
                params['examination_name'] = self.examination_name
        if self.examination_site:
            if hasattr(self.examination_site, 'to_alipay_dict'):
                params['examination_site'] = self.examination_site.to_alipay_dict()
            else:
                params['examination_site'] = self.examination_site
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
        if self.standard_examination_name:
            if hasattr(self.standard_examination_name, 'to_alipay_dict'):
                params['standard_examination_name'] = self.standard_examination_name.to_alipay_dict()
            else:
                params['standard_examination_name'] = self.standard_examination_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryExaminationSyncModel()
        if 'data_status' in d:
            o.data_status = d['data_status']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'equipment_type' in d:
            o.equipment_type = d['equipment_type']
        if 'examination_category' in d:
            o.examination_category = d['examination_category']
        if 'examination_desc' in d:
            o.examination_desc = d['examination_desc']
        if 'examination_id' in d:
            o.examination_id = d['examination_id']
        if 'examination_name' in d:
            o.examination_name = d['examination_name']
        if 'examination_site' in d:
            o.examination_site = d['examination_site']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'precautions' in d:
            o.precautions = d['precautions']
        if 'standard_examination_name' in d:
            o.standard_examination_name = d['standard_examination_name']
        return o


