#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YpzCloudDispenseMedicineCardOne(object):

    def __init__(self):
        self._redirect_url = None
        self._status = None

    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YpzCloudDispenseMedicineCardOne()
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'status' in d:
            o.status = d['status']
        return o


