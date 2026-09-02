#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserRoleNoteSendcallbackModel(object):

    def __init__(self):
        self._note_callback_type = None
        self._note_detail = None
        self._note_req_params = None
        self._note_task_id = None

    @property
    def note_callback_type(self):
        return self._note_callback_type

    @note_callback_type.setter
    def note_callback_type(self, value):
        self._note_callback_type = value
    @property
    def note_detail(self):
        return self._note_detail

    @note_detail.setter
    def note_detail(self, value):
        self._note_detail = value
    @property
    def note_req_params(self):
        return self._note_req_params

    @note_req_params.setter
    def note_req_params(self, value):
        self._note_req_params = value
    @property
    def note_task_id(self):
        return self._note_task_id

    @note_task_id.setter
    def note_task_id(self, value):
        self._note_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.note_callback_type:
            if hasattr(self.note_callback_type, 'to_alipay_dict'):
                params['note_callback_type'] = self.note_callback_type.to_alipay_dict()
            else:
                params['note_callback_type'] = self.note_callback_type
        if self.note_detail:
            if hasattr(self.note_detail, 'to_alipay_dict'):
                params['note_detail'] = self.note_detail.to_alipay_dict()
            else:
                params['note_detail'] = self.note_detail
        if self.note_req_params:
            if hasattr(self.note_req_params, 'to_alipay_dict'):
                params['note_req_params'] = self.note_req_params.to_alipay_dict()
            else:
                params['note_req_params'] = self.note_req_params
        if self.note_task_id:
            if hasattr(self.note_task_id, 'to_alipay_dict'):
                params['note_task_id'] = self.note_task_id.to_alipay_dict()
            else:
                params['note_task_id'] = self.note_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserRoleNoteSendcallbackModel()
        if 'note_callback_type' in d:
            o.note_callback_type = d['note_callback_type']
        if 'note_detail' in d:
            o.note_detail = d['note_detail']
        if 'note_req_params' in d:
            o.note_req_params = d['note_req_params']
        if 'note_task_id' in d:
            o.note_task_id = d['note_task_id']
        return o


