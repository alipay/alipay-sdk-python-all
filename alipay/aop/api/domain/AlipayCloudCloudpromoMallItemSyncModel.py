#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMallItemSyncModel(object):

    def __init__(self):
        self._purchaser_id = None

    @property
    def purchaser_id(self):
        return self._purchaser_id

    @purchaser_id.setter
    def purchaser_id(self, value):
        self._purchaser_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.purchaser_id:
            if hasattr(self.purchaser_id, 'to_alipay_dict'):
                params['purchaser_id'] = self.purchaser_id.to_alipay_dict()
            else:
                params['purchaser_id'] = self.purchaser_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMallItemSyncModel()
        if 'purchaser_id' in d:
            o.purchaser_id = d['purchaser_id']
        return o


