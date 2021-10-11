#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpBranchInfo(object):

    def __init__(self):
        self._branch_cert_no = None
        self._branch_name = None
        self._registry_agency = None

    @property
    def branch_cert_no(self):
        return self._branch_cert_no

    @branch_cert_no.setter
    def branch_cert_no(self, value):
        self._branch_cert_no = value
    @property
    def branch_name(self):
        return self._branch_name

    @branch_name.setter
    def branch_name(self, value):
        self._branch_name = value
    @property
    def registry_agency(self):
        return self._registry_agency

    @registry_agency.setter
    def registry_agency(self, value):
        self._registry_agency = value


    def to_alipay_dict(self):
        params = dict()
        if self.branch_cert_no:
            if hasattr(self.branch_cert_no, 'to_alipay_dict'):
                params['branch_cert_no'] = self.branch_cert_no.to_alipay_dict()
            else:
                params['branch_cert_no'] = self.branch_cert_no
        if self.branch_name:
            if hasattr(self.branch_name, 'to_alipay_dict'):
                params['branch_name'] = self.branch_name.to_alipay_dict()
            else:
                params['branch_name'] = self.branch_name
        if self.registry_agency:
            if hasattr(self.registry_agency, 'to_alipay_dict'):
                params['registry_agency'] = self.registry_agency.to_alipay_dict()
            else:
                params['registry_agency'] = self.registry_agency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpBranchInfo()
        if 'branch_cert_no' in d:
            o.branch_cert_no = d['branch_cert_no']
        if 'branch_name' in d:
            o.branch_name = d['branch_name']
        if 'registry_agency' in d:
            o.registry_agency = d['registry_agency']
        return o


