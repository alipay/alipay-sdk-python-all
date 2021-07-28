#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateImageDTO(object):

    def __init__(self):
        self._logo = None
        self._strip = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def strip(self):
        return self._strip

    @strip.setter
    def strip(self, value):
        self._strip = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.strip:
            if hasattr(self.strip, 'to_alipay_dict'):
                params['strip'] = self.strip.to_alipay_dict()
            else:
                params['strip'] = self.strip
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateImageDTO()
        if 'logo' in d:
            o.logo = d['logo']
        if 'strip' in d:
            o.strip = d['strip']
        return o


