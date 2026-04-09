#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EscrowLicense(object):

    def __init__(self):
        self._cert_expired_date = None
        self._cert_mobile = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._legal_person_cert_expired_date = None
        self._legal_person_cert_no = None
        self._legal_person_cert_type = None
        self._legal_person_mobile = None
        self._legal_person_real_name = None
        self._license_address = None
        self._real_name = None

    @property
    def cert_expired_date(self):
        return self._cert_expired_date

    @cert_expired_date.setter
    def cert_expired_date(self, value):
        self._cert_expired_date = value
    @property
    def cert_mobile(self):
        return self._cert_mobile

    @cert_mobile.setter
    def cert_mobile(self, value):
        self._cert_mobile = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def legal_person_cert_expired_date(self):
        return self._legal_person_cert_expired_date

    @legal_person_cert_expired_date.setter
    def legal_person_cert_expired_date(self, value):
        self._legal_person_cert_expired_date = value
    @property
    def legal_person_cert_no(self):
        return self._legal_person_cert_no

    @legal_person_cert_no.setter
    def legal_person_cert_no(self, value):
        self._legal_person_cert_no = value
    @property
    def legal_person_cert_type(self):
        return self._legal_person_cert_type

    @legal_person_cert_type.setter
    def legal_person_cert_type(self, value):
        self._legal_person_cert_type = value
    @property
    def legal_person_mobile(self):
        return self._legal_person_mobile

    @legal_person_mobile.setter
    def legal_person_mobile(self, value):
        self._legal_person_mobile = value
    @property
    def legal_person_real_name(self):
        return self._legal_person_real_name

    @legal_person_real_name.setter
    def legal_person_real_name(self, value):
        self._legal_person_real_name = value
    @property
    def license_address(self):
        return self._license_address

    @license_address.setter
    def license_address(self, value):
        self._license_address = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_expired_date:
            if hasattr(self.cert_expired_date, 'to_alipay_dict'):
                params['cert_expired_date'] = self.cert_expired_date.to_alipay_dict()
            else:
                params['cert_expired_date'] = self.cert_expired_date
        if self.cert_mobile:
            if hasattr(self.cert_mobile, 'to_alipay_dict'):
                params['cert_mobile'] = self.cert_mobile.to_alipay_dict()
            else:
                params['cert_mobile'] = self.cert_mobile
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.legal_person_cert_expired_date:
            if hasattr(self.legal_person_cert_expired_date, 'to_alipay_dict'):
                params['legal_person_cert_expired_date'] = self.legal_person_cert_expired_date.to_alipay_dict()
            else:
                params['legal_person_cert_expired_date'] = self.legal_person_cert_expired_date
        if self.legal_person_cert_no:
            if hasattr(self.legal_person_cert_no, 'to_alipay_dict'):
                params['legal_person_cert_no'] = self.legal_person_cert_no.to_alipay_dict()
            else:
                params['legal_person_cert_no'] = self.legal_person_cert_no
        if self.legal_person_cert_type:
            if hasattr(self.legal_person_cert_type, 'to_alipay_dict'):
                params['legal_person_cert_type'] = self.legal_person_cert_type.to_alipay_dict()
            else:
                params['legal_person_cert_type'] = self.legal_person_cert_type
        if self.legal_person_mobile:
            if hasattr(self.legal_person_mobile, 'to_alipay_dict'):
                params['legal_person_mobile'] = self.legal_person_mobile.to_alipay_dict()
            else:
                params['legal_person_mobile'] = self.legal_person_mobile
        if self.legal_person_real_name:
            if hasattr(self.legal_person_real_name, 'to_alipay_dict'):
                params['legal_person_real_name'] = self.legal_person_real_name.to_alipay_dict()
            else:
                params['legal_person_real_name'] = self.legal_person_real_name
        if self.license_address:
            if hasattr(self.license_address, 'to_alipay_dict'):
                params['license_address'] = self.license_address.to_alipay_dict()
            else:
                params['license_address'] = self.license_address
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EscrowLicense()
        if 'cert_expired_date' in d:
            o.cert_expired_date = d['cert_expired_date']
        if 'cert_mobile' in d:
            o.cert_mobile = d['cert_mobile']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'legal_person_cert_expired_date' in d:
            o.legal_person_cert_expired_date = d['legal_person_cert_expired_date']
        if 'legal_person_cert_no' in d:
            o.legal_person_cert_no = d['legal_person_cert_no']
        if 'legal_person_cert_type' in d:
            o.legal_person_cert_type = d['legal_person_cert_type']
        if 'legal_person_mobile' in d:
            o.legal_person_mobile = d['legal_person_mobile']
        if 'legal_person_real_name' in d:
            o.legal_person_real_name = d['legal_person_real_name']
        if 'license_address' in d:
            o.license_address = d['license_address']
        if 'real_name' in d:
            o.real_name = d['real_name']
        return o


