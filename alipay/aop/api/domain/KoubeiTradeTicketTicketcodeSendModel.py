#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbIsvMaCode import KbIsvMaCode


class KoubeiTradeTicketTicketcodeSendModel(object):

    def __init__(self):
        self._isv_ma_list = None
        self._order_no = None
        self._request_id = None
        self._send_order_no = None
        self._send_token = None
        self._valid_end = None
        self._valid_start = None

    @property
    def isv_ma_list(self):
        return self._isv_ma_list

    @isv_ma_list.setter
    def isv_ma_list(self, value):
        if isinstance(value, list):
            self._isv_ma_list = list()
            for i in value:
                if isinstance(i, KbIsvMaCode):
                    self._isv_ma_list.append(i)
                else:
                    self._isv_ma_list.append(KbIsvMaCode.from_alipay_dict(i))
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def send_order_no(self):
        return self._send_order_no

    @send_order_no.setter
    def send_order_no(self, value):
        self._send_order_no = value
    @property
    def send_token(self):
        return self._send_token

    @send_token.setter
    def send_token(self, value):
        self._send_token = value
    @property
    def valid_end(self):
        return self._valid_end

    @valid_end.setter
    def valid_end(self, value):
        self._valid_end = value
    @property
    def valid_start(self):
        return self._valid_start

    @valid_start.setter
    def valid_start(self, value):
        self._valid_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_ma_list:
            if isinstance(self.isv_ma_list, list):
                for i in range(0, len(self.isv_ma_list)):
                    element = self.isv_ma_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.isv_ma_list[i] = element.to_alipay_dict()
            if hasattr(self.isv_ma_list, 'to_alipay_dict'):
                params['isv_ma_list'] = self.isv_ma_list.to_alipay_dict()
            else:
                params['isv_ma_list'] = self.isv_ma_list
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.send_order_no:
            if hasattr(self.send_order_no, 'to_alipay_dict'):
                params['send_order_no'] = self.send_order_no.to_alipay_dict()
            else:
                params['send_order_no'] = self.send_order_no
        if self.send_token:
            if hasattr(self.send_token, 'to_alipay_dict'):
                params['send_token'] = self.send_token.to_alipay_dict()
            else:
                params['send_token'] = self.send_token
        if self.valid_end:
            if hasattr(self.valid_end, 'to_alipay_dict'):
                params['valid_end'] = self.valid_end.to_alipay_dict()
            else:
                params['valid_end'] = self.valid_end
        if self.valid_start:
            if hasattr(self.valid_start, 'to_alipay_dict'):
                params['valid_start'] = self.valid_start.to_alipay_dict()
            else:
                params['valid_start'] = self.valid_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiTradeTicketTicketcodeSendModel()
        if 'isv_ma_list' in d:
            o.isv_ma_list = d['isv_ma_list']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'send_order_no' in d:
            o.send_order_no = d['send_order_no']
        if 'send_token' in d:
            o.send_token = d['send_token']
        if 'valid_end' in d:
            o.valid_end = d['valid_end']
        if 'valid_start' in d:
            o.valid_start = d['valid_start']
        return o


