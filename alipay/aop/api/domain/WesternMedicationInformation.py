#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WesternMedicationInformation(object):

    def __init__(self):
        self._dosage = None
        self._medical_name = None
        self._remark = None
        self._spec = None
        self._usage = None

    @property
    def dosage(self):
        return self._dosage

    @dosage.setter
    def dosage(self, value):
        self._dosage = value
    @property
    def medical_name(self):
        return self._medical_name

    @medical_name.setter
    def medical_name(self, value):
        self._medical_name = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        self._spec = value
    @property
    def usage(self):
        return self._usage

    @usage.setter
    def usage(self, value):
        self._usage = value


    def to_alipay_dict(self):
        params = dict()
        if self.dosage:
            if hasattr(self.dosage, 'to_alipay_dict'):
                params['dosage'] = self.dosage.to_alipay_dict()
            else:
                params['dosage'] = self.dosage
        if self.medical_name:
            if hasattr(self.medical_name, 'to_alipay_dict'):
                params['medical_name'] = self.medical_name.to_alipay_dict()
            else:
                params['medical_name'] = self.medical_name
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.spec:
            if hasattr(self.spec, 'to_alipay_dict'):
                params['spec'] = self.spec.to_alipay_dict()
            else:
                params['spec'] = self.spec
        if self.usage:
            if hasattr(self.usage, 'to_alipay_dict'):
                params['usage'] = self.usage.to_alipay_dict()
            else:
                params['usage'] = self.usage
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WesternMedicationInformation()
        if 'dosage' in d:
            o.dosage = d['dosage']
        if 'medical_name' in d:
            o.medical_name = d['medical_name']
        if 'remark' in d:
            o.remark = d['remark']
        if 'spec' in d:
            o.spec = d['spec']
        if 'usage' in d:
            o.usage = d['usage']
        return o


