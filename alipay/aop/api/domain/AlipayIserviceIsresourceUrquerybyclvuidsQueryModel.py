#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUrquerybyclvuidsQueryModel(object):

    def __init__(self):
        self._clv_user_ids = None

    @property
    def clv_user_ids(self):
        return self._clv_user_ids

    @clv_user_ids.setter
    def clv_user_ids(self, value):
        if isinstance(value, list):
            self._clv_user_ids = list()
            for i in value:
                self._clv_user_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.clv_user_ids:
            if isinstance(self.clv_user_ids, list):
                for i in range(0, len(self.clv_user_ids)):
                    element = self.clv_user_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clv_user_ids[i] = element.to_alipay_dict()
            if hasattr(self.clv_user_ids, 'to_alipay_dict'):
                params['clv_user_ids'] = self.clv_user_ids.to_alipay_dict()
            else:
                params['clv_user_ids'] = self.clv_user_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceUrquerybyclvuidsQueryModel()
        if 'clv_user_ids' in d:
            o.clv_user_ids = d['clv_user_ids']
        return o


