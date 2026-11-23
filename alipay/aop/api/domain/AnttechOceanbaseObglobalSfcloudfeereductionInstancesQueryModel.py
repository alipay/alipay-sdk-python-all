#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSfcloudfeereductionInstancesQueryModel(object):

    def __init__(self):
        self._keyword = None
        self._leads_code = None
        self._ob_passport_id = None
        self._region = None

    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def ob_passport_id(self):
        return self._ob_passport_id

    @ob_passport_id.setter
    def ob_passport_id(self, value):
        self._ob_passport_id = value
    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.ob_passport_id:
            if hasattr(self.ob_passport_id, 'to_alipay_dict'):
                params['ob_passport_id'] = self.ob_passport_id.to_alipay_dict()
            else:
                params['ob_passport_id'] = self.ob_passport_id
        if self.region:
            if hasattr(self.region, 'to_alipay_dict'):
                params['region'] = self.region.to_alipay_dict()
            else:
                params['region'] = self.region
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcloudfeereductionInstancesQueryModel()
        if 'keyword' in d:
            o.keyword = d['keyword']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'ob_passport_id' in d:
            o.ob_passport_id = d['ob_passport_id']
        if 'region' in d:
            o.region = d['region']
        return o


