#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtLandcoreLandcoretpspDataarchivesCallbackModel(object):

    def __init__(self):
        self._data_id = None
        self._message_content = None
        self._status = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def message_content(self):
        return self._message_content

    @message_content.setter
    def message_content(self, value):
        self._message_content = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.message_content:
            if hasattr(self.message_content, 'to_alipay_dict'):
                params['message_content'] = self.message_content.to_alipay_dict()
            else:
                params['message_content'] = self.message_content
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtLandcoreLandcoretpspDataarchivesCallbackModel()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'message_content' in d:
            o.message_content = d['message_content']
        if 'status' in d:
            o.status = d['status']
        return o


