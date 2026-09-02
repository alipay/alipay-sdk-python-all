#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinRegistrationMortgageInfo(object):

    def __init__(self):
        self._mortgage_registration_date = None
        self._mortgage_release_date = None
        self._mortgagee_name = None

    @property
    def mortgage_registration_date(self):
        return self._mortgage_registration_date

    @mortgage_registration_date.setter
    def mortgage_registration_date(self, value):
        self._mortgage_registration_date = value
    @property
    def mortgage_release_date(self):
        return self._mortgage_release_date

    @mortgage_release_date.setter
    def mortgage_release_date(self, value):
        self._mortgage_release_date = value
    @property
    def mortgagee_name(self):
        return self._mortgagee_name

    @mortgagee_name.setter
    def mortgagee_name(self, value):
        self._mortgagee_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.mortgage_registration_date:
            if hasattr(self.mortgage_registration_date, 'to_alipay_dict'):
                params['mortgage_registration_date'] = self.mortgage_registration_date.to_alipay_dict()
            else:
                params['mortgage_registration_date'] = self.mortgage_registration_date
        if self.mortgage_release_date:
            if hasattr(self.mortgage_release_date, 'to_alipay_dict'):
                params['mortgage_release_date'] = self.mortgage_release_date.to_alipay_dict()
            else:
                params['mortgage_release_date'] = self.mortgage_release_date
        if self.mortgagee_name:
            if hasattr(self.mortgagee_name, 'to_alipay_dict'):
                params['mortgagee_name'] = self.mortgagee_name.to_alipay_dict()
            else:
                params['mortgagee_name'] = self.mortgagee_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinRegistrationMortgageInfo()
        if 'mortgage_registration_date' in d:
            o.mortgage_registration_date = d['mortgage_registration_date']
        if 'mortgage_release_date' in d:
            o.mortgage_release_date = d['mortgage_release_date']
        if 'mortgagee_name' in d:
            o.mortgagee_name = d['mortgagee_name']
        return o


