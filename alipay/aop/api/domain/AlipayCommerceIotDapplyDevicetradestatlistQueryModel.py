#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotDapplyDevicetradestatlistQueryModel(object):

    def __init__(self):
        self._offset = None
        self._page_size = None
        self._stat_end = None
        self._stat_start = None

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def stat_end(self):
        return self._stat_end

    @stat_end.setter
    def stat_end(self, value):
        self._stat_end = value
    @property
    def stat_start(self):
        return self._stat_start

    @stat_start.setter
    def stat_start(self, value):
        self._stat_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.offset:
            if hasattr(self.offset, 'to_alipay_dict'):
                params['offset'] = self.offset.to_alipay_dict()
            else:
                params['offset'] = self.offset
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.stat_end:
            if hasattr(self.stat_end, 'to_alipay_dict'):
                params['stat_end'] = self.stat_end.to_alipay_dict()
            else:
                params['stat_end'] = self.stat_end
        if self.stat_start:
            if hasattr(self.stat_start, 'to_alipay_dict'):
                params['stat_start'] = self.stat_start.to_alipay_dict()
            else:
                params['stat_start'] = self.stat_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDapplyDevicetradestatlistQueryModel()
        if 'offset' in d:
            o.offset = d['offset']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'stat_end' in d:
            o.stat_end = d['stat_end']
        if 'stat_start' in d:
            o.stat_start = d['stat_start']
        return o


