#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OBCompanyDTO import OBCompanyDTO
from alipay.aop.api.domain.OBPersonalDTO import OBPersonalDTO


class OBBatchCustomerIdentityDTO(object):

    def __init__(self):
        self._company = None
        self._passport_id = None
        self._personal = None

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        if isinstance(value, OBCompanyDTO):
            self._company = value
        else:
            self._company = OBCompanyDTO.from_alipay_dict(value)
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def personal(self):
        return self._personal

    @personal.setter
    def personal(self, value):
        if isinstance(value, OBPersonalDTO):
            self._personal = value
        else:
            self._personal = OBPersonalDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.personal:
            if hasattr(self.personal, 'to_alipay_dict'):
                params['personal'] = self.personal.to_alipay_dict()
            else:
                params['personal'] = self.personal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OBBatchCustomerIdentityDTO()
        if 'company' in d:
            o.company = d['company']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'personal' in d:
            o.personal = d['personal']
        return o


