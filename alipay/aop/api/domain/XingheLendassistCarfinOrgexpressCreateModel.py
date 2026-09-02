#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.XhExpressPostInfo import XhExpressPostInfo
from alipay.aop.api.domain.XhExpressPostInfo import XhExpressPostInfo


class XingheLendassistCarfinOrgexpressCreateModel(object):

    def __init__(self):
        self._appointment_time = None
        self._create_type = None
        self._mortgage_no = None
        self._receiver_info = None
        self._sender_info = None

    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        self._appointment_time = value
    @property
    def create_type(self):
        return self._create_type

    @create_type.setter
    def create_type(self, value):
        self._create_type = value
    @property
    def mortgage_no(self):
        return self._mortgage_no

    @mortgage_no.setter
    def mortgage_no(self, value):
        self._mortgage_no = value
    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, value):
        if isinstance(value, XhExpressPostInfo):
            self._receiver_info = value
        else:
            self._receiver_info = XhExpressPostInfo.from_alipay_dict(value)
    @property
    def sender_info(self):
        return self._sender_info

    @sender_info.setter
    def sender_info(self, value):
        if isinstance(value, XhExpressPostInfo):
            self._sender_info = value
        else:
            self._sender_info = XhExpressPostInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_time:
            if hasattr(self.appointment_time, 'to_alipay_dict'):
                params['appointment_time'] = self.appointment_time.to_alipay_dict()
            else:
                params['appointment_time'] = self.appointment_time
        if self.create_type:
            if hasattr(self.create_type, 'to_alipay_dict'):
                params['create_type'] = self.create_type.to_alipay_dict()
            else:
                params['create_type'] = self.create_type
        if self.mortgage_no:
            if hasattr(self.mortgage_no, 'to_alipay_dict'):
                params['mortgage_no'] = self.mortgage_no.to_alipay_dict()
            else:
                params['mortgage_no'] = self.mortgage_no
        if self.receiver_info:
            if hasattr(self.receiver_info, 'to_alipay_dict'):
                params['receiver_info'] = self.receiver_info.to_alipay_dict()
            else:
                params['receiver_info'] = self.receiver_info
        if self.sender_info:
            if hasattr(self.sender_info, 'to_alipay_dict'):
                params['sender_info'] = self.sender_info.to_alipay_dict()
            else:
                params['sender_info'] = self.sender_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistCarfinOrgexpressCreateModel()
        if 'appointment_time' in d:
            o.appointment_time = d['appointment_time']
        if 'create_type' in d:
            o.create_type = d['create_type']
        if 'mortgage_no' in d:
            o.mortgage_no = d['mortgage_no']
        if 'receiver_info' in d:
            o.receiver_info = d['receiver_info']
        if 'sender_info' in d:
            o.sender_info = d['sender_info']
        return o


