#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessParamDTO(object):

    def __init__(self):
        self._agreement_no = None
        self._contact_name = None
        self._contact_phone_number = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone_number(self):
        return self._contact_phone_number

    @contact_phone_number.setter
    def contact_phone_number(self, value):
        self._contact_phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone_number:
            if hasattr(self.contact_phone_number, 'to_alipay_dict'):
                params['contact_phone_number'] = self.contact_phone_number.to_alipay_dict()
            else:
                params['contact_phone_number'] = self.contact_phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessParamDTO()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        return o


