#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderAnxinitemsellorderBatchqueryModel(object):

    def __init__(self):
        self._create_time = None
        self._mini_app_id = None
        self._page_size = None
        self._page_token = None
        self._trade_no = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def page_token(self):
        return self._page_token

    @page_token.setter
    def page_token(self, value):
        self._page_token = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.page_token:
            if hasattr(self.page_token, 'to_alipay_dict'):
                params['page_token'] = self.page_token.to_alipay_dict()
            else:
                params['page_token'] = self.page_token
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniOrderAnxinitemsellorderBatchqueryModel()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'page_token' in d:
            o.page_token = d['page_token']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


