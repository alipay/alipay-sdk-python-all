#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrganizationJobInfo(object):

    def __init__(self):
        self._academic_require = None
        self._age = None
        self._brand_logo = None
        self._brand_name = None
        self._city_code = None
        self._count = None
        self._employer_cert_no = None
        self._employer_name = None
        self._geo = None
        self._job_detail_url = None
        self._job_features = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._job_type_name = None
        self._partner_name = None
        self._pay_period = None
        self._salary = None
        self._work_nature = None
        self._working_years = None

    @property
    def academic_require(self):
        return self._academic_require

    @academic_require.setter
    def academic_require(self, value):
        self._academic_require = value
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def employer_cert_no(self):
        return self._employer_cert_no

    @employer_cert_no.setter
    def employer_cert_no(self, value):
        self._employer_cert_no = value
    @property
    def employer_name(self):
        return self._employer_name

    @employer_name.setter
    def employer_name(self, value):
        self._employer_name = value
    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value
    @property
    def job_detail_url(self):
        return self._job_detail_url

    @job_detail_url.setter
    def job_detail_url(self, value):
        self._job_detail_url = value
    @property
    def job_features(self):
        return self._job_features

    @job_features.setter
    def job_features(self, value):
        if isinstance(value, list):
            self._job_features = list()
            for i in value:
                self._job_features.append(i)
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def job_type_name(self):
        return self._job_type_name

    @job_type_name.setter
    def job_type_name(self, value):
        self._job_type_name = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def pay_period(self):
        return self._pay_period

    @pay_period.setter
    def pay_period(self, value):
        self._pay_period = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def work_nature(self):
        return self._work_nature

    @work_nature.setter
    def work_nature(self, value):
        self._work_nature = value
    @property
    def working_years(self):
        return self._working_years

    @working_years.setter
    def working_years(self, value):
        self._working_years = value


    def to_alipay_dict(self):
        params = dict()
        if self.academic_require:
            if hasattr(self.academic_require, 'to_alipay_dict'):
                params['academic_require'] = self.academic_require.to_alipay_dict()
            else:
                params['academic_require'] = self.academic_require
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.employer_cert_no:
            if hasattr(self.employer_cert_no, 'to_alipay_dict'):
                params['employer_cert_no'] = self.employer_cert_no.to_alipay_dict()
            else:
                params['employer_cert_no'] = self.employer_cert_no
        if self.employer_name:
            if hasattr(self.employer_name, 'to_alipay_dict'):
                params['employer_name'] = self.employer_name.to_alipay_dict()
            else:
                params['employer_name'] = self.employer_name
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        if self.job_detail_url:
            if hasattr(self.job_detail_url, 'to_alipay_dict'):
                params['job_detail_url'] = self.job_detail_url.to_alipay_dict()
            else:
                params['job_detail_url'] = self.job_detail_url
        if self.job_features:
            if isinstance(self.job_features, list):
                for i in range(0, len(self.job_features)):
                    element = self.job_features[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_features[i] = element.to_alipay_dict()
            if hasattr(self.job_features, 'to_alipay_dict'):
                params['job_features'] = self.job_features.to_alipay_dict()
            else:
                params['job_features'] = self.job_features
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.job_type_name:
            if hasattr(self.job_type_name, 'to_alipay_dict'):
                params['job_type_name'] = self.job_type_name.to_alipay_dict()
            else:
                params['job_type_name'] = self.job_type_name
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.pay_period:
            if hasattr(self.pay_period, 'to_alipay_dict'):
                params['pay_period'] = self.pay_period.to_alipay_dict()
            else:
                params['pay_period'] = self.pay_period
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.work_nature:
            if hasattr(self.work_nature, 'to_alipay_dict'):
                params['work_nature'] = self.work_nature.to_alipay_dict()
            else:
                params['work_nature'] = self.work_nature
        if self.working_years:
            if hasattr(self.working_years, 'to_alipay_dict'):
                params['working_years'] = self.working_years.to_alipay_dict()
            else:
                params['working_years'] = self.working_years
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrganizationJobInfo()
        if 'academic_require' in d:
            o.academic_require = d['academic_require']
        if 'age' in d:
            o.age = d['age']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'count' in d:
            o.count = d['count']
        if 'employer_cert_no' in d:
            o.employer_cert_no = d['employer_cert_no']
        if 'employer_name' in d:
            o.employer_name = d['employer_name']
        if 'geo' in d:
            o.geo = d['geo']
        if 'job_detail_url' in d:
            o.job_detail_url = d['job_detail_url']
        if 'job_features' in d:
            o.job_features = d['job_features']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'job_type_name' in d:
            o.job_type_name = d['job_type_name']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'pay_period' in d:
            o.pay_period = d['pay_period']
        if 'salary' in d:
            o.salary = d['salary']
        if 'work_nature' in d:
            o.work_nature = d['work_nature']
        if 'working_years' in d:
            o.working_years = d['working_years']
        return o


