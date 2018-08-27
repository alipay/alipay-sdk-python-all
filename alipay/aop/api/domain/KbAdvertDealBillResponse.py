#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertDealBillResponse(object):

    def __init__(self):
        self._download_url = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertDealBillResponse()
        if 'download_url' in d:
            o.download_url = d['download_url']
        return o


