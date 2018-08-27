#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicMessageQueryModel(object):

    def __init__(self):
        self._message_ids = None

    @property
    def message_ids(self):
        return self._message_ids

    @message_ids.setter
    def message_ids(self, value):
        if isinstance(value, list):
            self._message_ids = list()
            for i in value:
                self._message_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.message_ids:
            if isinstance(self.message_ids, list):
                for i in range(0, len(self.message_ids)):
                    element = self.message_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.message_ids[i] = element.to_alipay_dict()
            if hasattr(self.message_ids, 'to_alipay_dict'):
                params['message_ids'] = self.message_ids.to_alipay_dict()
            else:
                params['message_ids'] = self.message_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMessageQueryModel()
        if 'message_ids' in d:
            o.message_ids = d['message_ids']
        return o


