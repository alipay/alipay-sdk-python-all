#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialQuestionnareTaskQueryModel(object):

    def __init__(self):
        self._channel_type = None
        self._ext_info = None
        self._qstn_id = None

    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def qstn_id(self):
        return self._qstn_id

    @qstn_id.setter
    def qstn_id(self, value):
        self._qstn_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.qstn_id:
            if hasattr(self.qstn_id, 'to_alipay_dict'):
                params['qstn_id'] = self.qstn_id.to_alipay_dict()
            else:
                params['qstn_id'] = self.qstn_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialQuestionnareTaskQueryModel()
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'qstn_id' in d:
            o.qstn_id = d['qstn_id']
        return o


