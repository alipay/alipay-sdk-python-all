#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvPicvideoQueryModel(object):

    def __init__(self):
        self._request_id = None
        self._transaction_id = None
        self._type = None
        self._video_detail = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def video_detail(self):
        return self._video_detail

    @video_detail.setter
    def video_detail(self, value):
        self._video_detail = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.transaction_id:
            if hasattr(self.transaction_id, 'to_alipay_dict'):
                params['transaction_id'] = self.transaction_id.to_alipay_dict()
            else:
                params['transaction_id'] = self.transaction_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.video_detail:
            if hasattr(self.video_detail, 'to_alipay_dict'):
                params['video_detail'] = self.video_detail.to_alipay_dict()
            else:
                params['video_detail'] = self.video_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvPicvideoQueryModel()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'transaction_id' in d:
            o.transaction_id = d['transaction_id']
        if 'type' in d:
            o.type = d['type']
        if 'video_detail' in d:
            o.video_detail = d['video_detail']
        return o


