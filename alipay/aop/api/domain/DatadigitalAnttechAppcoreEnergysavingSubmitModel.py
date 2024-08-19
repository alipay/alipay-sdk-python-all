#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechAppcoreEnergysavingSubmitModel(object):

    def __init__(self):
        self._apply_date = None
        self._company_uscc = None
        self._heating_card_number = None
        self._open_id = None
        self._resident_id = None
        self._submit_type = None
        self._user_id = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def company_uscc(self):
        return self._company_uscc

    @company_uscc.setter
    def company_uscc(self, value):
        self._company_uscc = value
    @property
    def heating_card_number(self):
        return self._heating_card_number

    @heating_card_number.setter
    def heating_card_number(self, value):
        self._heating_card_number = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def resident_id(self):
        return self._resident_id

    @resident_id.setter
    def resident_id(self, value):
        self._resident_id = value
    @property
    def submit_type(self):
        return self._submit_type

    @submit_type.setter
    def submit_type(self, value):
        self._submit_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.company_uscc:
            if hasattr(self.company_uscc, 'to_alipay_dict'):
                params['company_uscc'] = self.company_uscc.to_alipay_dict()
            else:
                params['company_uscc'] = self.company_uscc
        if self.heating_card_number:
            if hasattr(self.heating_card_number, 'to_alipay_dict'):
                params['heating_card_number'] = self.heating_card_number.to_alipay_dict()
            else:
                params['heating_card_number'] = self.heating_card_number
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.resident_id:
            if hasattr(self.resident_id, 'to_alipay_dict'):
                params['resident_id'] = self.resident_id.to_alipay_dict()
            else:
                params['resident_id'] = self.resident_id
        if self.submit_type:
            if hasattr(self.submit_type, 'to_alipay_dict'):
                params['submit_type'] = self.submit_type.to_alipay_dict()
            else:
                params['submit_type'] = self.submit_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechAppcoreEnergysavingSubmitModel()
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'company_uscc' in d:
            o.company_uscc = d['company_uscc']
        if 'heating_card_number' in d:
            o.heating_card_number = d['heating_card_number']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'resident_id' in d:
            o.resident_id = d['resident_id']
        if 'submit_type' in d:
            o.submit_type = d['submit_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


