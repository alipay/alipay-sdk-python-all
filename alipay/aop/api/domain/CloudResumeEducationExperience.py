#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumeEducationExperience(object):

    def __init__(self):
        self._degree = None
        self._education_status = None
        self._finish_school_month = None
        self._finish_school_year = None
        self._in_school_month = None
        self._in_school_year = None
        self._location = None
        self._major = None
        self._month = None
        self._school_name = None
        self._tong_zhao = None
        self._year = None

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def education_status(self):
        return self._education_status

    @education_status.setter
    def education_status(self, value):
        self._education_status = value
    @property
    def finish_school_month(self):
        return self._finish_school_month

    @finish_school_month.setter
    def finish_school_month(self, value):
        self._finish_school_month = value
    @property
    def finish_school_year(self):
        return self._finish_school_year

    @finish_school_year.setter
    def finish_school_year(self, value):
        self._finish_school_year = value
    @property
    def in_school_month(self):
        return self._in_school_month

    @in_school_month.setter
    def in_school_month(self, value):
        self._in_school_month = value
    @property
    def in_school_year(self):
        return self._in_school_year

    @in_school_year.setter
    def in_school_year(self, value):
        self._in_school_year = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def tong_zhao(self):
        return self._tong_zhao

    @tong_zhao.setter
    def tong_zhao(self, value):
        self._tong_zhao = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.degree:
            if hasattr(self.degree, 'to_alipay_dict'):
                params['degree'] = self.degree.to_alipay_dict()
            else:
                params['degree'] = self.degree
        if self.education_status:
            if hasattr(self.education_status, 'to_alipay_dict'):
                params['education_status'] = self.education_status.to_alipay_dict()
            else:
                params['education_status'] = self.education_status
        if self.finish_school_month:
            if hasattr(self.finish_school_month, 'to_alipay_dict'):
                params['finish_school_month'] = self.finish_school_month.to_alipay_dict()
            else:
                params['finish_school_month'] = self.finish_school_month
        if self.finish_school_year:
            if hasattr(self.finish_school_year, 'to_alipay_dict'):
                params['finish_school_year'] = self.finish_school_year.to_alipay_dict()
            else:
                params['finish_school_year'] = self.finish_school_year
        if self.in_school_month:
            if hasattr(self.in_school_month, 'to_alipay_dict'):
                params['in_school_month'] = self.in_school_month.to_alipay_dict()
            else:
                params['in_school_month'] = self.in_school_month
        if self.in_school_year:
            if hasattr(self.in_school_year, 'to_alipay_dict'):
                params['in_school_year'] = self.in_school_year.to_alipay_dict()
            else:
                params['in_school_year'] = self.in_school_year
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.major:
            if hasattr(self.major, 'to_alipay_dict'):
                params['major'] = self.major.to_alipay_dict()
            else:
                params['major'] = self.major
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.tong_zhao:
            if hasattr(self.tong_zhao, 'to_alipay_dict'):
                params['tong_zhao'] = self.tong_zhao.to_alipay_dict()
            else:
                params['tong_zhao'] = self.tong_zhao
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumeEducationExperience()
        if 'degree' in d:
            o.degree = d['degree']
        if 'education_status' in d:
            o.education_status = d['education_status']
        if 'finish_school_month' in d:
            o.finish_school_month = d['finish_school_month']
        if 'finish_school_year' in d:
            o.finish_school_year = d['finish_school_year']
        if 'in_school_month' in d:
            o.in_school_month = d['in_school_month']
        if 'in_school_year' in d:
            o.in_school_year = d['in_school_year']
        if 'location' in d:
            o.location = d['location']
        if 'major' in d:
            o.major = d['major']
        if 'month' in d:
            o.month = d['month']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'tong_zhao' in d:
            o.tong_zhao = d['tong_zhao']
        if 'year' in d:
            o.year = d['year']
        return o


