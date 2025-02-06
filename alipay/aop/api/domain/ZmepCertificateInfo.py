#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepCertificateInfo(object):

    def __init__(self):
        self._authority = None
        self._certificate_no = None
        self._certificate_type = None
        self._expire_date = None
        self._issue_date = None
        self._valid = None

    @property
    def authority(self):
        return self._authority

    @authority.setter
    def authority(self, value):
        self._authority = value
    @property
    def certificate_no(self):
        return self._certificate_no

    @certificate_no.setter
    def certificate_no(self, value):
        self._certificate_no = value
    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value


    def to_alipay_dict(self):
        params = dict()
        if self.authority:
            if hasattr(self.authority, 'to_alipay_dict'):
                params['authority'] = self.authority.to_alipay_dict()
            else:
                params['authority'] = self.authority
        if self.certificate_no:
            if hasattr(self.certificate_no, 'to_alipay_dict'):
                params['certificate_no'] = self.certificate_no.to_alipay_dict()
            else:
                params['certificate_no'] = self.certificate_no
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.valid:
            if hasattr(self.valid, 'to_alipay_dict'):
                params['valid'] = self.valid.to_alipay_dict()
            else:
                params['valid'] = self.valid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepCertificateInfo()
        if 'authority' in d:
            o.authority = d['authority']
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'valid' in d:
            o.valid = d['valid']
        return o


