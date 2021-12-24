#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WriteOffProcessOrderOpenApiDTO import WriteOffProcessOrderOpenApiDTO


class AlipayBossFncGfsettleprodWriteofforderVerifyModel(object):

    def __init__(self):
        self._write_off_process_order = None

    @property
    def write_off_process_order(self):
        return self._write_off_process_order

    @write_off_process_order.setter
    def write_off_process_order(self, value):
        if isinstance(value, WriteOffProcessOrderOpenApiDTO):
            self._write_off_process_order = value
        else:
            self._write_off_process_order = WriteOffProcessOrderOpenApiDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.write_off_process_order:
            if hasattr(self.write_off_process_order, 'to_alipay_dict'):
                params['write_off_process_order'] = self.write_off_process_order.to_alipay_dict()
            else:
                params['write_off_process_order'] = self.write_off_process_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodWriteofforderVerifyModel()
        if 'write_off_process_order' in d:
            o.write_off_process_order = d['write_off_process_order']
        return o


