#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCsfuServicehallSyncModel(object):

    def __init__(self):
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value


    def to_alipay_dict(self):
        params = dict()
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCsfuServicehallSyncModel()
        if 'message' in d:
            o.message = d['message']
        return o


