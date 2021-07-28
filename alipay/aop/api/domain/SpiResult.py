#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SpiResult(object):

    def __init__(self):
        self._biz_code = None
        self._spi_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def spi_id(self):
        return self._spi_id

    @spi_id.setter
    def spi_id(self, value):
        self._spi_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.spi_id:
            if hasattr(self.spi_id, 'to_alipay_dict'):
                params['spi_id'] = self.spi_id.to_alipay_dict()
            else:
                params['spi_id'] = self.spi_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SpiResult()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'spi_id' in d:
            o.spi_id = d['spi_id']
        return o


