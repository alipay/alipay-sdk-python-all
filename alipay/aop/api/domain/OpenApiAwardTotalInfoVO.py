#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAwardInfo import OpenApiAwardInfo
from alipay.aop.api.domain.OpenApiAwardInfo import OpenApiAwardInfo


class OpenApiAwardTotalInfoVO(object):

    def __init__(self):
        self._invitee_info = None
        self._inviter_info = None

    @property
    def invitee_info(self):
        return self._invitee_info

    @invitee_info.setter
    def invitee_info(self, value):
        if isinstance(value, OpenApiAwardInfo):
            self._invitee_info = value
        else:
            self._invitee_info = OpenApiAwardInfo.from_alipay_dict(value)
    @property
    def inviter_info(self):
        return self._inviter_info

    @inviter_info.setter
    def inviter_info(self, value):
        if isinstance(value, OpenApiAwardInfo):
            self._inviter_info = value
        else:
            self._inviter_info = OpenApiAwardInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invitee_info:
            if hasattr(self.invitee_info, 'to_alipay_dict'):
                params['invitee_info'] = self.invitee_info.to_alipay_dict()
            else:
                params['invitee_info'] = self.invitee_info
        if self.inviter_info:
            if hasattr(self.inviter_info, 'to_alipay_dict'):
                params['inviter_info'] = self.inviter_info.to_alipay_dict()
            else:
                params['inviter_info'] = self.inviter_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiAwardTotalInfoVO()
        if 'invitee_info' in d:
            o.invitee_info = d['invitee_info']
        if 'inviter_info' in d:
            o.inviter_info = d['inviter_info']
        return o


