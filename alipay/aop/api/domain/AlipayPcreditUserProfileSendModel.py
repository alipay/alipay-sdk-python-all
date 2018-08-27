#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditUserProfileSendModel(object):

    def __init__(self):
        self._biz_no = None
        self._item_key = None
        self._out_biz_no = None
        self._params = None
        self._status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def item_key(self):
        return self._item_key

    @item_key.setter
    def item_key(self, value):
        self._item_key = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.item_key:
            if hasattr(self.item_key, 'to_alipay_dict'):
                params['item_key'] = self.item_key.to_alipay_dict()
            else:
                params['item_key'] = self.item_key
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
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
        o = AlipayPcreditUserProfileSendModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'item_key' in d:
            o.item_key = d['item_key']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'params' in d:
            o.params = d['params']
        if 'status' in d:
            o.status = d['status']
        return o


