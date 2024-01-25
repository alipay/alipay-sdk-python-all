#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMiniBatchtemplatemsgQueryModel(object):

    def __init__(self):
        self._batch_msg_id = None

    @property
    def batch_msg_id(self):
        return self._batch_msg_id

    @batch_msg_id.setter
    def batch_msg_id(self, value):
        self._batch_msg_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_msg_id:
            if hasattr(self.batch_msg_id, 'to_alipay_dict'):
                params['batch_msg_id'] = self.batch_msg_id.to_alipay_dict()
            else:
                params['batch_msg_id'] = self.batch_msg_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMiniBatchtemplatemsgQueryModel()
        if 'batch_msg_id' in d:
            o.batch_msg_id = d['batch_msg_id']
        return o


