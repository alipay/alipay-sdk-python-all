#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAicsDtcontrolVisitorqueueQueryModel(object):

    def __init__(self):
        self._channel = None
        self._service_uniq_code = None
        self._tnt_inst_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAicsDtcontrolVisitorqueueQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


