#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppRateDataSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._control_status = None
        self._in_biz_account = None
        self._oper_type = None
        self._out_biz_account = None
        self._rate_id = None
        self._score = None
        self._shop_id = None
        self._source = None
        self._type = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def control_status(self):
        return self._control_status

    @control_status.setter
    def control_status(self, value):
        self._control_status = value
    @property
    def in_biz_account(self):
        return self._in_biz_account

    @in_biz_account.setter
    def in_biz_account(self, value):
        self._in_biz_account = value
    @property
    def oper_type(self):
        return self._oper_type

    @oper_type.setter
    def oper_type(self, value):
        self._oper_type = value
    @property
    def out_biz_account(self):
        return self._out_biz_account

    @out_biz_account.setter
    def out_biz_account(self, value):
        self._out_biz_account = value
    @property
    def rate_id(self):
        return self._rate_id

    @rate_id.setter
    def rate_id(self, value):
        self._rate_id = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.control_status:
            if hasattr(self.control_status, 'to_alipay_dict'):
                params['control_status'] = self.control_status.to_alipay_dict()
            else:
                params['control_status'] = self.control_status
        if self.in_biz_account:
            if hasattr(self.in_biz_account, 'to_alipay_dict'):
                params['in_biz_account'] = self.in_biz_account.to_alipay_dict()
            else:
                params['in_biz_account'] = self.in_biz_account
        if self.oper_type:
            if hasattr(self.oper_type, 'to_alipay_dict'):
                params['oper_type'] = self.oper_type.to_alipay_dict()
            else:
                params['oper_type'] = self.oper_type
        if self.out_biz_account:
            if hasattr(self.out_biz_account, 'to_alipay_dict'):
                params['out_biz_account'] = self.out_biz_account.to_alipay_dict()
            else:
                params['out_biz_account'] = self.out_biz_account
        if self.rate_id:
            if hasattr(self.rate_id, 'to_alipay_dict'):
                params['rate_id'] = self.rate_id.to_alipay_dict()
            else:
                params['rate_id'] = self.rate_id
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppRateDataSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'control_status' in d:
            o.control_status = d['control_status']
        if 'in_biz_account' in d:
            o.in_biz_account = d['in_biz_account']
        if 'oper_type' in d:
            o.oper_type = d['oper_type']
        if 'out_biz_account' in d:
            o.out_biz_account = d['out_biz_account']
        if 'rate_id' in d:
            o.rate_id = d['rate_id']
        if 'score' in d:
            o.score = d['score']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'source' in d:
            o.source = d['source']
        if 'type' in d:
            o.type = d['type']
        return o


