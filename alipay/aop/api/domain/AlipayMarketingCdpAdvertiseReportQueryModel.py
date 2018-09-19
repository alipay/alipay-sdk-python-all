#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCdpAdvertiseReportQueryModel(object):

    def __init__(self):
        self._ad_id = None

    @property
    def ad_id(self):
        return self._ad_id

    @ad_id.setter
    def ad_id(self, value):
        self._ad_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_id:
            if hasattr(self.ad_id, 'to_alipay_dict'):
                params['ad_id'] = self.ad_id.to_alipay_dict()
            else:
                params['ad_id'] = self.ad_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCdpAdvertiseReportQueryModel()
        if 'ad_id' in d:
            o.ad_id = d['ad_id']
        return o


