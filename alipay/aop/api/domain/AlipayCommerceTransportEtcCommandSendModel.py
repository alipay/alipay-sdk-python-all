#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcCommandSendModel(object):

    def __init__(self):
        self._biz_time = None
        self._command_reason = None
        self._corp_id = None
        self._etc_switch_status = None
        self._plate_color = None
        self._plate_no = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def command_reason(self):
        return self._command_reason

    @command_reason.setter
    def command_reason(self, value):
        self._command_reason = value
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def etc_switch_status(self):
        return self._etc_switch_status

    @etc_switch_status.setter
    def etc_switch_status(self, value):
        self._etc_switch_status = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.command_reason:
            if hasattr(self.command_reason, 'to_alipay_dict'):
                params['command_reason'] = self.command_reason.to_alipay_dict()
            else:
                params['command_reason'] = self.command_reason
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.etc_switch_status:
            if hasattr(self.etc_switch_status, 'to_alipay_dict'):
                params['etc_switch_status'] = self.etc_switch_status.to_alipay_dict()
            else:
                params['etc_switch_status'] = self.etc_switch_status
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcCommandSendModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'command_reason' in d:
            o.command_reason = d['command_reason']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'etc_switch_status' in d:
            o.etc_switch_status = d['etc_switch_status']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        return o


