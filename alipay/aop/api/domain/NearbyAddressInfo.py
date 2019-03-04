#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NearbyAddressInfo(object):

    def __init__(self):
        self._audit_status = None
        self._certificate = None
        self._display_status = None
        self._fail_reason = None
        self._poi_address = None
        self._poi_id = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def certificate(self):
        return self._certificate

    @certificate.setter
    def certificate(self, value):
        self._certificate = value
    @property
    def display_status(self):
        return self._display_status

    @display_status.setter
    def display_status(self, value):
        self._display_status = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def poi_address(self):
        return self._poi_address

    @poi_address.setter
    def poi_address(self, value):
        self._poi_address = value
    @property
    def poi_id(self):
        return self._poi_id

    @poi_id.setter
    def poi_id(self, value):
        self._poi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.audit_status:
            if hasattr(self.audit_status, 'to_alipay_dict'):
                params['audit_status'] = self.audit_status.to_alipay_dict()
            else:
                params['audit_status'] = self.audit_status
        if self.certificate:
            if hasattr(self.certificate, 'to_alipay_dict'):
                params['certificate'] = self.certificate.to_alipay_dict()
            else:
                params['certificate'] = self.certificate
        if self.display_status:
            if hasattr(self.display_status, 'to_alipay_dict'):
                params['display_status'] = self.display_status.to_alipay_dict()
            else:
                params['display_status'] = self.display_status
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.poi_address:
            if hasattr(self.poi_address, 'to_alipay_dict'):
                params['poi_address'] = self.poi_address.to_alipay_dict()
            else:
                params['poi_address'] = self.poi_address
        if self.poi_id:
            if hasattr(self.poi_id, 'to_alipay_dict'):
                params['poi_id'] = self.poi_id.to_alipay_dict()
            else:
                params['poi_id'] = self.poi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NearbyAddressInfo()
        if 'audit_status' in d:
            o.audit_status = d['audit_status']
        if 'certificate' in d:
            o.certificate = d['certificate']
        if 'display_status' in d:
            o.display_status = d['display_status']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'poi_address' in d:
            o.poi_address = d['poi_address']
        if 'poi_id' in d:
            o.poi_id = d['poi_id']
        return o


