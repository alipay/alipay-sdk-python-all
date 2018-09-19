#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMarketingDataMessageDeliverModel(object):

    def __init__(self):
        self._content = None
        self._ext_info = None
        self._msg_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def msg_type(self):
        return self._msg_type

    @msg_type.setter
    def msg_type(self, value):
        self._msg_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.msg_type:
            if hasattr(self.msg_type, 'to_alipay_dict'):
                params['msg_type'] = self.msg_type.to_alipay_dict()
            else:
                params['msg_type'] = self.msg_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMarketingDataMessageDeliverModel()
        if 'content' in d:
            o.content = d['content']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'msg_type' in d:
            o.msg_type = d['msg_type']
        return o


