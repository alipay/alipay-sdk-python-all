#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiInfoVO import ApiInfoVO
from alipay.aop.api.domain.ApiInfoVO import ApiInfoVO


class ManjiangTestabc(object):

    def __init__(self):
        self._json = None
        self._ssddf = None
        self._sss_2 = None
        self._t = None
        self._t_openid = None

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value
    @property
    def ssddf(self):
        return self._ssddf

    @ssddf.setter
    def ssddf(self, value):
        if isinstance(value, ApiInfoVO):
            self._ssddf = value
        else:
            self._ssddf = ApiInfoVO.from_alipay_dict(value)
    @property
    def sss_2(self):
        return self._sss_2

    @sss_2.setter
    def sss_2(self, value):
        if isinstance(value, ApiInfoVO):
            self._sss_2 = value
        else:
            self._sss_2 = ApiInfoVO.from_alipay_dict(value)
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
        if self.ssddf:
            if hasattr(self.ssddf, 'to_alipay_dict'):
                params['ssddf'] = self.ssddf.to_alipay_dict()
            else:
                params['ssddf'] = self.ssddf
        if self.sss_2:
            if hasattr(self.sss_2, 'to_alipay_dict'):
                params['sss_2'] = self.sss_2.to_alipay_dict()
            else:
                params['sss_2'] = self.sss_2
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
        if 'ssddf' in d:
            o.ssddf = d['ssddf']
        if 'sss_2' in d:
            o.sss_2 = d['sss_2']
        if 't' in d:
            o.t = d['t']
        if 't_openid' in d:
            o.t_openid = d['t_openid']
        return o


