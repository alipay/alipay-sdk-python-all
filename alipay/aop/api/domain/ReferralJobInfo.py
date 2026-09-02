#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReferralJobInfo(object):

    def __init__(self):
        self._academic_require = None
        self._address = None
        self._address_name = None
        self._age = None
        self._distance = None
        self._distance_display = None
        self._expire_date = None
        self._geo = None
        self._job_desc = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._pay_date = None
        self._pay_period = None
        self._platform_name = None
        self._recruitment_count = None
        self._salary = None
        self._salary_unit = None
        self._station_name = None
        self._work_nature = None

    @property
    def academic_require(self):
        return self._academic_require

    @academic_require.setter
    def academic_require(self, value):
        self._academic_require = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def address_name(self):
        return self._address_name

    @address_name.setter
    def address_name(self, value):
        self._address_name = value
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def distance_display(self):
        return self._distance_display

    @distance_display.setter
    def distance_display(self, value):
        self._distance_display = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def geo(self):
        return self._geo

    @geo.setter
    def geo(self, value):
        self._geo = value
    @property
    def job_desc(self):
        return self._job_desc

    @job_desc.setter
    def job_desc(self, value):
        self._job_desc = value
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
    def pay_date(self):
        return self._pay_date

    @pay_date.setter
    def pay_date(self, value):
        self._pay_date = value
    @property
    def pay_period(self):
        return self._pay_period

    @pay_period.setter
    def pay_period(self, value):
        self._pay_period = value
    @property
    def platform_name(self):
        return self._platform_name

    @platform_name.setter
    def platform_name(self, value):
        self._platform_name = value
    @property
    def recruitment_count(self):
        return self._recruitment_count

    @recruitment_count.setter
    def recruitment_count(self, value):
        self._recruitment_count = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def salary_unit(self):
        return self._salary_unit

    @salary_unit.setter
    def salary_unit(self, value):
        self._salary_unit = value
    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, value):
        self._station_name = value
    @property
    def work_nature(self):
        return self._work_nature

    @work_nature.setter
    def work_nature(self, value):
        self._work_nature = value


    def to_alipay_dict(self):
        params = dict()
        if self.academic_require:
            if hasattr(self.academic_require, 'to_alipay_dict'):
                params['academic_require'] = self.academic_require.to_alipay_dict()
            else:
                params['academic_require'] = self.academic_require
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.address_name:
            if hasattr(self.address_name, 'to_alipay_dict'):
                params['address_name'] = self.address_name.to_alipay_dict()
            else:
                params['address_name'] = self.address_name
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.distance_display:
            if hasattr(self.distance_display, 'to_alipay_dict'):
                params['distance_display'] = self.distance_display.to_alipay_dict()
            else:
                params['distance_display'] = self.distance_display
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.geo:
            if hasattr(self.geo, 'to_alipay_dict'):
                params['geo'] = self.geo.to_alipay_dict()
            else:
                params['geo'] = self.geo
        if self.job_desc:
            if hasattr(self.job_desc, 'to_alipay_dict'):
                params['job_desc'] = self.job_desc.to_alipay_dict()
            else:
                params['job_desc'] = self.job_desc
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
        if self.pay_date:
            if hasattr(self.pay_date, 'to_alipay_dict'):
                params['pay_date'] = self.pay_date.to_alipay_dict()
            else:
                params['pay_date'] = self.pay_date
        if self.pay_period:
            if hasattr(self.pay_period, 'to_alipay_dict'):
                params['pay_period'] = self.pay_period.to_alipay_dict()
            else:
                params['pay_period'] = self.pay_period
        if self.platform_name:
            if hasattr(self.platform_name, 'to_alipay_dict'):
                params['platform_name'] = self.platform_name.to_alipay_dict()
            else:
                params['platform_name'] = self.platform_name
        if self.recruitment_count:
            if hasattr(self.recruitment_count, 'to_alipay_dict'):
                params['recruitment_count'] = self.recruitment_count.to_alipay_dict()
            else:
                params['recruitment_count'] = self.recruitment_count
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.salary_unit:
            if hasattr(self.salary_unit, 'to_alipay_dict'):
                params['salary_unit'] = self.salary_unit.to_alipay_dict()
            else:
                params['salary_unit'] = self.salary_unit
        if self.station_name:
            if hasattr(self.station_name, 'to_alipay_dict'):
                params['station_name'] = self.station_name.to_alipay_dict()
            else:
                params['station_name'] = self.station_name
        if self.work_nature:
            if hasattr(self.work_nature, 'to_alipay_dict'):
                params['work_nature'] = self.work_nature.to_alipay_dict()
            else:
                params['work_nature'] = self.work_nature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReferralJobInfo()
        if 'academic_require' in d:
            o.academic_require = d['academic_require']
        if 'address' in d:
            o.address = d['address']
        if 'address_name' in d:
            o.address_name = d['address_name']
        if 'age' in d:
            o.age = d['age']
        if 'distance' in d:
            o.distance = d['distance']
        if 'distance_display' in d:
            o.distance_display = d['distance_display']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'geo' in d:
            o.geo = d['geo']
        if 'job_desc' in d:
            o.job_desc = d['job_desc']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'pay_date' in d:
            o.pay_date = d['pay_date']
        if 'pay_period' in d:
            o.pay_period = d['pay_period']
        if 'platform_name' in d:
            o.platform_name = d['platform_name']
        if 'recruitment_count' in d:
            o.recruitment_count = d['recruitment_count']
        if 'salary' in d:
            o.salary = d['salary']
        if 'salary_unit' in d:
            o.salary_unit = d['salary_unit']
        if 'station_name' in d:
            o.station_name = d['station_name']
        if 'work_nature' in d:
            o.work_nature = d['work_nature']
        return o


