#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditContractBorrowInitializeModel(object):

    def __init__(self):
        self._callback_url = None
        self._category = None
        self._ext = None
        self._isv_mode = None
        self._mode = None
        self._notify_addr = None
        self._out_trans_no = None
        self._qr_code = None
        self._service_id = None

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def isv_mode(self):
        return self._isv_mode

    @isv_mode.setter
    def isv_mode(self, value):
        self._isv_mode = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def notify_addr(self):
        return self._notify_addr

    @notify_addr.setter
    def notify_addr(self, value):
        if isinstance(value, list):
            self._notify_addr = list()
            for i in value:
                self._notify_addr.append(i)
    @property
    def out_trans_no(self):
        return self._out_trans_no

    @out_trans_no.setter
    def out_trans_no(self, value):
        self._out_trans_no = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.isv_mode:
            if hasattr(self.isv_mode, 'to_alipay_dict'):
                params['isv_mode'] = self.isv_mode.to_alipay_dict()
            else:
                params['isv_mode'] = self.isv_mode
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.notify_addr:
            if isinstance(self.notify_addr, list):
                for i in range(0, len(self.notify_addr)):
                    element = self.notify_addr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.notify_addr[i] = element.to_alipay_dict()
            if hasattr(self.notify_addr, 'to_alipay_dict'):
                params['notify_addr'] = self.notify_addr.to_alipay_dict()
            else:
                params['notify_addr'] = self.notify_addr
        if self.out_trans_no:
            if hasattr(self.out_trans_no, 'to_alipay_dict'):
                params['out_trans_no'] = self.out_trans_no.to_alipay_dict()
            else:
                params['out_trans_no'] = self.out_trans_no
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditContractBorrowInitializeModel()
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'category' in d:
            o.category = d['category']
        if 'ext' in d:
            o.ext = d['ext']
        if 'isv_mode' in d:
            o.isv_mode = d['isv_mode']
        if 'mode' in d:
            o.mode = d['mode']
        if 'notify_addr' in d:
            o.notify_addr = d['notify_addr']
        if 'out_trans_no' in d:
            o.out_trans_no = d['out_trans_no']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'service_id' in d:
            o.service_id = d['service_id']
        return o


