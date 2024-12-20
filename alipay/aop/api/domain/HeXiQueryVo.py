#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HeXiQueryVo(object):

    def __init__(self):
        self._db_mode = None

    @property
    def db_mode(self):
        return self._db_mode

    @db_mode.setter
    def db_mode(self, value):
        self._db_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.db_mode:
            if hasattr(self.db_mode, 'to_alipay_dict'):
                params['db_mode'] = self.db_mode.to_alipay_dict()
            else:
                params['db_mode'] = self.db_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HeXiQueryVo()
        if 'db_mode' in d:
            o.db_mode = d['db_mode']
        return o


