#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsultChannelResponse import ConsultChannelResponse
from alipay.aop.api.domain.ConsultRefuseResponse import ConsultRefuseResponse


class PreconsultResult(object):

    def __init__(self):
        self._channel_list = None
        self._inst_pid = None
        self._pass = None
        self._refuse_list = None

    @property
    def channel_list(self):
        return self._channel_list

    @channel_list.setter
    def channel_list(self, value):
        if isinstance(value, ConsultChannelResponse):
            self._channel_list = value
        else:
            self._channel_list = ConsultChannelResponse.from_alipay_dict(value)
    @property
    def inst_pid(self):
        return self._inst_pid

    @inst_pid.setter
    def inst_pid(self, value):
        self._inst_pid = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def refuse_list(self):
        return self._refuse_list

    @refuse_list.setter
    def refuse_list(self, value):
        if isinstance(value, ConsultRefuseResponse):
            self._refuse_list = value
        else:
            self._refuse_list = ConsultRefuseResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_list:
            if hasattr(self.channel_list, 'to_alipay_dict'):
                params['channel_list'] = self.channel_list.to_alipay_dict()
            else:
                params['channel_list'] = self.channel_list
        if self.inst_pid:
            if hasattr(self.inst_pid, 'to_alipay_dict'):
                params['inst_pid'] = self.inst_pid.to_alipay_dict()
            else:
                params['inst_pid'] = self.inst_pid
        if self.pass:
            if hasattr(self.pass, 'to_alipay_dict'):
                params['pass'] = self.pass.to_alipay_dict()
            else:
                params['pass'] = self.pass
        if self.refuse_list:
            if hasattr(self.refuse_list, 'to_alipay_dict'):
                params['refuse_list'] = self.refuse_list.to_alipay_dict()
            else:
                params['refuse_list'] = self.refuse_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PreconsultResult()
        if 'channel_list' in d:
            o.channel_list = d['channel_list']
        if 'inst_pid' in d:
            o.inst_pid = d['inst_pid']
        if 'pass' in d:
            o.pass = d['pass']
        if 'refuse_list' in d:
            o.refuse_list = d['refuse_list']
        return o


