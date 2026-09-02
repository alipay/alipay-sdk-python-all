#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfMsgSyncModel(object):

    def __init__(self):
        self._msg_app_id = None
        self._receiver_ids = None
        self._template_args = None
        self._template_id = None

    @property
    def msg_app_id(self):
        return self._msg_app_id

    @msg_app_id.setter
    def msg_app_id(self, value):
        self._msg_app_id = value
    @property
    def receiver_ids(self):
        return self._receiver_ids

    @receiver_ids.setter
    def receiver_ids(self, value):
        if isinstance(value, list):
            self._receiver_ids = list()
            for i in value:
                self._receiver_ids.append(i)
    @property
    def template_args(self):
        return self._template_args

    @template_args.setter
    def template_args(self, value):
        self._template_args = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_app_id:
            if hasattr(self.msg_app_id, 'to_alipay_dict'):
                params['msg_app_id'] = self.msg_app_id.to_alipay_dict()
            else:
                params['msg_app_id'] = self.msg_app_id
        if self.receiver_ids:
            if isinstance(self.receiver_ids, list):
                for i in range(0, len(self.receiver_ids)):
                    element = self.receiver_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.receiver_ids[i] = element.to_alipay_dict()
            if hasattr(self.receiver_ids, 'to_alipay_dict'):
                params['receiver_ids'] = self.receiver_ids.to_alipay_dict()
            else:
                params['receiver_ids'] = self.receiver_ids
        if self.template_args:
            if hasattr(self.template_args, 'to_alipay_dict'):
                params['template_args'] = self.template_args.to_alipay_dict()
            else:
                params['template_args'] = self.template_args
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfMsgSyncModel()
        if 'msg_app_id' in d:
            o.msg_app_id = d['msg_app_id']
        if 'receiver_ids' in d:
            o.receiver_ids = d['receiver_ids']
        if 'template_args' in d:
            o.template_args = d['template_args']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


