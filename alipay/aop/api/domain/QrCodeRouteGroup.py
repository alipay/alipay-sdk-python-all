#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QrCodeRouteGroup(object):

    def __init__(self):
        self._mode = None
        self._route_group = None
        self._route_url = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def route_group(self):
        return self._route_group

    @route_group.setter
    def route_group(self, value):
        self._route_group = value
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
        if self.route_group:
            if hasattr(self.route_group, 'to_alipay_dict'):
                params['route_group'] = self.route_group.to_alipay_dict()
            else:
                params['route_group'] = self.route_group
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
        o = QrCodeRouteGroup()
        if 'mode' in d:
            o.mode = d['mode']
        if 'route_group' in d:
            o.route_group = d['route_group']
        if 'route_url' in d:
            o.route_url = d['route_url']
        return o


