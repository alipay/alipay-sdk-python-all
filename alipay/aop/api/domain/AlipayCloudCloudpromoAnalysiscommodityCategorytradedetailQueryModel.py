#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysiscommodityCategorytradedetailQueryModel(object):

    def __init__(self):
        self._cate_name = None
        self._common_request = None

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


    def to_alipay_dict(self):
        params = dict()
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAnalysiscommodityCategorytradedetailQueryModel()
        if 'cate_name' in d:
            o.cate_name = d['cate_name']
        if 'common_request' in d:
            o.common_request = d['common_request']
        return o


