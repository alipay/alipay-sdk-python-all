#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectContactPersonInfo(object):

    def __init__(self):
        self._contact_card_no = None
        self._contact_cert_type = None
        self._contact_name = None
        self._contact_phone_no = None

    @property
    def contact_card_no(self):
        return self._contact_card_no

    @contact_card_no.setter
    def contact_card_no(self, value):
        self._contact_card_no = value
    @property
    def contact_cert_type(self):
        return self._contact_cert_type

    @contact_cert_type.setter
    def contact_cert_type(self, value):
        self._contact_cert_type = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone_no(self):
        return self._contact_phone_no

    @contact_phone_no.setter
    def contact_phone_no(self, value):
        self._contact_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_card_no:
            if hasattr(self.contact_card_no, 'to_alipay_dict'):
                params['contact_card_no'] = self.contact_card_no.to_alipay_dict()
            else:
                params['contact_card_no'] = self.contact_card_no
        if self.contact_cert_type:
            if hasattr(self.contact_cert_type, 'to_alipay_dict'):
                params['contact_cert_type'] = self.contact_cert_type.to_alipay_dict()
            else:
                params['contact_cert_type'] = self.contact_cert_type
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone_no:
            if hasattr(self.contact_phone_no, 'to_alipay_dict'):
                params['contact_phone_no'] = self.contact_phone_no.to_alipay_dict()
            else:
                params['contact_phone_no'] = self.contact_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectContactPersonInfo()
        if 'contact_card_no' in d:
            o.contact_card_no = d['contact_card_no']
        if 'contact_cert_type' in d:
            o.contact_cert_type = d['contact_cert_type']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone_no' in d:
            o.contact_phone_no = d['contact_phone_no']
        return o


