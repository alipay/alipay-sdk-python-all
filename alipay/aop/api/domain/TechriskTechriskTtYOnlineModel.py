#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestab import ManjiangTestab


class TechriskTechriskTtYOnlineModel(object):

    def __init__(self):
        self._s_openid = None
        self._sss = None
        self._sss_open_id = None
        self._ssss = None
        self._test_1 = None

    @property
    def s_openid(self):
        return self._s_openid

    @s_openid.setter
    def s_openid(self, value):
        self._s_openid = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        self._sss = value
    @property
    def sss_open_id(self):
        return self._sss_open_id

    @sss_open_id.setter
    def sss_open_id(self, value):
        self._sss_open_id = value
    @property
    def ssss(self):
        return self._ssss

    @ssss.setter
    def ssss(self, value):
        self._ssss = value
    @property
    def test_1(self):
        return self._test_1

    @test_1.setter
    def test_1(self, value):
        if isinstance(value, ManjiangTestab):
            self._test_1 = value
        else:
            self._test_1 = ManjiangTestab.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.s_openid:
            if hasattr(self.s_openid, 'to_alipay_dict'):
                params['s_openid'] = self.s_openid.to_alipay_dict()
            else:
                params['s_openid'] = self.s_openid
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.sss_open_id:
            if hasattr(self.sss_open_id, 'to_alipay_dict'):
                params['sss_open_id'] = self.sss_open_id.to_alipay_dict()
            else:
                params['sss_open_id'] = self.sss_open_id
        if self.ssss:
            if hasattr(self.ssss, 'to_alipay_dict'):
                params['ssss'] = self.ssss.to_alipay_dict()
            else:
                params['ssss'] = self.ssss
        if self.test_1:
            if hasattr(self.test_1, 'to_alipay_dict'):
                params['test_1'] = self.test_1.to_alipay_dict()
            else:
                params['test_1'] = self.test_1
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskTechriskTtYOnlineModel()
        if 's_openid' in d:
            o.s_openid = d['s_openid']
        if 'sss' in d:
            o.sss = d['sss']
        if 'sss_open_id' in d:
            o.sss_open_id = d['sss_open_id']
        if 'ssss' in d:
            o.ssss = d['ssss']
        if 'test_1' in d:
            o.test_1 = d['test_1']
        return o


