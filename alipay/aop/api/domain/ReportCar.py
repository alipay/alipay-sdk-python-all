#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Person import Person
from alipay.aop.api.domain.Person import Person
from alipay.aop.api.domain.Person import Person


class ReportCar(object):

    def __init__(self):
        self._assessor = None
        self._driver = None
        self._frame_no = None
        self._garage_address = None
        self._garage_name = None
        self._garage_phone_no = None
        self._garage_type = None
        self._license_no = None
        self._survey_first_commit_date = None
        self._survey_last_commit_date = None
        self._surveyor = None

    @property
    def assessor(self):
        return self._assessor

    @assessor.setter
    def assessor(self, value):
        if isinstance(value, Person):
            self._assessor = value
        else:
            self._assessor = Person.from_alipay_dict(value)
    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        if isinstance(value, Person):
            self._driver = value
        else:
            self._driver = Person.from_alipay_dict(value)
    @property
    def frame_no(self):
        return self._frame_no

    @frame_no.setter
    def frame_no(self, value):
        self._frame_no = value
    @property
    def garage_address(self):
        return self._garage_address

    @garage_address.setter
    def garage_address(self, value):
        self._garage_address = value
    @property
    def garage_name(self):
        return self._garage_name

    @garage_name.setter
    def garage_name(self, value):
        self._garage_name = value
    @property
    def garage_phone_no(self):
        return self._garage_phone_no

    @garage_phone_no.setter
    def garage_phone_no(self, value):
        self._garage_phone_no = value
    @property
    def garage_type(self):
        return self._garage_type

    @garage_type.setter
    def garage_type(self, value):
        self._garage_type = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def survey_first_commit_date(self):
        return self._survey_first_commit_date

    @survey_first_commit_date.setter
    def survey_first_commit_date(self, value):
        self._survey_first_commit_date = value
    @property
    def survey_last_commit_date(self):
        return self._survey_last_commit_date

    @survey_last_commit_date.setter
    def survey_last_commit_date(self, value):
        self._survey_last_commit_date = value
    @property
    def surveyor(self):
        return self._surveyor

    @surveyor.setter
    def surveyor(self, value):
        if isinstance(value, Person):
            self._surveyor = value
        else:
            self._surveyor = Person.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.assessor:
            if hasattr(self.assessor, 'to_alipay_dict'):
                params['assessor'] = self.assessor.to_alipay_dict()
            else:
                params['assessor'] = self.assessor
        if self.driver:
            if hasattr(self.driver, 'to_alipay_dict'):
                params['driver'] = self.driver.to_alipay_dict()
            else:
                params['driver'] = self.driver
        if self.frame_no:
            if hasattr(self.frame_no, 'to_alipay_dict'):
                params['frame_no'] = self.frame_no.to_alipay_dict()
            else:
                params['frame_no'] = self.frame_no
        if self.garage_address:
            if hasattr(self.garage_address, 'to_alipay_dict'):
                params['garage_address'] = self.garage_address.to_alipay_dict()
            else:
                params['garage_address'] = self.garage_address
        if self.garage_name:
            if hasattr(self.garage_name, 'to_alipay_dict'):
                params['garage_name'] = self.garage_name.to_alipay_dict()
            else:
                params['garage_name'] = self.garage_name
        if self.garage_phone_no:
            if hasattr(self.garage_phone_no, 'to_alipay_dict'):
                params['garage_phone_no'] = self.garage_phone_no.to_alipay_dict()
            else:
                params['garage_phone_no'] = self.garage_phone_no
        if self.garage_type:
            if hasattr(self.garage_type, 'to_alipay_dict'):
                params['garage_type'] = self.garage_type.to_alipay_dict()
            else:
                params['garage_type'] = self.garage_type
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.survey_first_commit_date:
            if hasattr(self.survey_first_commit_date, 'to_alipay_dict'):
                params['survey_first_commit_date'] = self.survey_first_commit_date.to_alipay_dict()
            else:
                params['survey_first_commit_date'] = self.survey_first_commit_date
        if self.survey_last_commit_date:
            if hasattr(self.survey_last_commit_date, 'to_alipay_dict'):
                params['survey_last_commit_date'] = self.survey_last_commit_date.to_alipay_dict()
            else:
                params['survey_last_commit_date'] = self.survey_last_commit_date
        if self.surveyor:
            if hasattr(self.surveyor, 'to_alipay_dict'):
                params['surveyor'] = self.surveyor.to_alipay_dict()
            else:
                params['surveyor'] = self.surveyor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportCar()
        if 'assessor' in d:
            o.assessor = d['assessor']
        if 'driver' in d:
            o.driver = d['driver']
        if 'frame_no' in d:
            o.frame_no = d['frame_no']
        if 'garage_address' in d:
            o.garage_address = d['garage_address']
        if 'garage_name' in d:
            o.garage_name = d['garage_name']
        if 'garage_phone_no' in d:
            o.garage_phone_no = d['garage_phone_no']
        if 'garage_type' in d:
            o.garage_type = d['garage_type']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'survey_first_commit_date' in d:
            o.survey_first_commit_date = d['survey_first_commit_date']
        if 'survey_last_commit_date' in d:
            o.survey_last_commit_date = d['survey_last_commit_date']
        if 'surveyor' in d:
            o.surveyor = d['surveyor']
        return o


