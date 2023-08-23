#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReceiveInfoDto import ReceiveInfoDto


class PoBillableInfoDto(object):

    def __init__(self):
        self._is_abroad = None
        self._is_current_buyer = None
        self._po_no = None
        self._receive_info = None

    @property
    def is_abroad(self):
        return self._is_abroad

    @is_abroad.setter
    def is_abroad(self, value):
        self._is_abroad = value
    @property
    def is_current_buyer(self):
        return self._is_current_buyer

    @is_current_buyer.setter
    def is_current_buyer(self, value):
        self._is_current_buyer = value
    @property
    def po_no(self):
        return self._po_no

    @po_no.setter
    def po_no(self, value):
        self._po_no = value
    @property
    def receive_info(self):
        return self._receive_info

    @receive_info.setter
    def receive_info(self, value):
        if isinstance(value, ReceiveInfoDto):
            self._receive_info = value
        else:
            self._receive_info = ReceiveInfoDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.is_abroad:
            if hasattr(self.is_abroad, 'to_alipay_dict'):
                params['is_abroad'] = self.is_abroad.to_alipay_dict()
            else:
                params['is_abroad'] = self.is_abroad
        if self.is_current_buyer:
            if hasattr(self.is_current_buyer, 'to_alipay_dict'):
                params['is_current_buyer'] = self.is_current_buyer.to_alipay_dict()
            else:
                params['is_current_buyer'] = self.is_current_buyer
        if self.po_no:
            if hasattr(self.po_no, 'to_alipay_dict'):
                params['po_no'] = self.po_no.to_alipay_dict()
            else:
                params['po_no'] = self.po_no
        if self.receive_info:
            if hasattr(self.receive_info, 'to_alipay_dict'):
                params['receive_info'] = self.receive_info.to_alipay_dict()
            else:
                params['receive_info'] = self.receive_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PoBillableInfoDto()
        if 'is_abroad' in d:
            o.is_abroad = d['is_abroad']
        if 'is_current_buyer' in d:
            o.is_current_buyer = d['is_current_buyer']
        if 'po_no' in d:
            o.po_no = d['po_no']
        if 'receive_info' in d:
            o.receive_info = d['receive_info']
        return o


