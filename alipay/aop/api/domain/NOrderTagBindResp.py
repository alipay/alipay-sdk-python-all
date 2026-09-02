#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NOrderTagBindResp(object):

    def __init__(self):
        self._bind_pic = None
        self._nfc_url = None
        self._operate_time = None
        self._operator_name = None
        self._operator_phone = None
        self._route_url = None

    @property
    def bind_pic(self):
        return self._bind_pic

    @bind_pic.setter
    def bind_pic(self, value):
        if isinstance(value, list):
            self._bind_pic = list()
            for i in value:
                self._bind_pic.append(i)
    @property
    def nfc_url(self):
        return self._nfc_url

    @nfc_url.setter
    def nfc_url(self, value):
        if isinstance(value, list):
            self._nfc_url = list()
            for i in value:
                self._nfc_url.append(i)
    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, value):
        self._operate_time = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_phone(self):
        return self._operator_phone

    @operator_phone.setter
    def operator_phone(self, value):
        self._operator_phone = value
    @property
    def route_url(self):
        return self._route_url

    @route_url.setter
    def route_url(self, value):
        if isinstance(value, list):
            self._route_url = list()
            for i in value:
                self._route_url.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bind_pic:
            if isinstance(self.bind_pic, list):
                for i in range(0, len(self.bind_pic)):
                    element = self.bind_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bind_pic[i] = element.to_alipay_dict()
            if hasattr(self.bind_pic, 'to_alipay_dict'):
                params['bind_pic'] = self.bind_pic.to_alipay_dict()
            else:
                params['bind_pic'] = self.bind_pic
        if self.nfc_url:
            if isinstance(self.nfc_url, list):
                for i in range(0, len(self.nfc_url)):
                    element = self.nfc_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.nfc_url[i] = element.to_alipay_dict()
            if hasattr(self.nfc_url, 'to_alipay_dict'):
                params['nfc_url'] = self.nfc_url.to_alipay_dict()
            else:
                params['nfc_url'] = self.nfc_url
        if self.operate_time:
            if hasattr(self.operate_time, 'to_alipay_dict'):
                params['operate_time'] = self.operate_time.to_alipay_dict()
            else:
                params['operate_time'] = self.operate_time
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.operator_phone:
            if hasattr(self.operator_phone, 'to_alipay_dict'):
                params['operator_phone'] = self.operator_phone.to_alipay_dict()
            else:
                params['operator_phone'] = self.operator_phone
        if self.route_url:
            if isinstance(self.route_url, list):
                for i in range(0, len(self.route_url)):
                    element = self.route_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.route_url[i] = element.to_alipay_dict()
            if hasattr(self.route_url, 'to_alipay_dict'):
                params['route_url'] = self.route_url.to_alipay_dict()
            else:
                params['route_url'] = self.route_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NOrderTagBindResp()
        if 'bind_pic' in d:
            o.bind_pic = d['bind_pic']
        if 'nfc_url' in d:
            o.nfc_url = d['nfc_url']
        if 'operate_time' in d:
            o.operate_time = d['operate_time']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_phone' in d:
            o.operator_phone = d['operator_phone']
        if 'route_url' in d:
            o.route_url = d['route_url']
        return o


