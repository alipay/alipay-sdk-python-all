#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJfexportBillkeyQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._inst_code = None
        self._open_id = None
        self._source = None
        self._sub_biz_type = None
        self._user_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJfexportBillkeyQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


