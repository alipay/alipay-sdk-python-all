#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasAccountRejectedSyncModel(object):

    def __init__(self):
        self._biz_token = None
        self._gmt_rejected = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def gmt_rejected(self):
        return self._gmt_rejected

    @gmt_rejected.setter
    def gmt_rejected(self, value):
        self._gmt_rejected = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.gmt_rejected:
            if hasattr(self.gmt_rejected, 'to_alipay_dict'):
                params['gmt_rejected'] = self.gmt_rejected.to_alipay_dict()
            else:
                params['gmt_rejected'] = self.gmt_rejected
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasAccountRejectedSyncModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'gmt_rejected' in d:
            o.gmt_rejected = d['gmt_rejected']
        return o


