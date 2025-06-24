#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorIotnsphgHgauthGetModel(object):

    def __init__(self):
        self._amount = None
        self._biz_tid = None
        self._ori_out_trade_no = None
        self._ori_req_id = None
        self._out_trade_no = None
        self._pid = None
        self._req_id = None
        self._service_id = None
        self._sn = None
        self._terminal_id = None
        self._user_id = None
        self._user_open_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def ori_out_trade_no(self):
        return self._ori_out_trade_no

    @ori_out_trade_no.setter
    def ori_out_trade_no(self, value):
        self._ori_out_trade_no = value
    @property
    def ori_req_id(self):
        return self._ori_req_id

    @ori_req_id.setter
    def ori_req_id(self, value):
        self._ori_req_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def req_id(self):
        return self._req_id

    @req_id.setter
    def req_id(self, value):
        self._req_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value
    @property
    def terminal_id(self):
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, value):
        self._terminal_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.ori_out_trade_no:
            if hasattr(self.ori_out_trade_no, 'to_alipay_dict'):
                params['ori_out_trade_no'] = self.ori_out_trade_no.to_alipay_dict()
            else:
                params['ori_out_trade_no'] = self.ori_out_trade_no
        if self.ori_req_id:
            if hasattr(self.ori_req_id, 'to_alipay_dict'):
                params['ori_req_id'] = self.ori_req_id.to_alipay_dict()
            else:
                params['ori_req_id'] = self.ori_req_id
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.req_id:
            if hasattr(self.req_id, 'to_alipay_dict'):
                params['req_id'] = self.req_id.to_alipay_dict()
            else:
                params['req_id'] = self.req_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        if self.terminal_id:
            if hasattr(self.terminal_id, 'to_alipay_dict'):
                params['terminal_id'] = self.terminal_id.to_alipay_dict()
            else:
                params['terminal_id'] = self.terminal_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorIotnsphgHgauthGetModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'ori_out_trade_no' in d:
            o.ori_out_trade_no = d['ori_out_trade_no']
        if 'ori_req_id' in d:
            o.ori_req_id = d['ori_req_id']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pid' in d:
            o.pid = d['pid']
        if 'req_id' in d:
            o.req_id = d['req_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'sn' in d:
            o.sn = d['sn']
        if 'terminal_id' in d:
            o.terminal_id = d['terminal_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


