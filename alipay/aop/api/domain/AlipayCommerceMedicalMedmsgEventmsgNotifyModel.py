#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalMedmsgArg import MedicalMedmsgArg


class AlipayCommerceMedicalMedmsgEventmsgNotifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_source = None
        self._event_type = None
        self._medical_medmsg_arg = None
        self._msg_create_time = None
        self._msg_id = None
        self._open_id = None
        self._push = None
        self._to_user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def medical_medmsg_arg(self):
        return self._medical_medmsg_arg

    @medical_medmsg_arg.setter
    def medical_medmsg_arg(self, value):
        if isinstance(value, list):
            self._medical_medmsg_arg = list()
            for i in value:
                if isinstance(i, MedicalMedmsgArg):
                    self._medical_medmsg_arg.append(i)
                else:
                    self._medical_medmsg_arg.append(MedicalMedmsgArg.from_alipay_dict(i))
    @property
    def msg_create_time(self):
        return self._msg_create_time

    @msg_create_time.setter
    def msg_create_time(self, value):
        self._msg_create_time = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def push(self):
        return self._push

    @push.setter
    def push(self, value):
        self._push = value
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.medical_medmsg_arg:
            if isinstance(self.medical_medmsg_arg, list):
                for i in range(0, len(self.medical_medmsg_arg)):
                    element = self.medical_medmsg_arg[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_medmsg_arg[i] = element.to_alipay_dict()
            if hasattr(self.medical_medmsg_arg, 'to_alipay_dict'):
                params['medical_medmsg_arg'] = self.medical_medmsg_arg.to_alipay_dict()
            else:
                params['medical_medmsg_arg'] = self.medical_medmsg_arg
        if self.msg_create_time:
            if hasattr(self.msg_create_time, 'to_alipay_dict'):
                params['msg_create_time'] = self.msg_create_time.to_alipay_dict()
            else:
                params['msg_create_time'] = self.msg_create_time
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.push:
            if hasattr(self.push, 'to_alipay_dict'):
                params['push'] = self.push.to_alipay_dict()
            else:
                params['push'] = self.push
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalMedmsgEventmsgNotifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'medical_medmsg_arg' in d:
            o.medical_medmsg_arg = d['medical_medmsg_arg']
        if 'msg_create_time' in d:
            o.msg_create_time = d['msg_create_time']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'push' in d:
            o.push = d['push']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


