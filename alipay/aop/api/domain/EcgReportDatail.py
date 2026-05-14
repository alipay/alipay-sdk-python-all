#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcgReportDatail(object):

    def __init__(self):
        self._age = None
        self._check_result = None
        self._gender = None
        self._hospital_code = None
        self._hospital_name = None
        self._pic_type = None
        self._report_id = None
        self._report_name = None
        self._report_time = None
        self._report_type = None
        self._report_upload_time = None
        self._report_url = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def check_result(self):
        return self._check_result

    @check_result.setter
    def check_result(self, value):
        self._check_result = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hospital_code(self):
        return self._hospital_code

    @hospital_code.setter
    def hospital_code(self, value):
        self._hospital_code = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def pic_type(self):
        return self._pic_type

    @pic_type.setter
    def pic_type(self, value):
        self._pic_type = value
    @property
    def report_id(self):
        return self._report_id

    @report_id.setter
    def report_id(self, value):
        self._report_id = value
    @property
    def report_name(self):
        return self._report_name

    @report_name.setter
    def report_name(self, value):
        self._report_name = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def report_upload_time(self):
        return self._report_upload_time

    @report_upload_time.setter
    def report_upload_time(self, value):
        self._report_upload_time = value
    @property
    def report_url(self):
        return self._report_url

    @report_url.setter
    def report_url(self, value):
        self._report_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.check_result:
            if hasattr(self.check_result, 'to_alipay_dict'):
                params['check_result'] = self.check_result.to_alipay_dict()
            else:
                params['check_result'] = self.check_result
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hospital_code:
            if hasattr(self.hospital_code, 'to_alipay_dict'):
                params['hospital_code'] = self.hospital_code.to_alipay_dict()
            else:
                params['hospital_code'] = self.hospital_code
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.pic_type:
            if hasattr(self.pic_type, 'to_alipay_dict'):
                params['pic_type'] = self.pic_type.to_alipay_dict()
            else:
                params['pic_type'] = self.pic_type
        if self.report_id:
            if hasattr(self.report_id, 'to_alipay_dict'):
                params['report_id'] = self.report_id.to_alipay_dict()
            else:
                params['report_id'] = self.report_id
        if self.report_name:
            if hasattr(self.report_name, 'to_alipay_dict'):
                params['report_name'] = self.report_name.to_alipay_dict()
            else:
                params['report_name'] = self.report_name
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.report_upload_time:
            if hasattr(self.report_upload_time, 'to_alipay_dict'):
                params['report_upload_time'] = self.report_upload_time.to_alipay_dict()
            else:
                params['report_upload_time'] = self.report_upload_time
        if self.report_url:
            if hasattr(self.report_url, 'to_alipay_dict'):
                params['report_url'] = self.report_url.to_alipay_dict()
            else:
                params['report_url'] = self.report_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcgReportDatail()
        if 'age' in d:
            o.age = d['age']
        if 'check_result' in d:
            o.check_result = d['check_result']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hospital_code' in d:
            o.hospital_code = d['hospital_code']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'pic_type' in d:
            o.pic_type = d['pic_type']
        if 'report_id' in d:
            o.report_id = d['report_id']
        if 'report_name' in d:
            o.report_name = d['report_name']
        if 'report_time' in d:
            o.report_time = d['report_time']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'report_upload_time' in d:
            o.report_upload_time = d['report_upload_time']
        if 'report_url' in d:
            o.report_url = d['report_url']
        return o


