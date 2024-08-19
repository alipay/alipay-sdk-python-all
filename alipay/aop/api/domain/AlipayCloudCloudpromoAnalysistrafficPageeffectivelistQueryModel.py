#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysistrafficPageeffectivelistQueryModel(object):

    def __init__(self):
        self._common_request = None
        self._page_name = None
        self._page_url_md5 = None
        self._trend = None

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
    def page_name(self):
        return self._page_name

    @page_name.setter
    def page_name(self, value):
        self._page_name = value
    @property
    def page_url_md5(self):
        return self._page_url_md5

    @page_url_md5.setter
    def page_url_md5(self, value):
        self._page_url_md5 = value
    @property
    def trend(self):
        return self._trend

    @trend.setter
    def trend(self, value):
        self._trend = value


    def to_alipay_dict(self):
        params = dict()
        if self.common_request:
            if hasattr(self.common_request, 'to_alipay_dict'):
                params['common_request'] = self.common_request.to_alipay_dict()
            else:
                params['common_request'] = self.common_request
        if self.page_name:
            if hasattr(self.page_name, 'to_alipay_dict'):
                params['page_name'] = self.page_name.to_alipay_dict()
            else:
                params['page_name'] = self.page_name
        if self.page_url_md5:
            if hasattr(self.page_url_md5, 'to_alipay_dict'):
                params['page_url_md5'] = self.page_url_md5.to_alipay_dict()
            else:
                params['page_url_md5'] = self.page_url_md5
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
        o = AlipayCloudCloudpromoAnalysistrafficPageeffectivelistQueryModel()
        if 'common_request' in d:
            o.common_request = d['common_request']
        if 'page_name' in d:
            o.page_name = d['page_name']
        if 'page_url_md5' in d:
            o.page_url_md5 = d['page_url_md5']
        if 'trend' in d:
            o.trend = d['trend']
        return o


