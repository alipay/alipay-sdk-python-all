#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiptBizData import ReceiptBizData


class AlipayCommerceIotReceiptSendModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._biz_data = None
        self._biztid = None
        self._pid = None
        self._smid = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        if isinstance(value, ReceiptBizData):
            self._biz_data = value
        else:
            self._biz_data = ReceiptBizData.from_alipay_dict(value)
    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value
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
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biztid:
            if hasattr(self.biztid, 'to_alipay_dict'):
                params['biztid'] = self.biztid.to_alipay_dict()
            else:
                params['biztid'] = self.biztid
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
        o = AlipayCommerceIotReceiptSendModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biztid' in d:
            o.biztid = d['biztid']
        if 'pid' in d:
            o.pid = d['pid']
        if 'smid' in d:
            o.smid = d['smid']
        return o


