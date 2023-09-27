#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AliyunBSN(object):

    def __init__(self):
        self._assign_ts = None
        self._beian_num = None
        self._bsn = None
        self._status = None

    @property
    def assign_ts(self):
        return self._assign_ts

    @assign_ts.setter
    def assign_ts(self, value):
        self._assign_ts = value
    @property
    def beian_num(self):
        return self._beian_num

    @beian_num.setter
    def beian_num(self, value):
        self._beian_num = value
    @property
    def bsn(self):
        return self._bsn

    @bsn.setter
    def bsn(self, value):
        self._bsn = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.assign_ts:
            if hasattr(self.assign_ts, 'to_alipay_dict'):
                params['assign_ts'] = self.assign_ts.to_alipay_dict()
            else:
                params['assign_ts'] = self.assign_ts
        if self.beian_num:
            if hasattr(self.beian_num, 'to_alipay_dict'):
                params['beian_num'] = self.beian_num.to_alipay_dict()
            else:
                params['beian_num'] = self.beian_num
        if self.bsn:
            if hasattr(self.bsn, 'to_alipay_dict'):
                params['bsn'] = self.bsn.to_alipay_dict()
            else:
                params['bsn'] = self.bsn
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AliyunBSN()
        if 'assign_ts' in d:
            o.assign_ts = d['assign_ts']
        if 'beian_num' in d:
            o.beian_num = d['beian_num']
        if 'bsn' in d:
            o.bsn = d['bsn']
        if 'status' in d:
            o.status = d['status']
        return o


