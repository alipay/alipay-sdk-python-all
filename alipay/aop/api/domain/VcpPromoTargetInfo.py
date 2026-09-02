#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VcpBizIndicator import VcpBizIndicator


class VcpPromoTargetInfo(object):

    def __init__(self):
        self._biz_indicator = None
        self._indicator_value = None
        self._region_code = None
        self._region_name = None

    @property
    def biz_indicator(self):
        return self._biz_indicator

    @biz_indicator.setter
    def biz_indicator(self, value):
        if isinstance(value, VcpBizIndicator):
            self._biz_indicator = value
        else:
            self._biz_indicator = VcpBizIndicator.from_alipay_dict(value)
    @property
    def indicator_value(self):
        return self._indicator_value

    @indicator_value.setter
    def indicator_value(self, value):
        self._indicator_value = value
    @property
    def region_code(self):
        return self._region_code

    @region_code.setter
    def region_code(self, value):
        self._region_code = value
    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value):
        self._region_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_indicator:
            if hasattr(self.biz_indicator, 'to_alipay_dict'):
                params['biz_indicator'] = self.biz_indicator.to_alipay_dict()
            else:
                params['biz_indicator'] = self.biz_indicator
        if self.indicator_value:
            if hasattr(self.indicator_value, 'to_alipay_dict'):
                params['indicator_value'] = self.indicator_value.to_alipay_dict()
            else:
                params['indicator_value'] = self.indicator_value
        if self.region_code:
            if hasattr(self.region_code, 'to_alipay_dict'):
                params['region_code'] = self.region_code.to_alipay_dict()
            else:
                params['region_code'] = self.region_code
        if self.region_name:
            if hasattr(self.region_name, 'to_alipay_dict'):
                params['region_name'] = self.region_name.to_alipay_dict()
            else:
                params['region_name'] = self.region_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpPromoTargetInfo()
        if 'biz_indicator' in d:
            o.biz_indicator = d['biz_indicator']
        if 'indicator_value' in d:
            o.indicator_value = d['indicator_value']
        if 'region_code' in d:
            o.region_code = d['region_code']
        if 'region_name' in d:
            o.region_name = d['region_name']
        return o


