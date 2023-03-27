#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppinfoModifyModel(object):

    def __init__(self):
        self._open_id_config = None

    @property
    def open_id_config(self):
        return self._open_id_config

    @open_id_config.setter
    def open_id_config(self, value):
        self._open_id_config = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id_config:
            if hasattr(self.open_id_config, 'to_alipay_dict'):
                params['open_id_config'] = self.open_id_config.to_alipay_dict()
            else:
                params['open_id_config'] = self.open_id_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppinfoModifyModel()
        if 'open_id_config' in d:
            o.open_id_config = d['open_id_config']
        return o


