#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdCreative import AdCreative


class AlipayCommerceTransportAdCreativeCreateModel(object):

    def __init__(self):
        self._ad_creative = None
        self._ad_user_id = None

    @property
    def ad_creative(self):
        return self._ad_creative

    @ad_creative.setter
    def ad_creative(self, value):
        if isinstance(value, AdCreative):
            self._ad_creative = value
        else:
            self._ad_creative = AdCreative.from_alipay_dict(value)
    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_creative:
            if hasattr(self.ad_creative, 'to_alipay_dict'):
                params['ad_creative'] = self.ad_creative.to_alipay_dict()
            else:
                params['ad_creative'] = self.ad_creative
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdCreativeCreateModel()
        if 'ad_creative' in d:
            o.ad_creative = d['ad_creative']
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        return o


