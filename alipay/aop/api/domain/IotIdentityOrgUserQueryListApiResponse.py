#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotIdentityOrgUserQueryApiResponse import IotIdentityOrgUserQueryApiResponse


class IotIdentityOrgUserQueryListApiResponse(object):

    def __init__(self):
        self._face_info = None

    @property
    def face_info(self):
        return self._face_info

    @face_info.setter
    def face_info(self, value):
        if isinstance(value, list):
            self._face_info = list()
            for i in value:
                if isinstance(i, IotIdentityOrgUserQueryApiResponse):
                    self._face_info.append(i)
                else:
                    self._face_info.append(IotIdentityOrgUserQueryApiResponse.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.face_info:
            if isinstance(self.face_info, list):
                for i in range(0, len(self.face_info)):
                    element = self.face_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.face_info[i] = element.to_alipay_dict()
            if hasattr(self.face_info, 'to_alipay_dict'):
                params['face_info'] = self.face_info.to_alipay_dict()
            else:
                params['face_info'] = self.face_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotIdentityOrgUserQueryListApiResponse()
        if 'face_info' in d:
            o.face_info = d['face_info']
        return o


