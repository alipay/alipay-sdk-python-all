#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiEventReportCommRequest import OpenApiEventReportCommRequest


class AlipayCloudCloudpromoEventreportEventdetailQueryModel(object):

    def __init__(self):
        self._event_request = None

    @property
    def event_request(self):
        return self._event_request

    @event_request.setter
    def event_request(self, value):
        if isinstance(value, OpenApiEventReportCommRequest):
            self._event_request = value
        else:
            self._event_request = OpenApiEventReportCommRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.event_request:
            if hasattr(self.event_request, 'to_alipay_dict'):
                params['event_request'] = self.event_request.to_alipay_dict()
            else:
                params['event_request'] = self.event_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoEventreportEventdetailQueryModel()
        if 'event_request' in d:
            o.event_request = d['event_request']
        return o


