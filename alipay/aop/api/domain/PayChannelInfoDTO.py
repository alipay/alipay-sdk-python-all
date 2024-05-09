#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayChannelInfoDTO(object):

    def __init__(self):
        self._asset_id = None
        self._channel_mode = None
        self._inst_id = None
        self._pay_channel_debit_credit_type = None
        self._pay_tool_type = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def channel_mode(self):
        return self._channel_mode

    @channel_mode.setter
    def channel_mode(self, value):
        self._channel_mode = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def pay_channel_debit_credit_type(self):
        return self._pay_channel_debit_credit_type

    @pay_channel_debit_credit_type.setter
    def pay_channel_debit_credit_type(self, value):
        self._pay_channel_debit_credit_type = value
    @property
    def pay_tool_type(self):
        return self._pay_tool_type

    @pay_tool_type.setter
    def pay_tool_type(self, value):
        self._pay_tool_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.channel_mode:
            if hasattr(self.channel_mode, 'to_alipay_dict'):
                params['channel_mode'] = self.channel_mode.to_alipay_dict()
            else:
                params['channel_mode'] = self.channel_mode
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.pay_channel_debit_credit_type:
            if hasattr(self.pay_channel_debit_credit_type, 'to_alipay_dict'):
                params['pay_channel_debit_credit_type'] = self.pay_channel_debit_credit_type.to_alipay_dict()
            else:
                params['pay_channel_debit_credit_type'] = self.pay_channel_debit_credit_type
        if self.pay_tool_type:
            if hasattr(self.pay_tool_type, 'to_alipay_dict'):
                params['pay_tool_type'] = self.pay_tool_type.to_alipay_dict()
            else:
                params['pay_tool_type'] = self.pay_tool_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayChannelInfoDTO()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'channel_mode' in d:
            o.channel_mode = d['channel_mode']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'pay_channel_debit_credit_type' in d:
            o.pay_channel_debit_credit_type = d['pay_channel_debit_credit_type']
        if 'pay_tool_type' in d:
            o.pay_tool_type = d['pay_tool_type']
        return o


