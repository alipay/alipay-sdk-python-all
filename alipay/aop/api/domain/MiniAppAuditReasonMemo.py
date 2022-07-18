#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppAuditReasonMemo(object):

    def __init__(self):
        self._memo = None
        self._memo_image_list = None

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def memo_image_list(self):
        return self._memo_image_list

    @memo_image_list.setter
    def memo_image_list(self, value):
        if isinstance(value, list):
            self._memo_image_list = list()
            for i in value:
                self._memo_image_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.memo_image_list:
            if isinstance(self.memo_image_list, list):
                for i in range(0, len(self.memo_image_list)):
                    element = self.memo_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.memo_image_list[i] = element.to_alipay_dict()
            if hasattr(self.memo_image_list, 'to_alipay_dict'):
                params['memo_image_list'] = self.memo_image_list.to_alipay_dict()
            else:
                params['memo_image_list'] = self.memo_image_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppAuditReasonMemo()
        if 'memo' in d:
            o.memo = d['memo']
        if 'memo_image_list' in d:
            o.memo_image_list = d['memo_image_list']
        return o


