#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseLeaseStateSyncModel(object):

    def __init__(self):
        self._lease_ca_file = None
        self._lease_code = None
        self._lease_status = None

    @property
    def lease_ca_file(self):
        return self._lease_ca_file

    @lease_ca_file.setter
    def lease_ca_file(self, value):
        self._lease_ca_file = value
    @property
    def lease_code(self):
        return self._lease_code

    @lease_code.setter
    def lease_code(self, value):
        self._lease_code = value
    @property
    def lease_status(self):
        return self._lease_status

    @lease_status.setter
    def lease_status(self, value):
        self._lease_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.lease_ca_file:
            if hasattr(self.lease_ca_file, 'to_alipay_dict'):
                params['lease_ca_file'] = self.lease_ca_file.to_alipay_dict()
            else:
                params['lease_ca_file'] = self.lease_ca_file
        if self.lease_code:
            if hasattr(self.lease_code, 'to_alipay_dict'):
                params['lease_code'] = self.lease_code.to_alipay_dict()
            else:
                params['lease_code'] = self.lease_code
        if self.lease_status:
            if hasattr(self.lease_status, 'to_alipay_dict'):
                params['lease_status'] = self.lease_status.to_alipay_dict()
            else:
                params['lease_status'] = self.lease_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseLeaseStateSyncModel()
        if 'lease_ca_file' in d:
            o.lease_ca_file = d['lease_ca_file']
        if 'lease_code' in d:
            o.lease_code = d['lease_code']
        if 'lease_status' in d:
            o.lease_status = d['lease_status']
        return o


