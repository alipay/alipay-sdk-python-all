#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicContentCancelModel(object):

    def __init__(self):
        self._message_id = None

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicContentCancelModel()
        if 'message_id' in d:
            o.message_id = d['message_id']
        return o


