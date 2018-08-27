#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryQualificationInfo(object):

    def __init__(self):
        self._industry_qualification_image = None
        self._industry_qualification_type = None

    @property
    def industry_qualification_image(self):
        return self._industry_qualification_image

    @industry_qualification_image.setter
    def industry_qualification_image(self, value):
        self._industry_qualification_image = value
    @property
    def industry_qualification_type(self):
        return self._industry_qualification_type

    @industry_qualification_type.setter
    def industry_qualification_type(self, value):
        self._industry_qualification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_qualification_image:
            if hasattr(self.industry_qualification_image, 'to_alipay_dict'):
                params['industry_qualification_image'] = self.industry_qualification_image.to_alipay_dict()
            else:
                params['industry_qualification_image'] = self.industry_qualification_image
        if self.industry_qualification_type:
            if hasattr(self.industry_qualification_type, 'to_alipay_dict'):
                params['industry_qualification_type'] = self.industry_qualification_type.to_alipay_dict()
            else:
                params['industry_qualification_type'] = self.industry_qualification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryQualificationInfo()
        if 'industry_qualification_image' in d:
            o.industry_qualification_image = d['industry_qualification_image']
        if 'industry_qualification_type' in d:
            o.industry_qualification_type = d['industry_qualification_type']
        return o


