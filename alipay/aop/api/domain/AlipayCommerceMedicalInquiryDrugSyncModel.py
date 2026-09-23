#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInquiryDrugSyncModel(object):

    def __init__(self):
        self._approval_number = None
        self._chinese_standard_code = None
        self._data_version = None
        self._default_frequency = None
        self._default_route = None
        self._dosage_form = None
        self._drug_category = None
        self._drug_classification = None
        self._drug_generic_name = None
        self._drug_id = None
        self._drug_name = None
        self._drug_pinyin_code = None
        self._drug_status = None
        self._drug_trade_name = None
        self._hospital_id = None
        self._is_hospital_preparation = None
        self._is_original_drug = None
        self._isv_code = None
        self._manufacturer = None
        self._medical_insurance_code = None
        self._min_dose_unit = None
        self._min_package_unit = None
        self._origin = None
        self._pharmacy_unit = None
        self._platform_code = None
        self._regulatory_level = None
        self._specification = None
        self._upc_code = None

    @property
    def approval_number(self):
        return self._approval_number

    @approval_number.setter
    def approval_number(self, value):
        self._approval_number = value
    @property
    def chinese_standard_code(self):
        return self._chinese_standard_code

    @chinese_standard_code.setter
    def chinese_standard_code(self, value):
        self._chinese_standard_code = value
    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def default_frequency(self):
        return self._default_frequency

    @default_frequency.setter
    def default_frequency(self, value):
        self._default_frequency = value
    @property
    def default_route(self):
        return self._default_route

    @default_route.setter
    def default_route(self, value):
        self._default_route = value
    @property
    def dosage_form(self):
        return self._dosage_form

    @dosage_form.setter
    def dosage_form(self, value):
        self._dosage_form = value
    @property
    def drug_category(self):
        return self._drug_category

    @drug_category.setter
    def drug_category(self, value):
        self._drug_category = value
    @property
    def drug_classification(self):
        return self._drug_classification

    @drug_classification.setter
    def drug_classification(self, value):
        self._drug_classification = value
    @property
    def drug_generic_name(self):
        return self._drug_generic_name

    @drug_generic_name.setter
    def drug_generic_name(self, value):
        self._drug_generic_name = value
    @property
    def drug_id(self):
        return self._drug_id

    @drug_id.setter
    def drug_id(self, value):
        self._drug_id = value
    @property
    def drug_name(self):
        return self._drug_name

    @drug_name.setter
    def drug_name(self, value):
        self._drug_name = value
    @property
    def drug_pinyin_code(self):
        return self._drug_pinyin_code

    @drug_pinyin_code.setter
    def drug_pinyin_code(self, value):
        self._drug_pinyin_code = value
    @property
    def drug_status(self):
        return self._drug_status

    @drug_status.setter
    def drug_status(self, value):
        self._drug_status = value
    @property
    def drug_trade_name(self):
        return self._drug_trade_name

    @drug_trade_name.setter
    def drug_trade_name(self, value):
        self._drug_trade_name = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def is_hospital_preparation(self):
        return self._is_hospital_preparation

    @is_hospital_preparation.setter
    def is_hospital_preparation(self, value):
        self._is_hospital_preparation = value
    @property
    def is_original_drug(self):
        return self._is_original_drug

    @is_original_drug.setter
    def is_original_drug(self, value):
        self._is_original_drug = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    @property
    def medical_insurance_code(self):
        return self._medical_insurance_code

    @medical_insurance_code.setter
    def medical_insurance_code(self, value):
        self._medical_insurance_code = value
    @property
    def min_dose_unit(self):
        return self._min_dose_unit

    @min_dose_unit.setter
    def min_dose_unit(self, value):
        self._min_dose_unit = value
    @property
    def min_package_unit(self):
        return self._min_package_unit

    @min_package_unit.setter
    def min_package_unit(self, value):
        self._min_package_unit = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
    @property
    def pharmacy_unit(self):
        return self._pharmacy_unit

    @pharmacy_unit.setter
    def pharmacy_unit(self, value):
        self._pharmacy_unit = value
    @property
    def platform_code(self):
        return self._platform_code

    @platform_code.setter
    def platform_code(self, value):
        self._platform_code = value
    @property
    def regulatory_level(self):
        return self._regulatory_level

    @regulatory_level.setter
    def regulatory_level(self, value):
        self._regulatory_level = value
    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._specification = value
    @property
    def upc_code(self):
        return self._upc_code

    @upc_code.setter
    def upc_code(self, value):
        self._upc_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.approval_number:
            if hasattr(self.approval_number, 'to_alipay_dict'):
                params['approval_number'] = self.approval_number.to_alipay_dict()
            else:
                params['approval_number'] = self.approval_number
        if self.chinese_standard_code:
            if hasattr(self.chinese_standard_code, 'to_alipay_dict'):
                params['chinese_standard_code'] = self.chinese_standard_code.to_alipay_dict()
            else:
                params['chinese_standard_code'] = self.chinese_standard_code
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.default_frequency:
            if hasattr(self.default_frequency, 'to_alipay_dict'):
                params['default_frequency'] = self.default_frequency.to_alipay_dict()
            else:
                params['default_frequency'] = self.default_frequency
        if self.default_route:
            if hasattr(self.default_route, 'to_alipay_dict'):
                params['default_route'] = self.default_route.to_alipay_dict()
            else:
                params['default_route'] = self.default_route
        if self.dosage_form:
            if hasattr(self.dosage_form, 'to_alipay_dict'):
                params['dosage_form'] = self.dosage_form.to_alipay_dict()
            else:
                params['dosage_form'] = self.dosage_form
        if self.drug_category:
            if hasattr(self.drug_category, 'to_alipay_dict'):
                params['drug_category'] = self.drug_category.to_alipay_dict()
            else:
                params['drug_category'] = self.drug_category
        if self.drug_classification:
            if hasattr(self.drug_classification, 'to_alipay_dict'):
                params['drug_classification'] = self.drug_classification.to_alipay_dict()
            else:
                params['drug_classification'] = self.drug_classification
        if self.drug_generic_name:
            if hasattr(self.drug_generic_name, 'to_alipay_dict'):
                params['drug_generic_name'] = self.drug_generic_name.to_alipay_dict()
            else:
                params['drug_generic_name'] = self.drug_generic_name
        if self.drug_id:
            if hasattr(self.drug_id, 'to_alipay_dict'):
                params['drug_id'] = self.drug_id.to_alipay_dict()
            else:
                params['drug_id'] = self.drug_id
        if self.drug_name:
            if hasattr(self.drug_name, 'to_alipay_dict'):
                params['drug_name'] = self.drug_name.to_alipay_dict()
            else:
                params['drug_name'] = self.drug_name
        if self.drug_pinyin_code:
            if hasattr(self.drug_pinyin_code, 'to_alipay_dict'):
                params['drug_pinyin_code'] = self.drug_pinyin_code.to_alipay_dict()
            else:
                params['drug_pinyin_code'] = self.drug_pinyin_code
        if self.drug_status:
            if hasattr(self.drug_status, 'to_alipay_dict'):
                params['drug_status'] = self.drug_status.to_alipay_dict()
            else:
                params['drug_status'] = self.drug_status
        if self.drug_trade_name:
            if hasattr(self.drug_trade_name, 'to_alipay_dict'):
                params['drug_trade_name'] = self.drug_trade_name.to_alipay_dict()
            else:
                params['drug_trade_name'] = self.drug_trade_name
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.is_hospital_preparation:
            if hasattr(self.is_hospital_preparation, 'to_alipay_dict'):
                params['is_hospital_preparation'] = self.is_hospital_preparation.to_alipay_dict()
            else:
                params['is_hospital_preparation'] = self.is_hospital_preparation
        if self.is_original_drug:
            if hasattr(self.is_original_drug, 'to_alipay_dict'):
                params['is_original_drug'] = self.is_original_drug.to_alipay_dict()
            else:
                params['is_original_drug'] = self.is_original_drug
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.manufacturer:
            if hasattr(self.manufacturer, 'to_alipay_dict'):
                params['manufacturer'] = self.manufacturer.to_alipay_dict()
            else:
                params['manufacturer'] = self.manufacturer
        if self.medical_insurance_code:
            if hasattr(self.medical_insurance_code, 'to_alipay_dict'):
                params['medical_insurance_code'] = self.medical_insurance_code.to_alipay_dict()
            else:
                params['medical_insurance_code'] = self.medical_insurance_code
        if self.min_dose_unit:
            if hasattr(self.min_dose_unit, 'to_alipay_dict'):
                params['min_dose_unit'] = self.min_dose_unit.to_alipay_dict()
            else:
                params['min_dose_unit'] = self.min_dose_unit
        if self.min_package_unit:
            if hasattr(self.min_package_unit, 'to_alipay_dict'):
                params['min_package_unit'] = self.min_package_unit.to_alipay_dict()
            else:
                params['min_package_unit'] = self.min_package_unit
        if self.origin:
            if hasattr(self.origin, 'to_alipay_dict'):
                params['origin'] = self.origin.to_alipay_dict()
            else:
                params['origin'] = self.origin
        if self.pharmacy_unit:
            if hasattr(self.pharmacy_unit, 'to_alipay_dict'):
                params['pharmacy_unit'] = self.pharmacy_unit.to_alipay_dict()
            else:
                params['pharmacy_unit'] = self.pharmacy_unit
        if self.platform_code:
            if hasattr(self.platform_code, 'to_alipay_dict'):
                params['platform_code'] = self.platform_code.to_alipay_dict()
            else:
                params['platform_code'] = self.platform_code
        if self.regulatory_level:
            if hasattr(self.regulatory_level, 'to_alipay_dict'):
                params['regulatory_level'] = self.regulatory_level.to_alipay_dict()
            else:
                params['regulatory_level'] = self.regulatory_level
        if self.specification:
            if hasattr(self.specification, 'to_alipay_dict'):
                params['specification'] = self.specification.to_alipay_dict()
            else:
                params['specification'] = self.specification
        if self.upc_code:
            if hasattr(self.upc_code, 'to_alipay_dict'):
                params['upc_code'] = self.upc_code.to_alipay_dict()
            else:
                params['upc_code'] = self.upc_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInquiryDrugSyncModel()
        if 'approval_number' in d:
            o.approval_number = d['approval_number']
        if 'chinese_standard_code' in d:
            o.chinese_standard_code = d['chinese_standard_code']
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'default_frequency' in d:
            o.default_frequency = d['default_frequency']
        if 'default_route' in d:
            o.default_route = d['default_route']
        if 'dosage_form' in d:
            o.dosage_form = d['dosage_form']
        if 'drug_category' in d:
            o.drug_category = d['drug_category']
        if 'drug_classification' in d:
            o.drug_classification = d['drug_classification']
        if 'drug_generic_name' in d:
            o.drug_generic_name = d['drug_generic_name']
        if 'drug_id' in d:
            o.drug_id = d['drug_id']
        if 'drug_name' in d:
            o.drug_name = d['drug_name']
        if 'drug_pinyin_code' in d:
            o.drug_pinyin_code = d['drug_pinyin_code']
        if 'drug_status' in d:
            o.drug_status = d['drug_status']
        if 'drug_trade_name' in d:
            o.drug_trade_name = d['drug_trade_name']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'is_hospital_preparation' in d:
            o.is_hospital_preparation = d['is_hospital_preparation']
        if 'is_original_drug' in d:
            o.is_original_drug = d['is_original_drug']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'manufacturer' in d:
            o.manufacturer = d['manufacturer']
        if 'medical_insurance_code' in d:
            o.medical_insurance_code = d['medical_insurance_code']
        if 'min_dose_unit' in d:
            o.min_dose_unit = d['min_dose_unit']
        if 'min_package_unit' in d:
            o.min_package_unit = d['min_package_unit']
        if 'origin' in d:
            o.origin = d['origin']
        if 'pharmacy_unit' in d:
            o.pharmacy_unit = d['pharmacy_unit']
        if 'platform_code' in d:
            o.platform_code = d['platform_code']
        if 'regulatory_level' in d:
            o.regulatory_level = d['regulatory_level']
        if 'specification' in d:
            o.specification = d['specification']
        if 'upc_code' in d:
            o.upc_code = d['upc_code']
        return o


