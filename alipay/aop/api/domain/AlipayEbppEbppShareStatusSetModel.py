#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppEbppShareStatusSetModel(object):

    def __init__(self):
        self._open_id = None
        self._out_process_id = None
        self._process_id = None
        self._share_open_id = None
        self._share_uid = None
        self._share_user_benefit_expire = None
        self._share_user_benefit_start = None
        self._status = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_process_id(self):
        return self._out_process_id

    @out_process_id.setter
    def out_process_id(self, value):
        self._out_process_id = value
    @property
    def process_id(self):
        return self._process_id

    @process_id.setter
    def process_id(self, value):
        self._process_id = value
    @property
    def share_open_id(self):
        return self._share_open_id

    @share_open_id.setter
    def share_open_id(self, value):
        self._share_open_id = value
    @property
    def share_uid(self):
        return self._share_uid

    @share_uid.setter
    def share_uid(self, value):
        self._share_uid = value
    @property
    def share_user_benefit_expire(self):
        return self._share_user_benefit_expire

    @share_user_benefit_expire.setter
    def share_user_benefit_expire(self, value):
        self._share_user_benefit_expire = value
    @property
    def share_user_benefit_start(self):
        return self._share_user_benefit_start

    @share_user_benefit_start.setter
    def share_user_benefit_start(self, value):
        self._share_user_benefit_start = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_process_id:
            if hasattr(self.out_process_id, 'to_alipay_dict'):
                params['out_process_id'] = self.out_process_id.to_alipay_dict()
            else:
                params['out_process_id'] = self.out_process_id
        if self.process_id:
            if hasattr(self.process_id, 'to_alipay_dict'):
                params['process_id'] = self.process_id.to_alipay_dict()
            else:
                params['process_id'] = self.process_id
        if self.share_open_id:
            if hasattr(self.share_open_id, 'to_alipay_dict'):
                params['share_open_id'] = self.share_open_id.to_alipay_dict()
            else:
                params['share_open_id'] = self.share_open_id
        if self.share_uid:
            if hasattr(self.share_uid, 'to_alipay_dict'):
                params['share_uid'] = self.share_uid.to_alipay_dict()
            else:
                params['share_uid'] = self.share_uid
        if self.share_user_benefit_expire:
            if hasattr(self.share_user_benefit_expire, 'to_alipay_dict'):
                params['share_user_benefit_expire'] = self.share_user_benefit_expire.to_alipay_dict()
            else:
                params['share_user_benefit_expire'] = self.share_user_benefit_expire
        if self.share_user_benefit_start:
            if hasattr(self.share_user_benefit_start, 'to_alipay_dict'):
                params['share_user_benefit_start'] = self.share_user_benefit_start.to_alipay_dict()
            else:
                params['share_user_benefit_start'] = self.share_user_benefit_start
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayEbppEbppShareStatusSetModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_process_id' in d:
            o.out_process_id = d['out_process_id']
        if 'process_id' in d:
            o.process_id = d['process_id']
        if 'share_open_id' in d:
            o.share_open_id = d['share_open_id']
        if 'share_uid' in d:
            o.share_uid = d['share_uid']
        if 'share_user_benefit_expire' in d:
            o.share_user_benefit_expire = d['share_user_benefit_expire']
        if 'share_user_benefit_start' in d:
            o.share_user_benefit_start = d['share_user_benefit_start']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


