#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpOweTaxInfo(object):

    def __init__(self):
        self._identify_number = None
        self._issue_date = None
        self._legal_person_name = None
        self._manage_address = None
        self._money = None
        self._name = None
        self._notice_type = None
        self._taxes_organ = None
        self._taxes_type = None

    @property
    def identify_number(self):
        return self._identify_number

    @identify_number.setter
    def identify_number(self, value):
        self._identify_number = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value
    @property
    def manage_address(self):
        return self._manage_address

    @manage_address.setter
    def manage_address(self, value):
        self._manage_address = value
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def notice_type(self):
        return self._notice_type

    @notice_type.setter
    def notice_type(self, value):
        self._notice_type = value
    @property
    def taxes_organ(self):
        return self._taxes_organ

    @taxes_organ.setter
    def taxes_organ(self, value):
        self._taxes_organ = value
    @property
    def taxes_type(self):
        return self._taxes_type

    @taxes_type.setter
    def taxes_type(self, value):
        self._taxes_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identify_number:
            if hasattr(self.identify_number, 'to_alipay_dict'):
                params['identify_number'] = self.identify_number.to_alipay_dict()
            else:
                params['identify_number'] = self.identify_number
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        if self.manage_address:
            if hasattr(self.manage_address, 'to_alipay_dict'):
                params['manage_address'] = self.manage_address.to_alipay_dict()
            else:
                params['manage_address'] = self.manage_address
        if self.money:
            if hasattr(self.money, 'to_alipay_dict'):
                params['money'] = self.money.to_alipay_dict()
            else:
                params['money'] = self.money
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.notice_type:
            if hasattr(self.notice_type, 'to_alipay_dict'):
                params['notice_type'] = self.notice_type.to_alipay_dict()
            else:
                params['notice_type'] = self.notice_type
        if self.taxes_organ:
            if hasattr(self.taxes_organ, 'to_alipay_dict'):
                params['taxes_organ'] = self.taxes_organ.to_alipay_dict()
            else:
                params['taxes_organ'] = self.taxes_organ
        if self.taxes_type:
            if hasattr(self.taxes_type, 'to_alipay_dict'):
                params['taxes_type'] = self.taxes_type.to_alipay_dict()
            else:
                params['taxes_type'] = self.taxes_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpOweTaxInfo()
        if 'identify_number' in d:
            o.identify_number = d['identify_number']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        if 'manage_address' in d:
            o.manage_address = d['manage_address']
        if 'money' in d:
            o.money = d['money']
        if 'name' in d:
            o.name = d['name']
        if 'notice_type' in d:
            o.notice_type = d['notice_type']
        if 'taxes_organ' in d:
            o.taxes_organ = d['taxes_organ']
        if 'taxes_type' in d:
            o.taxes_type = d['taxes_type']
        return o


