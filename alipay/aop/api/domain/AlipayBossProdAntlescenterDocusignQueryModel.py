#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossProdAntlescenterDocusignQueryModel(object):

    def __init__(self):
        self._sign_task_request_id = None

    @property
    def sign_task_request_id(self):
        return self._sign_task_request_id

    @sign_task_request_id.setter
    def sign_task_request_id(self, value):
        self._sign_task_request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_task_request_id:
            if hasattr(self.sign_task_request_id, 'to_alipay_dict'):
                params['sign_task_request_id'] = self.sign_task_request_id.to_alipay_dict()
            else:
                params['sign_task_request_id'] = self.sign_task_request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdAntlescenterDocusignQueryModel()
        if 'sign_task_request_id' in d:
            o.sign_task_request_id = d['sign_task_request_id']
        return o


