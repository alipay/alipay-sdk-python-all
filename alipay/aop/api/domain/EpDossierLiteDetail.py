#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpDossierLiteDetail(object):

    def __init__(self):
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_status = None
        self._ep_type = None

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
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def ep_type(self):
        return self._ep_type

    @ep_type.setter
    def ep_type(self, value):
        self._ep_type = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.ep_status:
            if hasattr(self.ep_status, 'to_alipay_dict'):
                params['ep_status'] = self.ep_status.to_alipay_dict()
            else:
                params['ep_status'] = self.ep_status
        if self.ep_type:
            if hasattr(self.ep_type, 'to_alipay_dict'):
                params['ep_type'] = self.ep_type.to_alipay_dict()
            else:
                params['ep_type'] = self.ep_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpDossierLiteDetail()
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_status' in d:
            o.ep_status = d['ep_status']
        if 'ep_type' in d:
            o.ep_type = d['ep_type']
        return o


