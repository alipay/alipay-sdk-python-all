#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DepositRuleBizParam(object):

    def __init__(self):
        self._need_send_inner_msg = None

    @property
    def need_send_inner_msg(self):
        return self._need_send_inner_msg

    @need_send_inner_msg.setter
    def need_send_inner_msg(self, value):
        self._need_send_inner_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_send_inner_msg:
            if hasattr(self.need_send_inner_msg, 'to_alipay_dict'):
                params['need_send_inner_msg'] = self.need_send_inner_msg.to_alipay_dict()
            else:
                params['need_send_inner_msg'] = self.need_send_inner_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DepositRuleBizParam()
        if 'need_send_inner_msg' in d:
            o.need_send_inner_msg = d['need_send_inner_msg']
        return o


