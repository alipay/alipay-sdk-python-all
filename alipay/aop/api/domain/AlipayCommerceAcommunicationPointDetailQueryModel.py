#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPointDetailQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._page_size = None
        self._start_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_id(self):
        return self._start_id

    @start_id.setter
    def start_id(self, value):
        self._start_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_id:
            if hasattr(self.start_id, 'to_alipay_dict'):
                params['start_id'] = self.start_id.to_alipay_dict()
            else:
                params['start_id'] = self.start_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationPointDetailQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_id' in d:
            o.start_id = d['start_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


