#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Workload(object):

    def __init__(self):
        self._city_code = None
        self._city_name = None
        self._job_code = None
        self._job_name = None
        self._level_code = None
        self._level_name = None
        self._months = None
        self._packages = None
        self._person_day = None
        self._persons = None
        self._price = None
        self._price_type = None
        self._project_code = None
        self._remark = None
        self._site_code = None
        self._site_name = None
        self._total_price = None
        self._work_efficiency = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def job_code(self):
        return self._job_code

    @job_code.setter
    def job_code(self, value):
        self._job_code = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, value):
        self._level_code = value
    @property
    def level_name(self):
        return self._level_name

    @level_name.setter
    def level_name(self, value):
        self._level_name = value
    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, value):
        self._months = value
    @property
    def packages(self):
        return self._packages

    @packages.setter
    def packages(self, value):
        self._packages = value
    @property
    def person_day(self):
        return self._person_day

    @person_day.setter
    def person_day(self, value):
        self._person_day = value
    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, value):
        self._persons = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def price_type(self):
        return self._price_type

    @price_type.setter
    def price_type(self, value):
        self._price_type = value
    @property
    def project_code(self):
        return self._project_code

    @project_code.setter
    def project_code(self, value):
        self._project_code = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def site_code(self):
        return self._site_code

    @site_code.setter
    def site_code(self, value):
        self._site_code = value
    @property
    def site_name(self):
        return self._site_name

    @site_name.setter
    def site_name(self, value):
        self._site_name = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value
    @property
    def work_efficiency(self):
        return self._work_efficiency

    @work_efficiency.setter
    def work_efficiency(self, value):
        self._work_efficiency = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.job_code:
            if hasattr(self.job_code, 'to_alipay_dict'):
                params['job_code'] = self.job_code.to_alipay_dict()
            else:
                params['job_code'] = self.job_code
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.level_code:
            if hasattr(self.level_code, 'to_alipay_dict'):
                params['level_code'] = self.level_code.to_alipay_dict()
            else:
                params['level_code'] = self.level_code
        if self.level_name:
            if hasattr(self.level_name, 'to_alipay_dict'):
                params['level_name'] = self.level_name.to_alipay_dict()
            else:
                params['level_name'] = self.level_name
        if self.months:
            if hasattr(self.months, 'to_alipay_dict'):
                params['months'] = self.months.to_alipay_dict()
            else:
                params['months'] = self.months
        if self.packages:
            if hasattr(self.packages, 'to_alipay_dict'):
                params['packages'] = self.packages.to_alipay_dict()
            else:
                params['packages'] = self.packages
        if self.person_day:
            if hasattr(self.person_day, 'to_alipay_dict'):
                params['person_day'] = self.person_day.to_alipay_dict()
            else:
                params['person_day'] = self.person_day
        if self.persons:
            if hasattr(self.persons, 'to_alipay_dict'):
                params['persons'] = self.persons.to_alipay_dict()
            else:
                params['persons'] = self.persons
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.price_type:
            if hasattr(self.price_type, 'to_alipay_dict'):
                params['price_type'] = self.price_type.to_alipay_dict()
            else:
                params['price_type'] = self.price_type
        if self.project_code:
            if hasattr(self.project_code, 'to_alipay_dict'):
                params['project_code'] = self.project_code.to_alipay_dict()
            else:
                params['project_code'] = self.project_code
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.site_code:
            if hasattr(self.site_code, 'to_alipay_dict'):
                params['site_code'] = self.site_code.to_alipay_dict()
            else:
                params['site_code'] = self.site_code
        if self.site_name:
            if hasattr(self.site_name, 'to_alipay_dict'):
                params['site_name'] = self.site_name.to_alipay_dict()
            else:
                params['site_name'] = self.site_name
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
        if self.work_efficiency:
            if hasattr(self.work_efficiency, 'to_alipay_dict'):
                params['work_efficiency'] = self.work_efficiency.to_alipay_dict()
            else:
                params['work_efficiency'] = self.work_efficiency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Workload()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'job_code' in d:
            o.job_code = d['job_code']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'level_code' in d:
            o.level_code = d['level_code']
        if 'level_name' in d:
            o.level_name = d['level_name']
        if 'months' in d:
            o.months = d['months']
        if 'packages' in d:
            o.packages = d['packages']
        if 'person_day' in d:
            o.person_day = d['person_day']
        if 'persons' in d:
            o.persons = d['persons']
        if 'price' in d:
            o.price = d['price']
        if 'price_type' in d:
            o.price_type = d['price_type']
        if 'project_code' in d:
            o.project_code = d['project_code']
        if 'remark' in d:
            o.remark = d['remark']
        if 'site_code' in d:
            o.site_code = d['site_code']
        if 'site_name' in d:
            o.site_name = d['site_name']
        if 'total_price' in d:
            o.total_price = d['total_price']
        if 'work_efficiency' in d:
            o.work_efficiency = d['work_efficiency']
        return o


