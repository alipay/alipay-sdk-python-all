#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PushChannelDTO import PushChannelDTO


class AlipayCommerceMedicalMsgReachSendModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._alipay_user_open_id = None
        self._biz_type = None
        self._msg_id = None
        self._msg_template_code = None
        self._out_biz_no = None
        self._push_channel = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def alipay_user_open_id(self):
        return self._alipay_user_open_id

    @alipay_user_open_id.setter
    def alipay_user_open_id(self, value):
        self._alipay_user_open_id = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def msg_template_code(self):
        return self._msg_template_code

    @msg_template_code.setter
    def msg_template_code(self, value):
        self._msg_template_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def push_channel(self):
        return self._push_channel

    @push_channel.setter
    def push_channel(self, value):
        if isinstance(value, PushChannelDTO):
            self._push_channel = value
        else:
            self._push_channel = PushChannelDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.alipay_user_open_id:
            if hasattr(self.alipay_user_open_id, 'to_alipay_dict'):
                params['alipay_user_open_id'] = self.alipay_user_open_id.to_alipay_dict()
            else:
                params['alipay_user_open_id'] = self.alipay_user_open_id
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.msg_template_code:
            if hasattr(self.msg_template_code, 'to_alipay_dict'):
                params['msg_template_code'] = self.msg_template_code.to_alipay_dict()
            else:
                params['msg_template_code'] = self.msg_template_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.push_channel:
            if hasattr(self.push_channel, 'to_alipay_dict'):
                params['push_channel'] = self.push_channel.to_alipay_dict()
            else:
                params['push_channel'] = self.push_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMsgReachSendModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'alipay_user_open_id' in d:
            o.alipay_user_open_id = d['alipay_user_open_id']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'msg_template_code' in d:
            o.msg_template_code = d['msg_template_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'push_channel' in d:
            o.push_channel = d['push_channel']
        return o


