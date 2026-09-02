#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdShortplaypurchaseUploadModel(object):

    def __init__(self):
        self._appid = None
        self._drama_id = None
        self._open_id = None
        self._payment_time = None
        self._shortplay_amount = None
        self._shortplay_link = None
        self._trans_number = None
        self._uuid = None

    @property
    def appid(self):
        return self._appid

    @appid.setter
    def appid(self, value):
        self._appid = value
    @property
    def drama_id(self):
        return self._drama_id

    @drama_id.setter
    def drama_id(self, value):
        self._drama_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def shortplay_amount(self):
        return self._shortplay_amount

    @shortplay_amount.setter
    def shortplay_amount(self, value):
        self._shortplay_amount = value
    @property
    def shortplay_link(self):
        return self._shortplay_link

    @shortplay_link.setter
    def shortplay_link(self, value):
        self._shortplay_link = value
    @property
    def trans_number(self):
        return self._trans_number

    @trans_number.setter
    def trans_number(self, value):
        self._trans_number = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value


    def to_alipay_dict(self):
        params = dict()
        if self.appid:
            if hasattr(self.appid, 'to_alipay_dict'):
                params['appid'] = self.appid.to_alipay_dict()
            else:
                params['appid'] = self.appid
        if self.drama_id:
            if hasattr(self.drama_id, 'to_alipay_dict'):
                params['drama_id'] = self.drama_id.to_alipay_dict()
            else:
                params['drama_id'] = self.drama_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.shortplay_amount:
            if hasattr(self.shortplay_amount, 'to_alipay_dict'):
                params['shortplay_amount'] = self.shortplay_amount.to_alipay_dict()
            else:
                params['shortplay_amount'] = self.shortplay_amount
        if self.shortplay_link:
            if hasattr(self.shortplay_link, 'to_alipay_dict'):
                params['shortplay_link'] = self.shortplay_link.to_alipay_dict()
            else:
                params['shortplay_link'] = self.shortplay_link
        if self.trans_number:
            if hasattr(self.trans_number, 'to_alipay_dict'):
                params['trans_number'] = self.trans_number.to_alipay_dict()
            else:
                params['trans_number'] = self.trans_number
        if self.uuid:
            if hasattr(self.uuid, 'to_alipay_dict'):
                params['uuid'] = self.uuid.to_alipay_dict()
            else:
                params['uuid'] = self.uuid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdShortplaypurchaseUploadModel()
        if 'appid' in d:
            o.appid = d['appid']
        if 'drama_id' in d:
            o.drama_id = d['drama_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'shortplay_amount' in d:
            o.shortplay_amount = d['shortplay_amount']
        if 'shortplay_link' in d:
            o.shortplay_link = d['shortplay_link']
        if 'trans_number' in d:
            o.trans_number = d['trans_number']
        if 'uuid' in d:
            o.uuid = d['uuid']
        return o


