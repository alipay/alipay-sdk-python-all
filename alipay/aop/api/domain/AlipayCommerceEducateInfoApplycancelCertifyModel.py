#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateInfoApplycancelCertifyModel(object):

    def __init__(self):
        self._cause_code = None
        self._cause_msg = None
        self._extend_info = None
        self._participant_id = None
        self._source_id = None

    @property
    def cause_code(self):
        return self._cause_code

    @cause_code.setter
    def cause_code(self, value):
        self._cause_code = value
    @property
    def cause_msg(self):
        return self._cause_msg

    @cause_msg.setter
    def cause_msg(self, value):
        self._cause_msg = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cause_code:
            if hasattr(self.cause_code, 'to_alipay_dict'):
                params['cause_code'] = self.cause_code.to_alipay_dict()
            else:
                params['cause_code'] = self.cause_code
        if self.cause_msg:
            if hasattr(self.cause_msg, 'to_alipay_dict'):
                params['cause_msg'] = self.cause_msg.to_alipay_dict()
            else:
                params['cause_msg'] = self.cause_msg
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateInfoApplycancelCertifyModel()
        if 'cause_code' in d:
            o.cause_code = d['cause_code']
        if 'cause_msg' in d:
            o.cause_msg = d['cause_msg']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


