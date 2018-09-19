#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCardDeleteModel(object):

    def __init__(self):
        self._ext_info = None
        self._out_serial_no = None
        self._reason_code = None
        self._target_card_no = None
        self._target_card_no_type = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_serial_no(self):
        return self._out_serial_no

    @out_serial_no.setter
    def out_serial_no(self, value):
        self._out_serial_no = value
    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def target_card_no(self):
        return self._target_card_no

    @target_card_no.setter
    def target_card_no(self, value):
        self._target_card_no = value
    @property
    def target_card_no_type(self):
        return self._target_card_no_type

    @target_card_no_type.setter
    def target_card_no_type(self, value):
        self._target_card_no_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_serial_no:
            if hasattr(self.out_serial_no, 'to_alipay_dict'):
                params['out_serial_no'] = self.out_serial_no.to_alipay_dict()
            else:
                params['out_serial_no'] = self.out_serial_no
        if self.reason_code:
            if hasattr(self.reason_code, 'to_alipay_dict'):
                params['reason_code'] = self.reason_code.to_alipay_dict()
            else:
                params['reason_code'] = self.reason_code
        if self.target_card_no:
            if hasattr(self.target_card_no, 'to_alipay_dict'):
                params['target_card_no'] = self.target_card_no.to_alipay_dict()
            else:
                params['target_card_no'] = self.target_card_no
        if self.target_card_no_type:
            if hasattr(self.target_card_no_type, 'to_alipay_dict'):
                params['target_card_no_type'] = self.target_card_no_type.to_alipay_dict()
            else:
                params['target_card_no_type'] = self.target_card_no_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCardDeleteModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_serial_no' in d:
            o.out_serial_no = d['out_serial_no']
        if 'reason_code' in d:
            o.reason_code = d['reason_code']
        if 'target_card_no' in d:
            o.target_card_no = d['target_card_no']
        if 'target_card_no_type' in d:
            o.target_card_no_type = d['target_card_no_type']
        return o


