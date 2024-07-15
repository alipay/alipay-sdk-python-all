#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallRenfundorderQueryModel(object):

    def __init__(self):
        self._dispute_id = None

    @property
    def dispute_id(self):
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, value):
        self._dispute_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.dispute_id:
            if hasattr(self.dispute_id, 'to_alipay_dict'):
                params['dispute_id'] = self.dispute_id.to_alipay_dict()
            else:
                params['dispute_id'] = self.dispute_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallRenfundorderQueryModel()
        if 'dispute_id' in d:
            o.dispute_id = d['dispute_id']
        return o


