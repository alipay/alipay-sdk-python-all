#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BannerInfo import BannerInfo


class AlipayCommerceIotReceiptOperationSubmitModel(object):

    def __init__(self):
        self._banner_info = None
        self._op_type = None
        self._pid = None
        self._smid = None

    @property
    def banner_info(self):
        return self._banner_info

    @banner_info.setter
    def banner_info(self, value):
        if isinstance(value, BannerInfo):
            self._banner_info = value
        else:
            self._banner_info = BannerInfo.from_alipay_dict(value)
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.banner_info:
            if hasattr(self.banner_info, 'to_alipay_dict'):
                params['banner_info'] = self.banner_info.to_alipay_dict()
            else:
                params['banner_info'] = self.banner_info
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotReceiptOperationSubmitModel()
        if 'banner_info' in d:
            o.banner_info = d['banner_info']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'pid' in d:
            o.pid = d['pid']
        if 'smid' in d:
            o.smid = d['smid']
        return o


