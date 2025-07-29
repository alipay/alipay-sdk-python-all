#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompanyInvoiceClerk(object):

    def __init__(self):
        self._clerk_cert_no = None
        self._clerk_name = None
        self._clerk_no = None

    @property
    def clerk_cert_no(self):
        return self._clerk_cert_no

    @clerk_cert_no.setter
    def clerk_cert_no(self, value):
        self._clerk_cert_no = value
    @property
    def clerk_name(self):
        return self._clerk_name

    @clerk_name.setter
    def clerk_name(self, value):
        self._clerk_name = value
    @property
    def clerk_no(self):
        return self._clerk_no

    @clerk_no.setter
    def clerk_no(self, value):
        self._clerk_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.clerk_cert_no:
            if hasattr(self.clerk_cert_no, 'to_alipay_dict'):
                params['clerk_cert_no'] = self.clerk_cert_no.to_alipay_dict()
            else:
                params['clerk_cert_no'] = self.clerk_cert_no
        if self.clerk_name:
            if hasattr(self.clerk_name, 'to_alipay_dict'):
                params['clerk_name'] = self.clerk_name.to_alipay_dict()
            else:
                params['clerk_name'] = self.clerk_name
        if self.clerk_no:
            if hasattr(self.clerk_no, 'to_alipay_dict'):
                params['clerk_no'] = self.clerk_no.to_alipay_dict()
            else:
                params['clerk_no'] = self.clerk_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompanyInvoiceClerk()
        if 'clerk_cert_no' in d:
            o.clerk_cert_no = d['clerk_cert_no']
        if 'clerk_name' in d:
            o.clerk_name = d['clerk_name']
        if 'clerk_no' in d:
            o.clerk_no = d['clerk_no']
        return o


