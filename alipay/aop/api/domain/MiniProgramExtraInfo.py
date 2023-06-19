#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniProgramExtraInfo(object):

    def __init__(self):
        self._mini_program_id = None

    @property
    def mini_program_id(self):
        return self._mini_program_id

    @mini_program_id.setter
    def mini_program_id(self, value):
        self._mini_program_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_program_id:
            if hasattr(self.mini_program_id, 'to_alipay_dict'):
                params['mini_program_id'] = self.mini_program_id.to_alipay_dict()
            else:
                params['mini_program_id'] = self.mini_program_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniProgramExtraInfo()
        if 'mini_program_id' in d:
            o.mini_program_id = d['mini_program_id']
        return o


