#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsOrderprintreceiptQueryModel(object):

    def __init__(self):
        self._instruction_id = None

    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.instruction_id:
            if hasattr(self.instruction_id, 'to_alipay_dict'):
                params['instruction_id'] = self.instruction_id.to_alipay_dict()
            else:
                params['instruction_id'] = self.instruction_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsOrderprintreceiptQueryModel()
        if 'instruction_id' in d:
            o.instruction_id = d['instruction_id']
        return o


