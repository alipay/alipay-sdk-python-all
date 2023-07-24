#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCrlevelQueryModel(object):

    def __init__(self):
        self._auth_no = None
        self._auth_url = None
        self._cognizant_cert_no = None
        self._cognizant_name = None
        self._ep_cert_no = None
        self._ep_name = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value
    @property
    def cognizant_cert_no(self):
        return self._cognizant_cert_no

    @cognizant_cert_no.setter
    def cognizant_cert_no(self, value):
        self._cognizant_cert_no = value
    @property
    def cognizant_name(self):
        return self._cognizant_name

    @cognizant_name.setter
    def cognizant_name(self, value):
        self._cognizant_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.auth_url:
            if hasattr(self.auth_url, 'to_alipay_dict'):
                params['auth_url'] = self.auth_url.to_alipay_dict()
            else:
                params['auth_url'] = self.auth_url
        if self.cognizant_cert_no:
            if hasattr(self.cognizant_cert_no, 'to_alipay_dict'):
                params['cognizant_cert_no'] = self.cognizant_cert_no.to_alipay_dict()
            else:
                params['cognizant_cert_no'] = self.cognizant_cert_no
        if self.cognizant_name:
            if hasattr(self.cognizant_name, 'to_alipay_dict'):
                params['cognizant_name'] = self.cognizant_name.to_alipay_dict()
            else:
                params['cognizant_name'] = self.cognizant_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCrlevelQueryModel()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'auth_url' in d:
            o.auth_url = d['auth_url']
        if 'cognizant_cert_no' in d:
            o.cognizant_cert_no = d['cognizant_cert_no']
        if 'cognizant_name' in d:
            o.cognizant_name = d['cognizant_name']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        return o


