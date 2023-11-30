#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PucExternalOrderDetailInfo(object):

    def __init__(self):
        self._billkey = None
        self._biz_type = None
        self._charge_inst = None
        self._external_biz_id = None
        self._out_biz_no = None
        self._sub_biz_type = None
        self._trade_no = None

    @property
    def billkey(self):
        return self._billkey

    @billkey.setter
    def billkey(self, value):
        self._billkey = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_inst(self):
        return self._charge_inst

    @charge_inst.setter
    def charge_inst(self, value):
        self._charge_inst = value
    @property
    def external_biz_id(self):
        return self._external_biz_id

    @external_biz_id.setter
    def external_biz_id(self, value):
        self._external_biz_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sub_biz_type(self):
        return self._sub_biz_type

    @sub_biz_type.setter
    def sub_biz_type(self, value):
        self._sub_biz_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.billkey:
            if hasattr(self.billkey, 'to_alipay_dict'):
                params['billkey'] = self.billkey.to_alipay_dict()
            else:
                params['billkey'] = self.billkey
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_inst:
            if hasattr(self.charge_inst, 'to_alipay_dict'):
                params['charge_inst'] = self.charge_inst.to_alipay_dict()
            else:
                params['charge_inst'] = self.charge_inst
        if self.external_biz_id:
            if hasattr(self.external_biz_id, 'to_alipay_dict'):
                params['external_biz_id'] = self.external_biz_id.to_alipay_dict()
            else:
                params['external_biz_id'] = self.external_biz_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sub_biz_type:
            if hasattr(self.sub_biz_type, 'to_alipay_dict'):
                params['sub_biz_type'] = self.sub_biz_type.to_alipay_dict()
            else:
                params['sub_biz_type'] = self.sub_biz_type
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
        o = PucExternalOrderDetailInfo()
        if 'billkey' in d:
            o.billkey = d['billkey']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_inst' in d:
            o.charge_inst = d['charge_inst']
        if 'external_biz_id' in d:
            o.external_biz_id = d['external_biz_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sub_biz_type' in d:
            o.sub_biz_type = d['sub_biz_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


