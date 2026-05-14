#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExtInfoAttrs import ExtInfoAttrs


class OtherInfo(object):

    def __init__(self):
        self._ext_info_attrs = None
        self._medical_insurance = None

    @property
    def ext_info_attrs(self):
        return self._ext_info_attrs

    @ext_info_attrs.setter
    def ext_info_attrs(self, value):
        if isinstance(value, list):
            self._ext_info_attrs = list()
            for i in value:
                if isinstance(i, ExtInfoAttrs):
                    self._ext_info_attrs.append(i)
                else:
                    self._ext_info_attrs.append(ExtInfoAttrs.from_alipay_dict(i))
    @property
    def medical_insurance(self):
        return self._medical_insurance

    @medical_insurance.setter
    def medical_insurance(self, value):
        self._medical_insurance = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info_attrs:
            if isinstance(self.ext_info_attrs, list):
                for i in range(0, len(self.ext_info_attrs)):
                    element = self.ext_info_attrs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info_attrs[i] = element.to_alipay_dict()
            if hasattr(self.ext_info_attrs, 'to_alipay_dict'):
                params['ext_info_attrs'] = self.ext_info_attrs.to_alipay_dict()
            else:
                params['ext_info_attrs'] = self.ext_info_attrs
        if self.medical_insurance:
            if hasattr(self.medical_insurance, 'to_alipay_dict'):
                params['medical_insurance'] = self.medical_insurance.to_alipay_dict()
            else:
                params['medical_insurance'] = self.medical_insurance
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OtherInfo()
        if 'ext_info_attrs' in d:
            o.ext_info_attrs = d['ext_info_attrs']
        if 'medical_insurance' in d:
            o.medical_insurance = d['medical_insurance']
        return o


