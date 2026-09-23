#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalReportBroadcastNotifyModel(object):

    def __init__(self):
        self._alipay_user = None
        self._aq_user = None
        self._biz_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._out_biz_id = None
        self._status = None

    @property
    def alipay_user(self):
        return self._alipay_user

    @alipay_user.setter
    def alipay_user(self, value):
        self._alipay_user = value
    @property
    def aq_user(self):
        return self._aq_user

    @aq_user.setter
    def aq_user(self, value):
        self._aq_user = value
    @property
    def biz_info(self):
        return self._biz_info

    @biz_info.setter
    def biz_info(self, value):
        self._biz_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user:
            if hasattr(self.alipay_user, 'to_alipay_dict'):
                params['alipay_user'] = self.alipay_user.to_alipay_dict()
            else:
                params['alipay_user'] = self.alipay_user
        if self.aq_user:
            if hasattr(self.aq_user, 'to_alipay_dict'):
                params['aq_user'] = self.aq_user.to_alipay_dict()
            else:
                params['aq_user'] = self.aq_user
        if self.biz_info:
            if hasattr(self.biz_info, 'to_alipay_dict'):
                params['biz_info'] = self.biz_info.to_alipay_dict()
            else:
                params['biz_info'] = self.biz_info
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalReportBroadcastNotifyModel()
        if 'alipay_user' in d:
            o.alipay_user = d['alipay_user']
        if 'aq_user' in d:
            o.aq_user = d['aq_user']
        if 'biz_info' in d:
            o.biz_info = d['biz_info']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'status' in d:
            o.status = d['status']
        return o


