#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoTextVoiceTransferModel(object):

    def __init__(self):
        self._called_number = None
        self._out_id = None
        self._tts_code = None
        self._tts_param = None

    @property
    def called_number(self):
        return self._called_number

    @called_number.setter
    def called_number(self, value):
        self._called_number = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def tts_code(self):
        return self._tts_code

    @tts_code.setter
    def tts_code(self, value):
        self._tts_code = value
    @property
    def tts_param(self):
        return self._tts_param

    @tts_param.setter
    def tts_param(self, value):
        self._tts_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.called_number:
            if hasattr(self.called_number, 'to_alipay_dict'):
                params['called_number'] = self.called_number.to_alipay_dict()
            else:
                params['called_number'] = self.called_number
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.tts_code:
            if hasattr(self.tts_code, 'to_alipay_dict'):
                params['tts_code'] = self.tts_code.to_alipay_dict()
            else:
                params['tts_code'] = self.tts_code
        if self.tts_param:
            if hasattr(self.tts_param, 'to_alipay_dict'):
                params['tts_param'] = self.tts_param.to_alipay_dict()
            else:
                params['tts_param'] = self.tts_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoTextVoiceTransferModel()
        if 'called_number' in d:
            o.called_number = d['called_number']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'tts_code' in d:
            o.tts_code = d['tts_code']
        if 'tts_param' in d:
            o.tts_param = d['tts_param']
        return o


