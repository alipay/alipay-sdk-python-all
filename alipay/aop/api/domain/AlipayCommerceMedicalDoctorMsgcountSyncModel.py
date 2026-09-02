#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalDoctorMsgcountSyncModel(object):

    def __init__(self):
        self._aq_user_id = None
        self._aq_user_open_id = None
        self._out_app_id = None
        self._out_biz_id = None
        self._un_read_count = None

    @property
    def aq_user_id(self):
        return self._aq_user_id

    @aq_user_id.setter
    def aq_user_id(self, value):
        self._aq_user_id = value
    @property
    def aq_user_open_id(self):
        return self._aq_user_open_id

    @aq_user_open_id.setter
    def aq_user_open_id(self, value):
        self._aq_user_open_id = value
    @property
    def out_app_id(self):
        return self._out_app_id

    @out_app_id.setter
    def out_app_id(self, value):
        self._out_app_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def un_read_count(self):
        return self._un_read_count

    @un_read_count.setter
    def un_read_count(self, value):
        self._un_read_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.aq_user_id:
            if hasattr(self.aq_user_id, 'to_alipay_dict'):
                params['aq_user_id'] = self.aq_user_id.to_alipay_dict()
            else:
                params['aq_user_id'] = self.aq_user_id
        if self.aq_user_open_id:
            if hasattr(self.aq_user_open_id, 'to_alipay_dict'):
                params['aq_user_open_id'] = self.aq_user_open_id.to_alipay_dict()
            else:
                params['aq_user_open_id'] = self.aq_user_open_id
        if self.out_app_id:
            if hasattr(self.out_app_id, 'to_alipay_dict'):
                params['out_app_id'] = self.out_app_id.to_alipay_dict()
            else:
                params['out_app_id'] = self.out_app_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.un_read_count:
            if hasattr(self.un_read_count, 'to_alipay_dict'):
                params['un_read_count'] = self.un_read_count.to_alipay_dict()
            else:
                params['un_read_count'] = self.un_read_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDoctorMsgcountSyncModel()
        if 'aq_user_id' in d:
            o.aq_user_id = d['aq_user_id']
        if 'aq_user_open_id' in d:
            o.aq_user_open_id = d['aq_user_open_id']
        if 'out_app_id' in d:
            o.out_app_id = d['out_app_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'un_read_count' in d:
            o.un_read_count = d['un_read_count']
        return o


