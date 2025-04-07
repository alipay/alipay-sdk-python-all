#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrugInfo(object):

    def __init__(self):
        self._brand_name = None
        self._diagnosis = None
        self._drug_cnt = None
        self._drug_dosform = None
        self._drug_pic_url = None
        self._drug_type = None
        self._drug_unit_desc = None
        self._ext_drug_code = None
        self._ext_drug_name = None
        self._generic_name = None
        self._spec = None
        self._usage_dosage_desc = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value
    @property
    def drug_cnt(self):
        return self._drug_cnt

    @drug_cnt.setter
    def drug_cnt(self, value):
        self._drug_cnt = value
    @property
    def drug_dosform(self):
        return self._drug_dosform

    @drug_dosform.setter
    def drug_dosform(self, value):
        self._drug_dosform = value
    @property
    def drug_pic_url(self):
        return self._drug_pic_url

    @drug_pic_url.setter
    def drug_pic_url(self, value):
        self._drug_pic_url = value
    @property
    def drug_type(self):
        return self._drug_type

    @drug_type.setter
    def drug_type(self, value):
        self._drug_type = value
    @property
    def drug_unit_desc(self):
        return self._drug_unit_desc

    @drug_unit_desc.setter
    def drug_unit_desc(self, value):
        self._drug_unit_desc = value
    @property
    def ext_drug_code(self):
        return self._ext_drug_code

    @ext_drug_code.setter
    def ext_drug_code(self, value):
        self._ext_drug_code = value
    @property
    def ext_drug_name(self):
        return self._ext_drug_name

    @ext_drug_name.setter
    def ext_drug_name(self, value):
        self._ext_drug_name = value
    @property
    def generic_name(self):
        return self._generic_name

    @generic_name.setter
    def generic_name(self, value):
        self._generic_name = value
    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        self._spec = value
    @property
    def usage_dosage_desc(self):
        return self._usage_dosage_desc

    @usage_dosage_desc.setter
    def usage_dosage_desc(self, value):
        self._usage_dosage_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.diagnosis:
            if hasattr(self.diagnosis, 'to_alipay_dict'):
                params['diagnosis'] = self.diagnosis.to_alipay_dict()
            else:
                params['diagnosis'] = self.diagnosis
        if self.drug_cnt:
            if hasattr(self.drug_cnt, 'to_alipay_dict'):
                params['drug_cnt'] = self.drug_cnt.to_alipay_dict()
            else:
                params['drug_cnt'] = self.drug_cnt
        if self.drug_dosform:
            if hasattr(self.drug_dosform, 'to_alipay_dict'):
                params['drug_dosform'] = self.drug_dosform.to_alipay_dict()
            else:
                params['drug_dosform'] = self.drug_dosform
        if self.drug_pic_url:
            if hasattr(self.drug_pic_url, 'to_alipay_dict'):
                params['drug_pic_url'] = self.drug_pic_url.to_alipay_dict()
            else:
                params['drug_pic_url'] = self.drug_pic_url
        if self.drug_type:
            if hasattr(self.drug_type, 'to_alipay_dict'):
                params['drug_type'] = self.drug_type.to_alipay_dict()
            else:
                params['drug_type'] = self.drug_type
        if self.drug_unit_desc:
            if hasattr(self.drug_unit_desc, 'to_alipay_dict'):
                params['drug_unit_desc'] = self.drug_unit_desc.to_alipay_dict()
            else:
                params['drug_unit_desc'] = self.drug_unit_desc
        if self.ext_drug_code:
            if hasattr(self.ext_drug_code, 'to_alipay_dict'):
                params['ext_drug_code'] = self.ext_drug_code.to_alipay_dict()
            else:
                params['ext_drug_code'] = self.ext_drug_code
        if self.ext_drug_name:
            if hasattr(self.ext_drug_name, 'to_alipay_dict'):
                params['ext_drug_name'] = self.ext_drug_name.to_alipay_dict()
            else:
                params['ext_drug_name'] = self.ext_drug_name
        if self.generic_name:
            if hasattr(self.generic_name, 'to_alipay_dict'):
                params['generic_name'] = self.generic_name.to_alipay_dict()
            else:
                params['generic_name'] = self.generic_name
        if self.spec:
            if hasattr(self.spec, 'to_alipay_dict'):
                params['spec'] = self.spec.to_alipay_dict()
            else:
                params['spec'] = self.spec
        if self.usage_dosage_desc:
            if hasattr(self.usage_dosage_desc, 'to_alipay_dict'):
                params['usage_dosage_desc'] = self.usage_dosage_desc.to_alipay_dict()
            else:
                params['usage_dosage_desc'] = self.usage_dosage_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrugInfo()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'diagnosis' in d:
            o.diagnosis = d['diagnosis']
        if 'drug_cnt' in d:
            o.drug_cnt = d['drug_cnt']
        if 'drug_dosform' in d:
            o.drug_dosform = d['drug_dosform']
        if 'drug_pic_url' in d:
            o.drug_pic_url = d['drug_pic_url']
        if 'drug_type' in d:
            o.drug_type = d['drug_type']
        if 'drug_unit_desc' in d:
            o.drug_unit_desc = d['drug_unit_desc']
        if 'ext_drug_code' in d:
            o.ext_drug_code = d['ext_drug_code']
        if 'ext_drug_name' in d:
            o.ext_drug_name = d['ext_drug_name']
        if 'generic_name' in d:
            o.generic_name = d['generic_name']
        if 'spec' in d:
            o.spec = d['spec']
        if 'usage_dosage_desc' in d:
            o.usage_dosage_desc = d['usage_dosage_desc']
        return o


