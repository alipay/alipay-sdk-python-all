#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocOperatonconfirmOnlineModel(object):

    def __init__(self):
        self._confirm_code = None
        self._verify_event_id = None

    @property
    def confirm_code(self):
        return self._confirm_code

    @confirm_code.setter
    def confirm_code(self, value):
        self._confirm_code = value
    @property
    def verify_event_id(self):
        return self._verify_event_id

    @verify_event_id.setter
    def verify_event_id(self, value):
        self._verify_event_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_code:
            if hasattr(self.confirm_code, 'to_alipay_dict'):
                params['confirm_code'] = self.confirm_code.to_alipay_dict()
            else:
                params['confirm_code'] = self.confirm_code
        if self.verify_event_id:
            if hasattr(self.verify_event_id, 'to_alipay_dict'):
                params['verify_event_id'] = self.verify_event_id.to_alipay_dict()
            else:
                params['verify_event_id'] = self.verify_event_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocOperatonconfirmOnlineModel()
        if 'confirm_code' in d:
            o.confirm_code = d['confirm_code']
        if 'verify_event_id' in d:
            o.verify_event_id = d['verify_event_id']
        return o


