#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAuthContent(object):

    def __init__(self):
        self._credit_level = None
        self._ep_auth_no = None
        self._ep_cert_no = None
        self._ep_name = None
        self._legal_person_cert_no = None
        self._legal_person_name = None

    @property
    def credit_level(self):
        return self._credit_level

    @credit_level.setter
    def credit_level(self, value):
        self._credit_level = value
    @property
    def ep_auth_no(self):
        return self._ep_auth_no

    @ep_auth_no.setter
    def ep_auth_no(self, value):
        self._ep_auth_no = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_name(self):
        return self._legal_person_name

    @legal_person_name.setter
    def legal_person_name(self, value):
        self._legal_person_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_level:
            if hasattr(self.credit_level, 'to_alipay_dict'):
                params['credit_level'] = self.credit_level.to_alipay_dict()
            else:
                params['credit_level'] = self.credit_level
        if self.ep_auth_no:
            if hasattr(self.ep_auth_no, 'to_alipay_dict'):
                params['ep_auth_no'] = self.ep_auth_no.to_alipay_dict()
            else:
                params['ep_auth_no'] = self.ep_auth_no
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_name:
            if hasattr(self.legal_person_name, 'to_alipay_dict'):
                params['legal_person_name'] = self.legal_person_name.to_alipay_dict()
            else:
                params['legal_person_name'] = self.legal_person_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAuthContent()
        if 'credit_level' in d:
            o.credit_level = d['credit_level']
        if 'ep_auth_no' in d:
            o.ep_auth_no = d['ep_auth_no']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_name' in d:
            o.legal_person_name = d['legal_person_name']
        return o


