#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysiscommodityCategoryrankingQueryModel(object):

    def __init__(self):
        self._cate_id = None
        self._cate_name = None
        self._common_request = None
        self._indicator_top = None
        self._trend = None

    @property
    def cate_id(self):
        return self._cate_id

    @cate_id.setter
    def cate_id(self, value):
        self._cate_id = value
    @property
    def cate_name(self):
        return self._cate_name

    @cate_name.setter
    def cate_name(self, value):
        self._cate_name = value
    @property
    def common_request(self):
        return self._common_request

    @common_request.setter
    def common_request(self, value):
        if isinstance(value, OpenApiAnalysisCommonRequest):
            self._common_request = value
        else:
            self._common_request = OpenApiAnalysisCommonRequest.from_alipay_dict(value)
    @property
    def indicator_top(self):
        return self._indicator_top

    @indicator_top.setter
    def indicator_top(self, value):
        self._indicator_top = value
    @property
    def trend(self):
        return self._trend

    @trend.setter
    def trend(self, value):
        self._trend = value


    def to_alipay_dict(self):
        params = dict()
        if self.cate_id:
            if hasattr(self.cate_id, 'to_alipay_dict'):
                params['cate_id'] = self.cate_id.to_alipay_dict()
            else:
                params['cate_id'] = self.cate_id
        if self.cate_name:
            if hasattr(self.cate_name, 'to_alipay_dict'):
                params['cate_name'] = self.cate_name.to_alipay_dict()
            else:
                params['cate_name'] = self.cate_name
        if self.common_request:
            if hasattr(self.common_request, 'to_alipay_dict'):
                params['common_request'] = self.common_request.to_alipay_dict()
            else:
                params['common_request'] = self.common_request
        if self.indicator_top:
            if hasattr(self.indicator_top, 'to_alipay_dict'):
                params['indicator_top'] = self.indicator_top.to_alipay_dict()
            else:
                params['indicator_top'] = self.indicator_top
        if self.trend:
            if hasattr(self.trend, 'to_alipay_dict'):
                params['trend'] = self.trend.to_alipay_dict()
            else:
                params['trend'] = self.trend
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAnalysiscommodityCategoryrankingQueryModel()
        if 'cate_id' in d:
            o.cate_id = d['cate_id']
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'common_request' in d:
            o.common_request = d['common_request']
        if 'indicator_top' in d:
            o.indicator_top = d['indicator_top']
        if 'trend' in d:
            o.trend = d['trend']
        return o


