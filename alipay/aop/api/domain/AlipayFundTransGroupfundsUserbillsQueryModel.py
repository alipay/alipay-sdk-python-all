#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFundTransGroupfundsUserbillsQueryModel(object):

    def __init__(self):
        self._batch_nos = None
        self._current_user_id = None

    @property
    def batch_nos(self):
        return self._batch_nos

    @batch_nos.setter
    def batch_nos(self, value):
        if isinstance(value, list):
            self._batch_nos = list()
            for i in value:
                self._batch_nos.append(i)
    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_nos:
            if isinstance(self.batch_nos, list):
                for i in range(0, len(self.batch_nos)):
                    element = self.batch_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.batch_nos[i] = element.to_alipay_dict()
            if hasattr(self.batch_nos, 'to_alipay_dict'):
                params['batch_nos'] = self.batch_nos.to_alipay_dict()
            else:
                params['batch_nos'] = self.batch_nos
        if self.current_user_id:
            if hasattr(self.current_user_id, 'to_alipay_dict'):
                params['current_user_id'] = self.current_user_id.to_alipay_dict()
            else:
                params['current_user_id'] = self.current_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundTransGroupfundsUserbillsQueryModel()
        if 'batch_nos' in d:
            o.batch_nos = d['batch_nos']
        if 'current_user_id' in d:
            o.current_user_id = d['current_user_id']
        return o


