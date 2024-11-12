#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudHeyagentCreateModel(object):

    def __init__(self):
        self._acr = None
        self._acr_sub_biz_type = None
        self._app_name = None
        self._application_id = None
        self._biz_name = None
        self._boot_type = None
        self._open_id = None
        self._task_time_out_thres = None
        self._uid = None
        self._utdid = None

    @property
    def acr(self):
        return self._acr

    @acr.setter
    def acr(self, value):
        self._acr = value
    @property
    def acr_sub_biz_type(self):
        return self._acr_sub_biz_type

    @acr_sub_biz_type.setter
    def acr_sub_biz_type(self, value):
        self._acr_sub_biz_type = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, value):
        self._application_id = value
    @property
    def biz_name(self):
        return self._biz_name

    @biz_name.setter
    def biz_name(self, value):
        self._biz_name = value
    @property
    def boot_type(self):
        return self._boot_type

    @boot_type.setter
    def boot_type(self, value):
        self._boot_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def task_time_out_thres(self):
        return self._task_time_out_thres

    @task_time_out_thres.setter
    def task_time_out_thres(self, value):
        self._task_time_out_thres = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def utdid(self):
        return self._utdid

    @utdid.setter
    def utdid(self, value):
        self._utdid = value


    def to_alipay_dict(self):
        params = dict()
        if self.acr:
            if hasattr(self.acr, 'to_alipay_dict'):
                params['acr'] = self.acr.to_alipay_dict()
            else:
                params['acr'] = self.acr
        if self.acr_sub_biz_type:
            if hasattr(self.acr_sub_biz_type, 'to_alipay_dict'):
                params['acr_sub_biz_type'] = self.acr_sub_biz_type.to_alipay_dict()
            else:
                params['acr_sub_biz_type'] = self.acr_sub_biz_type
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.application_id:
            if hasattr(self.application_id, 'to_alipay_dict'):
                params['application_id'] = self.application_id.to_alipay_dict()
            else:
                params['application_id'] = self.application_id
        if self.biz_name:
            if hasattr(self.biz_name, 'to_alipay_dict'):
                params['biz_name'] = self.biz_name.to_alipay_dict()
            else:
                params['biz_name'] = self.biz_name
        if self.boot_type:
            if hasattr(self.boot_type, 'to_alipay_dict'):
                params['boot_type'] = self.boot_type.to_alipay_dict()
            else:
                params['boot_type'] = self.boot_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.task_time_out_thres:
            if hasattr(self.task_time_out_thres, 'to_alipay_dict'):
                params['task_time_out_thres'] = self.task_time_out_thres.to_alipay_dict()
            else:
                params['task_time_out_thres'] = self.task_time_out_thres
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.utdid:
            if hasattr(self.utdid, 'to_alipay_dict'):
                params['utdid'] = self.utdid.to_alipay_dict()
            else:
                params['utdid'] = self.utdid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudHeyagentCreateModel()
        if 'acr' in d:
            o.acr = d['acr']
        if 'acr_sub_biz_type' in d:
            o.acr_sub_biz_type = d['acr_sub_biz_type']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'application_id' in d:
            o.application_id = d['application_id']
        if 'biz_name' in d:
            o.biz_name = d['biz_name']
        if 'boot_type' in d:
            o.boot_type = d['boot_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'task_time_out_thres' in d:
            o.task_time_out_thres = d['task_time_out_thres']
        if 'uid' in d:
            o.uid = d['uid']
        if 'utdid' in d:
            o.utdid = d['utdid']
        return o


