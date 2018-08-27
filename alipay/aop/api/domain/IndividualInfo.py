#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndividualInfo(object):

    def __init__(self):
        self._date_of_birth = None
        self._id_number = None
        self._name = None
        self._nationality = None
        self._residential_address = None
        self._type = None

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def residential_address(self):
        return self._residential_address

    @residential_address.setter
    def residential_address(self, value):
        self._residential_address = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.date_of_birth:
            if hasattr(self.date_of_birth, 'to_alipay_dict'):
                params['date_of_birth'] = self.date_of_birth.to_alipay_dict()
            else:
                params['date_of_birth'] = self.date_of_birth
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.nationality:
            if hasattr(self.nationality, 'to_alipay_dict'):
                params['nationality'] = self.nationality.to_alipay_dict()
            else:
                params['nationality'] = self.nationality
        if self.residential_address:
            if hasattr(self.residential_address, 'to_alipay_dict'):
                params['residential_address'] = self.residential_address.to_alipay_dict()
            else:
                params['residential_address'] = self.residential_address
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndividualInfo()
        if 'date_of_birth' in d:
            o.date_of_birth = d['date_of_birth']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'name' in d:
            o.name = d['name']
        if 'nationality' in d:
            o.nationality = d['nationality']
        if 'residential_address' in d:
            o.residential_address = d['residential_address']
        if 'type' in d:
            o.type = d['type']
        return o


