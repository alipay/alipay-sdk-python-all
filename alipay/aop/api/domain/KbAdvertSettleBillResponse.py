#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertSettleBillResponse(object):

    def __init__(self):
        self._download_url = None
        self._paid_date = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def paid_date(self):
        return self._paid_date

    @paid_date.setter
    def paid_date(self, value):
        self._paid_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.paid_date:
            if hasattr(self.paid_date, 'to_alipay_dict'):
                params['paid_date'] = self.paid_date.to_alipay_dict()
            else:
                params['paid_date'] = self.paid_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSettleBillResponse()
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'paid_date' in d:
            o.paid_date = d['paid_date']
        return o


