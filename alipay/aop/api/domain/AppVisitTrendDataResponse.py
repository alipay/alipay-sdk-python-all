#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppVisitTrendDataResponse(object):

    def __init__(self):
        self._app_pv = None
        self._app_uv = None
        self._report_time = None

    @property
    def app_pv(self):
        return self._app_pv

    @app_pv.setter
    def app_pv(self, value):
        self._app_pv = value
    @property
    def app_uv(self):
        return self._app_uv

    @app_uv.setter
    def app_uv(self, value):
        self._app_uv = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_pv:
            if hasattr(self.app_pv, 'to_alipay_dict'):
                params['app_pv'] = self.app_pv.to_alipay_dict()
            else:
                params['app_pv'] = self.app_pv
        if self.app_uv:
            if hasattr(self.app_uv, 'to_alipay_dict'):
                params['app_uv'] = self.app_uv.to_alipay_dict()
            else:
                params['app_uv'] = self.app_uv
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AppVisitTrendDataResponse()
        if 'app_pv' in d:
            o.app_pv = d['app_pv']
        if 'app_uv' in d:
            o.app_uv = d['app_uv']
        if 'report_time' in d:
            o.report_time = d['report_time']
        return o


