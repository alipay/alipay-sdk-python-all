#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasRemitResultFinishModel(object):

    def __init__(self):
        self._biz_result_code = None
        self._biz_result_msg = None
        self._biz_result_status = None
        self._complete_time = None
        self._external_biz_no = None
        self._receiver_mid = None
        self._sender_mid = None

    @property
    def biz_result_code(self):
        return self._biz_result_code

    @biz_result_code.setter
    def biz_result_code(self, value):
        self._biz_result_code = value
    @property
    def biz_result_msg(self):
        return self._biz_result_msg

    @biz_result_msg.setter
    def biz_result_msg(self, value):
        self._biz_result_msg = value
    @property
    def biz_result_status(self):
        return self._biz_result_status

    @biz_result_status.setter
    def biz_result_status(self, value):
        self._biz_result_status = value
    @property
    def complete_time(self):
        return self._complete_time

    @complete_time.setter
    def complete_time(self, value):
        self._complete_time = value
    @property
    def external_biz_no(self):
        return self._external_biz_no

    @external_biz_no.setter
    def external_biz_no(self, value):
        self._external_biz_no = value
    @property
    def receiver_mid(self):
        return self._receiver_mid

    @receiver_mid.setter
    def receiver_mid(self, value):
        self._receiver_mid = value
    @property
    def sender_mid(self):
        return self._sender_mid

    @sender_mid.setter
    def sender_mid(self, value):
        self._sender_mid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_result_code:
            if hasattr(self.biz_result_code, 'to_alipay_dict'):
                params['biz_result_code'] = self.biz_result_code.to_alipay_dict()
            else:
                params['biz_result_code'] = self.biz_result_code
        if self.biz_result_msg:
            if hasattr(self.biz_result_msg, 'to_alipay_dict'):
                params['biz_result_msg'] = self.biz_result_msg.to_alipay_dict()
            else:
                params['biz_result_msg'] = self.biz_result_msg
        if self.biz_result_status:
            if hasattr(self.biz_result_status, 'to_alipay_dict'):
                params['biz_result_status'] = self.biz_result_status.to_alipay_dict()
            else:
                params['biz_result_status'] = self.biz_result_status
        if self.complete_time:
            if hasattr(self.complete_time, 'to_alipay_dict'):
                params['complete_time'] = self.complete_time.to_alipay_dict()
            else:
                params['complete_time'] = self.complete_time
        if self.external_biz_no:
            if hasattr(self.external_biz_no, 'to_alipay_dict'):
                params['external_biz_no'] = self.external_biz_no.to_alipay_dict()
            else:
                params['external_biz_no'] = self.external_biz_no
        if self.receiver_mid:
            if hasattr(self.receiver_mid, 'to_alipay_dict'):
                params['receiver_mid'] = self.receiver_mid.to_alipay_dict()
            else:
                params['receiver_mid'] = self.receiver_mid
        if self.sender_mid:
            if hasattr(self.sender_mid, 'to_alipay_dict'):
                params['sender_mid'] = self.sender_mid.to_alipay_dict()
            else:
                params['sender_mid'] = self.sender_mid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasRemitResultFinishModel()
        if 'biz_result_code' in d:
            o.biz_result_code = d['biz_result_code']
        if 'biz_result_msg' in d:
            o.biz_result_msg = d['biz_result_msg']
        if 'biz_result_status' in d:
            o.biz_result_status = d['biz_result_status']
        if 'complete_time' in d:
            o.complete_time = d['complete_time']
        if 'external_biz_no' in d:
            o.external_biz_no = d['external_biz_no']
        if 'receiver_mid' in d:
            o.receiver_mid = d['receiver_mid']
        if 'sender_mid' in d:
            o.sender_mid = d['sender_mid']
        return o


