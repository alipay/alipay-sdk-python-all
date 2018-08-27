#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozAuthenticationCustomerSmilepayInitializeModel(object):

    def __init__(self):
        self._zimmetainfo = None

    @property
    def zimmetainfo(self):
        return self._zimmetainfo

    @zimmetainfo.setter
    def zimmetainfo(self, value):
        self._zimmetainfo = value


    def to_alipay_dict(self):
        params = dict()
        if self.zimmetainfo:
            if hasattr(self.zimmetainfo, 'to_alipay_dict'):
                params['zimmetainfo'] = self.zimmetainfo.to_alipay_dict()
            else:
                params['zimmetainfo'] = self.zimmetainfo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozAuthenticationCustomerSmilepayInitializeModel()
        if 'zimmetainfo' in d:
            o.zimmetainfo = d['zimmetainfo']
        return o


