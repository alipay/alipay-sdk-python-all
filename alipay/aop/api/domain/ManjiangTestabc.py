#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ManjiangTestabc(object):

    def __init__(self):
        self._json = None
        self._t = None
        self._t_openid = None

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value
    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, value):
        self._t = value
    @property
    def t_openid(self):
        return self._t_openid

    @t_openid.setter
    def t_openid(self, value):
        self._t_openid = value


    def to_alipay_dict(self):
        params = dict()
        if self.json:
            if hasattr(self.json, 'to_alipay_dict'):
                params['json'] = self.json.to_alipay_dict()
            else:
                params['json'] = self.json
        if self.t:
            if hasattr(self.t, 'to_alipay_dict'):
                params['t'] = self.t.to_alipay_dict()
            else:
                params['t'] = self.t
        if self.t_openid:
            if hasattr(self.t_openid, 'to_alipay_dict'):
                params['t_openid'] = self.t_openid.to_alipay_dict()
            else:
                params['t_openid'] = self.t_openid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestabc()
        if 'json' in d:
            o.json = d['json']
        if 't' in d:
            o.t = d['t']
        if 't_openid' in d:
            o.t_openid = d['t_openid']
        return o


