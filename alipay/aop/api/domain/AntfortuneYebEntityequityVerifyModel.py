#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LinkMallCallBackInfo import LinkMallCallBackInfo


class AntfortuneYebEntityequityVerifyModel(object):

    def __init__(self):
        self._appid = None
        self._info = None
        self._signature = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        if isinstance(value, LinkMallCallBackInfo):
            self._info = value
        else:
            self._info = LinkMallCallBackInfo.from_alipay_dict(value)
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.info:
            if hasattr(self.info, 'to_alipay_dict'):
                params['info'] = self.info.to_alipay_dict()
            else:
                params['info'] = self.info
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneYebEntityequityVerifyModel()
        if 'appid' in d:
            o.appid = d['appid']
        if 'info' in d:
            o.info = d['info']
        if 'signature' in d:
            o.signature = d['signature']
        return o


