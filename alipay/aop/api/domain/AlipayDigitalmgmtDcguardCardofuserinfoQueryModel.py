#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtDcguardCardofuserinfoQueryModel(object):

    def __init__(self):
        self._main_no = None
        self._physical_no = None
        self._section_no = None

    @property
    def main_no(self):
        return self._main_no

    @main_no.setter
    def main_no(self, value):
        self._main_no = value
    @property
    def physical_no(self):
        return self._physical_no

    @physical_no.setter
    def physical_no(self, value):
        self._physical_no = value
    @property
    def section_no(self):
        return self._section_no

    @section_no.setter
    def section_no(self, value):
        self._section_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.main_no:
            if hasattr(self.main_no, 'to_alipay_dict'):
                params['main_no'] = self.main_no.to_alipay_dict()
            else:
                params['main_no'] = self.main_no
        if self.physical_no:
            if hasattr(self.physical_no, 'to_alipay_dict'):
                params['physical_no'] = self.physical_no.to_alipay_dict()
            else:
                params['physical_no'] = self.physical_no
        if self.section_no:
            if hasattr(self.section_no, 'to_alipay_dict'):
                params['section_no'] = self.section_no.to_alipay_dict()
            else:
                params['section_no'] = self.section_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtDcguardCardofuserinfoQueryModel()
        if 'main_no' in d:
            o.main_no = d['main_no']
        if 'physical_no' in d:
            o.physical_no = d['physical_no']
        if 'section_no' in d:
            o.section_no = d['section_no']
        return o


