#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerZmcardInfoQueryModel(object):

    def __init__(self):
        self._guest_cert_no = None
        self._host_cert_no = None
        self._host_cert_type = None
        self._source = None

    @property
    def guest_cert_no(self):
        return self._guest_cert_no

    @guest_cert_no.setter
    def guest_cert_no(self, value):
        self._guest_cert_no = value
    @property
    def host_cert_no(self):
        return self._host_cert_no

    @host_cert_no.setter
    def host_cert_no(self, value):
        self._host_cert_no = value
    @property
    def host_cert_type(self):
        return self._host_cert_type

    @host_cert_type.setter
    def host_cert_type(self, value):
        self._host_cert_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.guest_cert_no:
            if hasattr(self.guest_cert_no, 'to_alipay_dict'):
                params['guest_cert_no'] = self.guest_cert_no.to_alipay_dict()
            else:
                params['guest_cert_no'] = self.guest_cert_no
        if self.host_cert_no:
            if hasattr(self.host_cert_no, 'to_alipay_dict'):
                params['host_cert_no'] = self.host_cert_no.to_alipay_dict()
            else:
                params['host_cert_no'] = self.host_cert_no
        if self.host_cert_type:
            if hasattr(self.host_cert_type, 'to_alipay_dict'):
                params['host_cert_type'] = self.host_cert_type.to_alipay_dict()
            else:
                params['host_cert_type'] = self.host_cert_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerZmcardInfoQueryModel()
        if 'guest_cert_no' in d:
            o.guest_cert_no = d['guest_cert_no']
        if 'host_cert_no' in d:
            o.host_cert_no = d['host_cert_no']
        if 'host_cert_type' in d:
            o.host_cert_type = d['host_cert_type']
        if 'source' in d:
            o.source = d['source']
        return o


