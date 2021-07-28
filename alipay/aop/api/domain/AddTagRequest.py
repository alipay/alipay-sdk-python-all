#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AddTagRequest(object):

    def __init__(self):
        self._biz_id = None
        self._schain_id = None
        self._trade_no = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def schain_id(self):
        return self._schain_id

    @schain_id.setter
    def schain_id(self, value):
        self._schain_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.schain_id:
            if hasattr(self.schain_id, 'to_alipay_dict'):
                params['schain_id'] = self.schain_id.to_alipay_dict()
            else:
                params['schain_id'] = self.schain_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AddTagRequest()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'schain_id' in d:
            o.schain_id = d['schain_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


