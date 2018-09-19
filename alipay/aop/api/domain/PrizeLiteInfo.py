#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeLiteInfo(object):

    def __init__(self):
        self._out_prize_id = None
        self._status = None

    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
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
        o = PrizeLiteInfo()
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'status' in d:
            o.status = d['status']
        return o


