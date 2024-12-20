#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalInsuredCityList import MedicalInsuredCityList


class MedicalCardInfoList(object):

    def __init__(self):
        self._family_medical_card_id = None
        self._family_user_id = None
        self._insured_cities = None
        self._insured_status = None
        self._medical_card_id = None
        self._status = None

    @property
    def family_medical_card_id(self):
        return self._family_medical_card_id

    @family_medical_card_id.setter
    def family_medical_card_id(self, value):
        self._family_medical_card_id = value
    @property
    def family_user_id(self):
        return self._family_user_id

    @family_user_id.setter
    def family_user_id(self, value):
        self._family_user_id = value
    @property
    def insured_cities(self):
        return self._insured_cities

    @insured_cities.setter
    def insured_cities(self, value):
        if isinstance(value, MedicalInsuredCityList):
            self._insured_cities = value
        else:
            self._insured_cities = MedicalInsuredCityList.from_alipay_dict(value)
    @property
    def insured_status(self):
        return self._insured_status

    @insured_status.setter
    def insured_status(self, value):
        self._insured_status = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.family_medical_card_id:
            if hasattr(self.family_medical_card_id, 'to_alipay_dict'):
                params['family_medical_card_id'] = self.family_medical_card_id.to_alipay_dict()
            else:
                params['family_medical_card_id'] = self.family_medical_card_id
        if self.family_user_id:
            if hasattr(self.family_user_id, 'to_alipay_dict'):
                params['family_user_id'] = self.family_user_id.to_alipay_dict()
            else:
                params['family_user_id'] = self.family_user_id
        if self.insured_cities:
            if hasattr(self.insured_cities, 'to_alipay_dict'):
                params['insured_cities'] = self.insured_cities.to_alipay_dict()
            else:
                params['insured_cities'] = self.insured_cities
        if self.insured_status:
            if hasattr(self.insured_status, 'to_alipay_dict'):
                params['insured_status'] = self.insured_status.to_alipay_dict()
            else:
                params['insured_status'] = self.insured_status
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalCardInfoList()
        if 'family_medical_card_id' in d:
            o.family_medical_card_id = d['family_medical_card_id']
        if 'family_user_id' in d:
            o.family_user_id = d['family_user_id']
        if 'insured_cities' in d:
            o.insured_cities = d['insured_cities']
        if 'insured_status' in d:
            o.insured_status = d['insured_status']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'status' in d:
            o.status = d['status']
        return o


