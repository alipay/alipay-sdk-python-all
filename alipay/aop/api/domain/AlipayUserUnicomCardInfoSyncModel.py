#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserUnicomCardInfoSyncModel(object):

    def __init__(self):
        self._gmt_status_change = None
        self._phone_no = None
        self._phone_no_status = None
        self._user_id = None

    @property
    def gmt_status_change(self):
        return self._gmt_status_change

    @gmt_status_change.setter
    def gmt_status_change(self, value):
        self._gmt_status_change = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def phone_no_status(self):
        return self._phone_no_status

    @phone_no_status.setter
    def phone_no_status(self, value):
        self._phone_no_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_status_change:
            if hasattr(self.gmt_status_change, 'to_alipay_dict'):
                params['gmt_status_change'] = self.gmt_status_change.to_alipay_dict()
            else:
                params['gmt_status_change'] = self.gmt_status_change
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.phone_no_status:
            if hasattr(self.phone_no_status, 'to_alipay_dict'):
                params['phone_no_status'] = self.phone_no_status.to_alipay_dict()
            else:
                params['phone_no_status'] = self.phone_no_status
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserUnicomCardInfoSyncModel()
        if 'gmt_status_change' in d:
            o.gmt_status_change = d['gmt_status_change']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'phone_no_status' in d:
            o.phone_no_status = d['phone_no_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


