#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppOpenidOpenidtounionidBatchqueryModel(object):

    def __init__(self):
        self._open_id_list = None

    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppOpenidOpenidtounionidBatchqueryModel()
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        return o


