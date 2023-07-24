#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallReceivePrResponseData(object):

    def __init__(self):
        self._pur_req_id = None
        self._redirect_url = None

    @property
    def pur_req_id(self):
        return self._pur_req_id

    @pur_req_id.setter
    def pur_req_id(self, value):
        self._pur_req_id = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.pur_req_id:
            if hasattr(self.pur_req_id, 'to_alipay_dict'):
                params['pur_req_id'] = self.pur_req_id.to_alipay_dict()
            else:
                params['pur_req_id'] = self.pur_req_id
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallReceivePrResponseData()
        if 'pur_req_id' in d:
            o.pur_req_id = d['pur_req_id']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        return o


