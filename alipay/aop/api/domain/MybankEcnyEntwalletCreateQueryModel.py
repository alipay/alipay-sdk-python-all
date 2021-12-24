#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankEcnyEntwalletCreateQueryModel(object):

    def __init__(self):
        self._ent_cert_no = None
        self._ent_cert_type = None
        self._ent_name = None
        self._out_request_no = None
        self._process_no = None

    @property
    def ent_cert_no(self):
        return self._ent_cert_no

    @ent_cert_no.setter
    def ent_cert_no(self, value):
        self._ent_cert_no = value
    @property
    def ent_cert_type(self):
        return self._ent_cert_type

    @ent_cert_type.setter
    def ent_cert_type(self, value):
        self._ent_cert_type = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def process_no(self):
        return self._process_no

    @process_no.setter
    def process_no(self, value):
        self._process_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ent_cert_no:
            if hasattr(self.ent_cert_no, 'to_alipay_dict'):
                params['ent_cert_no'] = self.ent_cert_no.to_alipay_dict()
            else:
                params['ent_cert_no'] = self.ent_cert_no
        if self.ent_cert_type:
            if hasattr(self.ent_cert_type, 'to_alipay_dict'):
                params['ent_cert_type'] = self.ent_cert_type.to_alipay_dict()
            else:
                params['ent_cert_type'] = self.ent_cert_type
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.process_no:
            if hasattr(self.process_no, 'to_alipay_dict'):
                params['process_no'] = self.process_no.to_alipay_dict()
            else:
                params['process_no'] = self.process_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyEntwalletCreateQueryModel()
        if 'ent_cert_no' in d:
            o.ent_cert_no = d['ent_cert_no']
        if 'ent_cert_type' in d:
            o.ent_cert_type = d['ent_cert_type']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'process_no' in d:
            o.process_no = d['process_no']
        return o


