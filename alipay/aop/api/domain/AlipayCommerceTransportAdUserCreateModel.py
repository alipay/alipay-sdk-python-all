#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdUser import AdUser


class AlipayCommerceTransportAdUserCreateModel(object):

    def __init__(self):
        self._ad_user = None

    @property
    def ad_user(self):
        return self._ad_user

    @ad_user.setter
    def ad_user(self, value):
        if isinstance(value, AdUser):
            self._ad_user = value
        else:
            self._ad_user = AdUser.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user:
            if hasattr(self.ad_user, 'to_alipay_dict'):
                params['ad_user'] = self.ad_user.to_alipay_dict()
            else:
                params['ad_user'] = self.ad_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdUserCreateModel()
        if 'ad_user' in d:
            o.ad_user = d['ad_user']
        return o


