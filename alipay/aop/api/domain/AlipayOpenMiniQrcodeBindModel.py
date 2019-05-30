#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniQrcodeBindModel(object):

    def __init__(self):
        self._mode = None
        self._page_redirection = None
        self._route_url = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def page_redirection(self):
        return self._page_redirection

    @page_redirection.setter
    def page_redirection(self, value):
        self._page_redirection = value
    @property
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        self._route_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.page_redirection:
            if hasattr(self.page_redirection, 'to_alipay_dict'):
                params['page_redirection'] = self.page_redirection.to_alipay_dict()
            else:
                params['page_redirection'] = self.page_redirection
        if self.route_url:
            if hasattr(self.route_url, 'to_alipay_dict'):
                params['route_url'] = self.route_url.to_alipay_dict()
            else:
                params['route_url'] = self.route_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniQrcodeBindModel()
        if 'mode' in d:
            o.mode = d['mode']
        if 'page_redirection' in d:
            o.page_redirection = d['page_redirection']
        if 'route_url' in d:
            o.route_url = d['route_url']
        return o


