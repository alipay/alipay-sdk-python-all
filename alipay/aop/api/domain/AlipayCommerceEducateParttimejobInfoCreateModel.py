#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateParttimejobInfoCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._clearing_form = None
        self._company_logo = None
        self._company_name = None
        self._educational_requirements = None
        self._features = None
        self._gender_requirement = None
        self._heat = None
        self._height_limit = None
        self._industry_attributes = None
        self._is_famous = None
        self._job_address = None
        self._job_category = None
        self._job_frequency = None
        self._job_id = None
        self._job_name = None
        self._job_remark = None
        self._job_welfare = None
        self._need_health = None
        self._salary = None
        self._skip_url = None
        self._status = None
        self._working_date = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def clearing_form(self):
        return self._clearing_form

    @clearing_form.setter
    def clearing_form(self, value):
        self._clearing_form = value
    @property
    def company_logo(self):
        return self._company_logo

    @company_logo.setter
    def company_logo(self, value):
        self._company_logo = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def educational_requirements(self):
        return self._educational_requirements

    @educational_requirements.setter
    def educational_requirements(self, value):
        self._educational_requirements = value
    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        self._features = value
    @property
    def gender_requirement(self):
        return self._gender_requirement

    @gender_requirement.setter
    def gender_requirement(self, value):
        self._gender_requirement = value
    @property
    def heat(self):
        return self._heat

    @heat.setter
    def heat(self, value):
        self._heat = value
    @property
    def height_limit(self):
        return self._height_limit

    @height_limit.setter
    def height_limit(self, value):
        self._height_limit = value
    @property
    def industry_attributes(self):
        return self._industry_attributes

    @industry_attributes.setter
    def industry_attributes(self, value):
        self._industry_attributes = value
    @property
    def is_famous(self):
        return self._is_famous

    @is_famous.setter
    def is_famous(self, value):
        self._is_famous = value
    @property
    def job_address(self):
        return self._job_address

    @job_address.setter
    def job_address(self, value):
        self._job_address = value
    @property
    def job_category(self):
        return self._job_category

    @job_category.setter
    def job_category(self, value):
        self._job_category = value
    @property
    def job_frequency(self):
        return self._job_frequency

    @job_frequency.setter
    def job_frequency(self, value):
        self._job_frequency = value
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
    def job_remark(self):
        return self._job_remark

    @job_remark.setter
    def job_remark(self, value):
        self._job_remark = value
    @property
    def job_welfare(self):
        return self._job_welfare

    @job_welfare.setter
    def job_welfare(self, value):
        self._job_welfare = value
    @property
    def need_health(self):
        return self._need_health

    @need_health.setter
    def need_health(self, value):
        self._need_health = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def skip_url(self):
        return self._skip_url

    @skip_url.setter
    def skip_url(self, value):
        self._skip_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def working_date(self):
        return self._working_date

    @working_date.setter
    def working_date(self, value):
        self._working_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.clearing_form:
            if hasattr(self.clearing_form, 'to_alipay_dict'):
                params['clearing_form'] = self.clearing_form.to_alipay_dict()
            else:
                params['clearing_form'] = self.clearing_form
        if self.company_logo:
            if hasattr(self.company_logo, 'to_alipay_dict'):
                params['company_logo'] = self.company_logo.to_alipay_dict()
            else:
                params['company_logo'] = self.company_logo
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.educational_requirements:
            if hasattr(self.educational_requirements, 'to_alipay_dict'):
                params['educational_requirements'] = self.educational_requirements.to_alipay_dict()
            else:
                params['educational_requirements'] = self.educational_requirements
        if self.features:
            if hasattr(self.features, 'to_alipay_dict'):
                params['features'] = self.features.to_alipay_dict()
            else:
                params['features'] = self.features
        if self.gender_requirement:
            if hasattr(self.gender_requirement, 'to_alipay_dict'):
                params['gender_requirement'] = self.gender_requirement.to_alipay_dict()
            else:
                params['gender_requirement'] = self.gender_requirement
        if self.heat:
            if hasattr(self.heat, 'to_alipay_dict'):
                params['heat'] = self.heat.to_alipay_dict()
            else:
                params['heat'] = self.heat
        if self.height_limit:
            if hasattr(self.height_limit, 'to_alipay_dict'):
                params['height_limit'] = self.height_limit.to_alipay_dict()
            else:
                params['height_limit'] = self.height_limit
        if self.industry_attributes:
            if hasattr(self.industry_attributes, 'to_alipay_dict'):
                params['industry_attributes'] = self.industry_attributes.to_alipay_dict()
            else:
                params['industry_attributes'] = self.industry_attributes
        if self.is_famous:
            if hasattr(self.is_famous, 'to_alipay_dict'):
                params['is_famous'] = self.is_famous.to_alipay_dict()
            else:
                params['is_famous'] = self.is_famous
        if self.job_address:
            if hasattr(self.job_address, 'to_alipay_dict'):
                params['job_address'] = self.job_address.to_alipay_dict()
            else:
                params['job_address'] = self.job_address
        if self.job_category:
            if hasattr(self.job_category, 'to_alipay_dict'):
                params['job_category'] = self.job_category.to_alipay_dict()
            else:
                params['job_category'] = self.job_category
        if self.job_frequency:
            if hasattr(self.job_frequency, 'to_alipay_dict'):
                params['job_frequency'] = self.job_frequency.to_alipay_dict()
            else:
                params['job_frequency'] = self.job_frequency
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
        if self.job_remark:
            if hasattr(self.job_remark, 'to_alipay_dict'):
                params['job_remark'] = self.job_remark.to_alipay_dict()
            else:
                params['job_remark'] = self.job_remark
        if self.job_welfare:
            if hasattr(self.job_welfare, 'to_alipay_dict'):
                params['job_welfare'] = self.job_welfare.to_alipay_dict()
            else:
                params['job_welfare'] = self.job_welfare
        if self.need_health:
            if hasattr(self.need_health, 'to_alipay_dict'):
                params['need_health'] = self.need_health.to_alipay_dict()
            else:
                params['need_health'] = self.need_health
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.skip_url:
            if hasattr(self.skip_url, 'to_alipay_dict'):
                params['skip_url'] = self.skip_url.to_alipay_dict()
            else:
                params['skip_url'] = self.skip_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.working_date:
            if hasattr(self.working_date, 'to_alipay_dict'):
                params['working_date'] = self.working_date.to_alipay_dict()
            else:
                params['working_date'] = self.working_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateParttimejobInfoCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'clearing_form' in d:
            o.clearing_form = d['clearing_form']
        if 'company_logo' in d:
            o.company_logo = d['company_logo']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'educational_requirements' in d:
            o.educational_requirements = d['educational_requirements']
        if 'features' in d:
            o.features = d['features']
        if 'gender_requirement' in d:
            o.gender_requirement = d['gender_requirement']
        if 'heat' in d:
            o.heat = d['heat']
        if 'height_limit' in d:
            o.height_limit = d['height_limit']
        if 'industry_attributes' in d:
            o.industry_attributes = d['industry_attributes']
        if 'is_famous' in d:
            o.is_famous = d['is_famous']
        if 'job_address' in d:
            o.job_address = d['job_address']
        if 'job_category' in d:
            o.job_category = d['job_category']
        if 'job_frequency' in d:
            o.job_frequency = d['job_frequency']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_remark' in d:
            o.job_remark = d['job_remark']
        if 'job_welfare' in d:
            o.job_welfare = d['job_welfare']
        if 'need_health' in d:
            o.need_health = d['need_health']
        if 'salary' in d:
            o.salary = d['salary']
        if 'skip_url' in d:
            o.skip_url = d['skip_url']
        if 'status' in d:
            o.status = d['status']
        if 'working_date' in d:
            o.working_date = d['working_date']
        return o


