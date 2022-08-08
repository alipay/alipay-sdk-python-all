#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasAccountAppliedSyncModel(object):

    def __init__(self):
        self._biz_token = None
        self._gmt_applied = None
        self._out_biz_no = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def gmt_applied(self):
        return self._gmt_applied

    @gmt_applied.setter
    def gmt_applied(self, value):
        self._gmt_applied = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.gmt_applied:
            if hasattr(self.gmt_applied, 'to_alipay_dict'):
                params['gmt_applied'] = self.gmt_applied.to_alipay_dict()
            else:
                params['gmt_applied'] = self.gmt_applied
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasAccountAppliedSyncModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'gmt_applied' in d:
            o.gmt_applied = d['gmt_applied']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


