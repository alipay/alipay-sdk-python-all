#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthEcsignSealSaveModel(object):

    def __init__(self):
        self._enterprise_cert_no = None
        self._enterprise_name = None
        self._seal_description = None
        self._seal_id = None
        self._seal_name = None
        self._seal_type = None

    @property
    def enterprise_cert_no(self):
        return self._enterprise_cert_no

    @enterprise_cert_no.setter
    def enterprise_cert_no(self, value):
        self._enterprise_cert_no = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def seal_description(self):
        return self._seal_description

    @seal_description.setter
    def seal_description(self, value):
        self._seal_description = value
    @property
    def seal_id(self):
        return self._seal_id

    @seal_id.setter
    def seal_id(self, value):
        self._seal_id = value
    @property
    def seal_name(self):
        return self._seal_name

    @seal_name.setter
    def seal_name(self, value):
        self._seal_name = value
    @property
    def seal_type(self):
        return self._seal_type

    @seal_type.setter
    def seal_type(self, value):
        self._seal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_cert_no:
            if hasattr(self.enterprise_cert_no, 'to_alipay_dict'):
                params['enterprise_cert_no'] = self.enterprise_cert_no.to_alipay_dict()
            else:
                params['enterprise_cert_no'] = self.enterprise_cert_no
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.seal_description:
            if hasattr(self.seal_description, 'to_alipay_dict'):
                params['seal_description'] = self.seal_description.to_alipay_dict()
            else:
                params['seal_description'] = self.seal_description
        if self.seal_id:
            if hasattr(self.seal_id, 'to_alipay_dict'):
                params['seal_id'] = self.seal_id.to_alipay_dict()
            else:
                params['seal_id'] = self.seal_id
        if self.seal_name:
            if hasattr(self.seal_name, 'to_alipay_dict'):
                params['seal_name'] = self.seal_name.to_alipay_dict()
            else:
                params['seal_name'] = self.seal_name
        if self.seal_type:
            if hasattr(self.seal_type, 'to_alipay_dict'):
                params['seal_type'] = self.seal_type.to_alipay_dict()
            else:
                params['seal_type'] = self.seal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFinancialnetAuthEcsignSealSaveModel()
        if 'enterprise_cert_no' in d:
            o.enterprise_cert_no = d['enterprise_cert_no']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'seal_description' in d:
            o.seal_description = d['seal_description']
        if 'seal_id' in d:
            o.seal_id = d['seal_id']
        if 'seal_name' in d:
            o.seal_name = d['seal_name']
        if 'seal_type' in d:
            o.seal_type = d['seal_type']
        return o


