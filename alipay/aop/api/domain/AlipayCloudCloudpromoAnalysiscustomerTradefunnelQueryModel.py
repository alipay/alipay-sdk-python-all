#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysiscustomerTradefunnelQueryModel(object):

    def __init__(self):
        self._common_request = None

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
        o = AlipayCloudCloudpromoAnalysiscustomerTradefunnelQueryModel()
        if 'common_request' in d:
            o.common_request = d['common_request']
        return o


