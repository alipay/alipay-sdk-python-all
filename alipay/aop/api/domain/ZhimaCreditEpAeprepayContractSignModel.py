#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAeprepayContractSignModel(object):

    def __init__(self):
        self._alipay_uid = None
        self._havana_id = None
        self._open_id = None
        self._seller_login_id = None

    @property
    def alipay_uid(self):
        return self._alipay_uid

    @alipay_uid.setter
    def alipay_uid(self, value):
        self._alipay_uid = value
    @property
    def havana_id(self):
        return self._havana_id

    @havana_id.setter
    def havana_id(self, value):
        self._havana_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def seller_login_id(self):
        return self._seller_login_id

    @seller_login_id.setter
    def seller_login_id(self, value):
        self._seller_login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_uid:
            if hasattr(self.alipay_uid, 'to_alipay_dict'):
                params['alipay_uid'] = self.alipay_uid.to_alipay_dict()
            else:
                params['alipay_uid'] = self.alipay_uid
        if self.havana_id:
            if hasattr(self.havana_id, 'to_alipay_dict'):
                params['havana_id'] = self.havana_id.to_alipay_dict()
            else:
                params['havana_id'] = self.havana_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.seller_login_id:
            if hasattr(self.seller_login_id, 'to_alipay_dict'):
                params['seller_login_id'] = self.seller_login_id.to_alipay_dict()
            else:
                params['seller_login_id'] = self.seller_login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAeprepayContractSignModel()
        if 'alipay_uid' in d:
            o.alipay_uid = d['alipay_uid']
        if 'havana_id' in d:
            o.havana_id = d['havana_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'seller_login_id' in d:
            o.seller_login_id = d['seller_login_id']
        return o


