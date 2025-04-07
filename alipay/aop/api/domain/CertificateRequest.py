#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CertificateRequest(object):

    def __init__(self):
        self._certificate_type = None
        self._channel = None
        self._materials = None
        self._principal_type = None
        self._source_id = None
        self._value = None

    @property
    def certificate_type(self):
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, value):
        self._certificate_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def materials(self):
        return self._materials

    @materials.setter
    def materials(self, value):
        if isinstance(value, list):
            self._materials = list()
            for i in value:
                self._materials.append(i)
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_type:
            if hasattr(self.certificate_type, 'to_alipay_dict'):
                params['certificate_type'] = self.certificate_type.to_alipay_dict()
            else:
                params['certificate_type'] = self.certificate_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.materials:
            if isinstance(self.materials, list):
                for i in range(0, len(self.materials)):
                    element = self.materials[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.materials[i] = element.to_alipay_dict()
            if hasattr(self.materials, 'to_alipay_dict'):
                params['materials'] = self.materials.to_alipay_dict()
            else:
                params['materials'] = self.materials
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CertificateRequest()
        if 'certificate_type' in d:
            o.certificate_type = d['certificate_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'materials' in d:
            o.materials = d['materials']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'value' in d:
            o.value = d['value']
        return o


