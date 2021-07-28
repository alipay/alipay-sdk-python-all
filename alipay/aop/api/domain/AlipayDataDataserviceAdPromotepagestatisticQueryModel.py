#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPromotepagestatisticQueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._end_time = None
        self._page_id = None
        self._principal_id = None
        self._start_time = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.page_id:
            if hasattr(self.page_id, 'to_alipay_dict'):
                params['page_id'] = self.page_id.to_alipay_dict()
            else:
                params['page_id'] = self.page_id
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPromotepagestatisticQueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'page_id' in d:
            o.page_id = d['page_id']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


