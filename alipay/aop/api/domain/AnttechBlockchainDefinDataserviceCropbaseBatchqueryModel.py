#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinDataserviceCropbaseBatchqueryModel(object):

    def __init__(self):
        self._crop_code = None
        self._growth_strength = None
        self._is_growth_warn = None
        self._is_harvested = None
        self._need_crop_only = None
        self._page_no = None
        self._page_size = None
        self._region_codes = None

    @property
    def crop_code(self):
        return self._crop_code

    @crop_code.setter
    def crop_code(self, value):
        self._crop_code = value
    @property
    def growth_strength(self):
        return self._growth_strength

    @growth_strength.setter
    def growth_strength(self, value):
        self._growth_strength = value
    @property
    def is_growth_warn(self):
        return self._is_growth_warn

    @is_growth_warn.setter
    def is_growth_warn(self, value):
        self._is_growth_warn = value
    @property
    def is_harvested(self):
        return self._is_harvested

    @is_harvested.setter
    def is_harvested(self, value):
        self._is_harvested = value
    @property
    def need_crop_only(self):
        return self._need_crop_only

    @need_crop_only.setter
    def need_crop_only(self, value):
        self._need_crop_only = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def region_codes(self):
        return self._region_codes

    @region_codes.setter
    def region_codes(self, value):
        if isinstance(value, list):
            self._region_codes = list()
            for i in value:
                self._region_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.crop_code:
            if hasattr(self.crop_code, 'to_alipay_dict'):
                params['crop_code'] = self.crop_code.to_alipay_dict()
            else:
                params['crop_code'] = self.crop_code
        if self.growth_strength:
            if hasattr(self.growth_strength, 'to_alipay_dict'):
                params['growth_strength'] = self.growth_strength.to_alipay_dict()
            else:
                params['growth_strength'] = self.growth_strength
        if self.is_growth_warn:
            if hasattr(self.is_growth_warn, 'to_alipay_dict'):
                params['is_growth_warn'] = self.is_growth_warn.to_alipay_dict()
            else:
                params['is_growth_warn'] = self.is_growth_warn
        if self.is_harvested:
            if hasattr(self.is_harvested, 'to_alipay_dict'):
                params['is_harvested'] = self.is_harvested.to_alipay_dict()
            else:
                params['is_harvested'] = self.is_harvested
        if self.need_crop_only:
            if hasattr(self.need_crop_only, 'to_alipay_dict'):
                params['need_crop_only'] = self.need_crop_only.to_alipay_dict()
            else:
                params['need_crop_only'] = self.need_crop_only
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.region_codes:
            if isinstance(self.region_codes, list):
                for i in range(0, len(self.region_codes)):
                    element = self.region_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.region_codes[i] = element.to_alipay_dict()
            if hasattr(self.region_codes, 'to_alipay_dict'):
                params['region_codes'] = self.region_codes.to_alipay_dict()
            else:
                params['region_codes'] = self.region_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinDataserviceCropbaseBatchqueryModel()
        if 'crop_code' in d:
            o.crop_code = d['crop_code']
        if 'growth_strength' in d:
            o.growth_strength = d['growth_strength']
        if 'is_growth_warn' in d:
            o.is_growth_warn = d['is_growth_warn']
        if 'is_harvested' in d:
            o.is_harvested = d['is_harvested']
        if 'need_crop_only' in d:
            o.need_crop_only = d['need_crop_only']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'region_codes' in d:
            o.region_codes = d['region_codes']
        return o


