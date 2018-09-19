#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicThirdCustomerServiceModel(object):

    def __init__(self):
        self._channel_uid = None

    @property
    def channel_uid(self):
        return self._channel_uid

    @channel_uid.setter
    def channel_uid(self, value):
        self._channel_uid = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_uid:
            if hasattr(self.channel_uid, 'to_alipay_dict'):
                params['channel_uid'] = self.channel_uid.to_alipay_dict()
            else:
                params['channel_uid'] = self.channel_uid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicThirdCustomerServiceModel()
        if 'channel_uid' in d:
            o.channel_uid = d['channel_uid']
        return o


