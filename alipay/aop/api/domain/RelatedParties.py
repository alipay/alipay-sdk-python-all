#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RelatedParties(object):

    def __init__(self):
        self._related_party_cert_no = None
        self._related_party_cert_type = None
        self._related_party_name = None
        self._related_party_type = None

    @property
    def related_party_cert_no(self):
        return self._related_party_cert_no

    @related_party_cert_no.setter
    def related_party_cert_no(self, value):
        self._related_party_cert_no = value
    @property
    def related_party_cert_type(self):
        return self._related_party_cert_type

    @related_party_cert_type.setter
    def related_party_cert_type(self, value):
        self._related_party_cert_type = value
    @property
    def related_party_name(self):
        return self._related_party_name

    @related_party_name.setter
    def related_party_name(self, value):
        self._related_party_name = value
    @property
    def related_party_type(self):
        return self._related_party_type

    @related_party_type.setter
    def related_party_type(self, value):
        self._related_party_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.related_party_cert_no:
            if hasattr(self.related_party_cert_no, 'to_alipay_dict'):
                params['related_party_cert_no'] = self.related_party_cert_no.to_alipay_dict()
            else:
                params['related_party_cert_no'] = self.related_party_cert_no
        if self.related_party_cert_type:
            if hasattr(self.related_party_cert_type, 'to_alipay_dict'):
                params['related_party_cert_type'] = self.related_party_cert_type.to_alipay_dict()
            else:
                params['related_party_cert_type'] = self.related_party_cert_type
        if self.related_party_name:
            if hasattr(self.related_party_name, 'to_alipay_dict'):
                params['related_party_name'] = self.related_party_name.to_alipay_dict()
            else:
                params['related_party_name'] = self.related_party_name
        if self.related_party_type:
            if hasattr(self.related_party_type, 'to_alipay_dict'):
                params['related_party_type'] = self.related_party_type.to_alipay_dict()
            else:
                params['related_party_type'] = self.related_party_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RelatedParties()
        if 'related_party_cert_no' in d:
            o.related_party_cert_no = d['related_party_cert_no']
        if 'related_party_cert_type' in d:
            o.related_party_cert_type = d['related_party_cert_type']
        if 'related_party_name' in d:
            o.related_party_name = d['related_party_name']
        if 'related_party_type' in d:
            o.related_party_type = d['related_party_type']
        return o


