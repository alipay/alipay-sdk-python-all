#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndrISVBeneficiaryDTO(object):

    def __init__(self):
        self._beneficiary_id = None
        self._beneficiary_name = None
        self._country = None

    @property
    def beneficiary_id(self):
        return self._beneficiary_id

    @beneficiary_id.setter
    def beneficiary_id(self, value):
        self._beneficiary_id = value
    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self._beneficiary_name = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_id:
            if hasattr(self.beneficiary_id, 'to_alipay_dict'):
                params['beneficiary_id'] = self.beneficiary_id.to_alipay_dict()
            else:
                params['beneficiary_id'] = self.beneficiary_id
        if self.beneficiary_name:
            if hasattr(self.beneficiary_name, 'to_alipay_dict'):
                params['beneficiary_name'] = self.beneficiary_name.to_alipay_dict()
            else:
                params['beneficiary_name'] = self.beneficiary_name
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndrISVBeneficiaryDTO()
        if 'beneficiary_id' in d:
            o.beneficiary_id = d['beneficiary_id']
        if 'beneficiary_name' in d:
            o.beneficiary_name = d['beneficiary_name']
        if 'country' in d:
            o.country = d['country']
        return o


