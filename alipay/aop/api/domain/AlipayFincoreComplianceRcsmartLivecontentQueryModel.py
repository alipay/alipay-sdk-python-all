#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceRcsmartLivecontentQueryModel(object):

    def __init__(self):
        self._app_name = None
        self._app_token = None
        self._live_audit_time_begain = None
        self._live_audit_time_end = None
        self._live_start_time_begain = None
        self._live_start_time_end = None
        self._page_no = None
        self._page_size = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value
    @property
    def live_audit_time_begain(self):
        return self._live_audit_time_begain

    @live_audit_time_begain.setter
    def live_audit_time_begain(self, value):
        self._live_audit_time_begain = value
    @property
    def live_audit_time_end(self):
        return self._live_audit_time_end

    @live_audit_time_end.setter
    def live_audit_time_end(self, value):
        self._live_audit_time_end = value
    @property
    def live_start_time_begain(self):
        return self._live_start_time_begain

    @live_start_time_begain.setter
    def live_start_time_begain(self, value):
        self._live_start_time_begain = value
    @property
    def live_start_time_end(self):
        return self._live_start_time_end

    @live_start_time_end.setter
    def live_start_time_end(self, value):
        self._live_start_time_end = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_token:
            if hasattr(self.app_token, 'to_alipay_dict'):
                params['app_token'] = self.app_token.to_alipay_dict()
            else:
                params['app_token'] = self.app_token
        if self.live_audit_time_begain:
            if hasattr(self.live_audit_time_begain, 'to_alipay_dict'):
                params['live_audit_time_begain'] = self.live_audit_time_begain.to_alipay_dict()
            else:
                params['live_audit_time_begain'] = self.live_audit_time_begain
        if self.live_audit_time_end:
            if hasattr(self.live_audit_time_end, 'to_alipay_dict'):
                params['live_audit_time_end'] = self.live_audit_time_end.to_alipay_dict()
            else:
                params['live_audit_time_end'] = self.live_audit_time_end
        if self.live_start_time_begain:
            if hasattr(self.live_start_time_begain, 'to_alipay_dict'):
                params['live_start_time_begain'] = self.live_start_time_begain.to_alipay_dict()
            else:
                params['live_start_time_begain'] = self.live_start_time_begain
        if self.live_start_time_end:
            if hasattr(self.live_start_time_end, 'to_alipay_dict'):
                params['live_start_time_end'] = self.live_start_time_end.to_alipay_dict()
            else:
                params['live_start_time_end'] = self.live_start_time_end
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcsmartLivecontentQueryModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_token' in d:
            o.app_token = d['app_token']
        if 'live_audit_time_begain' in d:
            o.live_audit_time_begain = d['live_audit_time_begain']
        if 'live_audit_time_end' in d:
            o.live_audit_time_end = d['live_audit_time_end']
        if 'live_start_time_begain' in d:
            o.live_start_time_begain = d['live_start_time_begain']
        if 'live_start_time_end' in d:
            o.live_start_time_end = d['live_start_time_end']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


