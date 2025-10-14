#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClaimReportApplyIdentityMaterials(object):

    def __init__(self):
        self._material_type = None
        self._pic_urls = None

    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def pic_urls(self):
        return self._pic_urls

    @pic_urls.setter
    def pic_urls(self, value):
        self._pic_urls = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.pic_urls:
            if hasattr(self.pic_urls, 'to_alipay_dict'):
                params['pic_urls'] = self.pic_urls.to_alipay_dict()
            else:
                params['pic_urls'] = self.pic_urls
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClaimReportApplyIdentityMaterials()
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'pic_urls' in d:
            o.pic_urls = d['pic_urls']
        return o


