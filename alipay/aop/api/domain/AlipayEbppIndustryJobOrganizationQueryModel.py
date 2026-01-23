#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryJobOrganizationQueryModel(object):

    def __init__(self):
        self._academic_require = None
        self._cert_num = None
        self._city_code = None
        self._device_id = None
        self._device_id_type = None
        self._geo = None
        self._job_types = None
        self._mobile = None
        self._open_id = None
        self._page_num = None
        self._page_size = None
        self._salary_max = None
        self._salary_min = None
        self._search_word = None
        self._sort_type = None
        self._user_id = None
        self._work_nature = None
        self._working_years = None

    @property
    def academic_require(self):
        return self._academic_require

    @academic_require.setter
    def academic_require(self, value):
        self._academic_require = value
    @property
    def cert_num(self):
        return self._cert_num

    @cert_num.setter
    def cert_num(self, value):
        self._cert_num = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_id_type(self):
        return self._device_id_type

    @device_id_type.setter
    def device_id_type(self, value):
        self._device_id_type = value
    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value
    @property
    def job_types(self):
        return self._job_types

    @job_types.setter
    def job_types(self, value):
        if isinstance(value, list):
            self._job_types = list()
            for i in value:
                self._job_types.append(i)
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def salary_max(self):
        return self._salary_max

    @salary_max.setter
    def salary_max(self, value):
        self._salary_max = value
    @property
    def salary_min(self):
        return self._salary_min

    @salary_min.setter
    def salary_min(self, value):
        self._salary_min = value
    @property
    def search_word(self):
        return self._search_word

    @search_word.setter
    def search_word(self, value):
        self._search_word = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
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
        if self.cert_num:
            if hasattr(self.cert_num, 'to_alipay_dict'):
                params['cert_num'] = self.cert_num.to_alipay_dict()
            else:
                params['cert_num'] = self.cert_num
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_id_type:
            if hasattr(self.device_id_type, 'to_alipay_dict'):
                params['device_id_type'] = self.device_id_type.to_alipay_dict()
            else:
                params['device_id_type'] = self.device_id_type
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        if self.job_types:
            if isinstance(self.job_types, list):
                for i in range(0, len(self.job_types)):
                    element = self.job_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.job_types[i] = element.to_alipay_dict()
            if hasattr(self.job_types, 'to_alipay_dict'):
                params['job_types'] = self.job_types.to_alipay_dict()
            else:
                params['job_types'] = self.job_types
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.salary_max:
            if hasattr(self.salary_max, 'to_alipay_dict'):
                params['salary_max'] = self.salary_max.to_alipay_dict()
            else:
                params['salary_max'] = self.salary_max
        if self.salary_min:
            if hasattr(self.salary_min, 'to_alipay_dict'):
                params['salary_min'] = self.salary_min.to_alipay_dict()
            else:
                params['salary_min'] = self.salary_min
        if self.search_word:
            if hasattr(self.search_word, 'to_alipay_dict'):
                params['search_word'] = self.search_word.to_alipay_dict()
            else:
                params['search_word'] = self.search_word
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = AlipayEbppIndustryJobOrganizationQueryModel()
        if 'academic_require' in d:
            o.academic_require = d['academic_require']
        if 'cert_num' in d:
            o.cert_num = d['cert_num']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_id_type' in d:
            o.device_id_type = d['device_id_type']
        if 'geo' in d:
            o.geo = d['geo']
        if 'job_types' in d:
            o.job_types = d['job_types']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'salary_max' in d:
            o.salary_max = d['salary_max']
        if 'salary_min' in d:
            o.salary_min = d['salary_min']
        if 'search_word' in d:
            o.search_word = d['search_word']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'work_nature' in d:
            o.work_nature = d['work_nature']
        if 'working_years' in d:
            o.working_years = d['working_years']
        return o


