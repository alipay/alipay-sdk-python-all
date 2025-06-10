#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DentalInquiryArchivesDiseaseLevelInfo(object):

    def __init__(self):
        self._level_code = None
        self._level_name = None
        self._level_text = None

    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, value):
        self._level_code = value
    @property
    def level_name(self):
        return self._level_name

    @level_name.setter
    def level_name(self, value):
        self._level_name = value
    @property
    def level_text(self):
        return self._level_text

    @level_text.setter
    def level_text(self, value):
        self._level_text = value


    def to_alipay_dict(self):
        params = dict()
        if self.level_code:
            if hasattr(self.level_code, 'to_alipay_dict'):
                params['level_code'] = self.level_code.to_alipay_dict()
            else:
                params['level_code'] = self.level_code
        if self.level_name:
            if hasattr(self.level_name, 'to_alipay_dict'):
                params['level_name'] = self.level_name.to_alipay_dict()
            else:
                params['level_name'] = self.level_name
        if self.level_text:
            if hasattr(self.level_text, 'to_alipay_dict'):
                params['level_text'] = self.level_text.to_alipay_dict()
            else:
                params['level_text'] = self.level_text
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DentalInquiryArchivesDiseaseLevelInfo()
        if 'level_code' in d:
            o.level_code = d['level_code']
        if 'level_name' in d:
            o.level_name = d['level_name']
        if 'level_text' in d:
            o.level_text = d['level_text']
        return o


