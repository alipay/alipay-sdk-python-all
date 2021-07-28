#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TuitionUserName import TuitionUserName


class TuitionCertificate(object):

    def __init__(self):
        self._certificate_no = None
        self._certificate_type = None
        self._effective_date = None
        self._expire_date = None
        self._holder_name = None

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
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def holder_name(self):
        return self._holder_name

    @holder_name.setter
    def holder_name(self, value):
        if isinstance(value, TuitionUserName):
            self._holder_name = value
        else:
            self._holder_name = TuitionUserName.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
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
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.holder_name:
            if hasattr(self.holder_name, 'to_alipay_dict'):
                params['holder_name'] = self.holder_name.to_alipay_dict()
            else:
                params['holder_name'] = self.holder_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionCertificate()
        if 'certificate_no' in d:
            o.certificate_no = d['certificate_no']
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'holder_name' in d:
            o.holder_name = d['holder_name']
        return o


