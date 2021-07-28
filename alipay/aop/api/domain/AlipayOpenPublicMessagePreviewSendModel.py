#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicMessageBody import PublicMessageBody


class AlipayOpenPublicMessagePreviewSendModel(object):

    def __init__(self):
        self._logon_ids = None
        self._msg_body = None

    @property
    def logon_ids(self):
        return self._logon_ids

    @logon_ids.setter
    def logon_ids(self, value):
        if isinstance(value, list):
            self._logon_ids = list()
            for i in value:
                self._logon_ids.append(i)
    @property
    def msg_body(self):
        return self._msg_body

    @msg_body.setter
    def msg_body(self, value):
        if isinstance(value, PublicMessageBody):
            self._msg_body = value
        else:
            self._msg_body = PublicMessageBody.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.logon_ids:
            if isinstance(self.logon_ids, list):
                for i in range(0, len(self.logon_ids)):
                    element = self.logon_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logon_ids[i] = element.to_alipay_dict()
            if hasattr(self.logon_ids, 'to_alipay_dict'):
                params['logon_ids'] = self.logon_ids.to_alipay_dict()
            else:
                params['logon_ids'] = self.logon_ids
        if self.msg_body:
            if hasattr(self.msg_body, 'to_alipay_dict'):
                params['msg_body'] = self.msg_body.to_alipay_dict()
            else:
                params['msg_body'] = self.msg_body
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMessagePreviewSendModel()
        if 'logon_ids' in d:
            o.logon_ids = d['logon_ids']
        if 'msg_body' in d:
            o.msg_body = d['msg_body']
        return o


