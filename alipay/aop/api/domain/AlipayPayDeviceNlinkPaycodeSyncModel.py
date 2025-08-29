#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayDeviceNlinkPaycodeSyncModel(object):

    def __init__(self):
        self._biz_user_id = None
        self._create_time = None
        self._expire_time = None
        self._ntoken = None
        self._paycode = None
        self._paycode_status = None
        self._trade_no = None

    @property
    def biz_user_id(self):
        return self._biz_user_id

    @biz_user_id.setter
    def biz_user_id(self, value):
        self._biz_user_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def ntoken(self):
        return self._ntoken

    @ntoken.setter
    def ntoken(self, value):
        self._ntoken = value
    @property
    def paycode(self):
        return self._paycode

    @paycode.setter
    def paycode(self, value):
        self._paycode = value
    @property
    def paycode_status(self):
        return self._paycode_status

    @paycode_status.setter
    def paycode_status(self, value):
        self._paycode_status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_user_id:
            if hasattr(self.biz_user_id, 'to_alipay_dict'):
                params['biz_user_id'] = self.biz_user_id.to_alipay_dict()
            else:
                params['biz_user_id'] = self.biz_user_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.ntoken:
            if hasattr(self.ntoken, 'to_alipay_dict'):
                params['ntoken'] = self.ntoken.to_alipay_dict()
            else:
                params['ntoken'] = self.ntoken
        if self.paycode:
            if hasattr(self.paycode, 'to_alipay_dict'):
                params['paycode'] = self.paycode.to_alipay_dict()
            else:
                params['paycode'] = self.paycode
        if self.paycode_status:
            if hasattr(self.paycode_status, 'to_alipay_dict'):
                params['paycode_status'] = self.paycode_status.to_alipay_dict()
            else:
                params['paycode_status'] = self.paycode_status
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
        o = AlipayPayDeviceNlinkPaycodeSyncModel()
        if 'biz_user_id' in d:
            o.biz_user_id = d['biz_user_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'ntoken' in d:
            o.ntoken = d['ntoken']
        if 'paycode' in d:
            o.paycode = d['paycode']
        if 'paycode_status' in d:
            o.paycode_status = d['paycode_status']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


