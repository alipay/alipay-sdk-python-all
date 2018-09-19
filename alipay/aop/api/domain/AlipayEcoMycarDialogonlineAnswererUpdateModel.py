#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarDialogonlineAnswererUpdateModel(object):

    def __init__(self):
        self._answer_id = None
        self._answer_status = None

    @property
    def answer_id(self):
        return self._answer_id

    @answer_id.setter
    def answer_id(self, value):
        self._answer_id = value
    @property
    def answer_status(self):
        return self._answer_status

    @answer_status.setter
    def answer_status(self, value):
        self._answer_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.answer_id:
            if hasattr(self.answer_id, 'to_alipay_dict'):
                params['answer_id'] = self.answer_id.to_alipay_dict()
            else:
                params['answer_id'] = self.answer_id
        if self.answer_status:
            if hasattr(self.answer_status, 'to_alipay_dict'):
                params['answer_status'] = self.answer_status.to_alipay_dict()
            else:
                params['answer_status'] = self.answer_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarDialogonlineAnswererUpdateModel()
        if 'answer_id' in d:
            o.answer_id = d['answer_id']
        if 'answer_status' in d:
            o.answer_status = d['answer_status']
        return o


