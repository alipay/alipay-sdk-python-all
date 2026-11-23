#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPointTaskNotifyModel(object):

    def __init__(self):
        self._chinfo = None
        self._idp_biz_no = None
        self._open_id = None
        self._order_no = None
        self._scene = None
        self._task_value = None
        self._user_id = None

    @property
    def chinfo(self):
        return self._chinfo

    @chinfo.setter
    def chinfo(self, value):
        self._chinfo = value
    @property
    def idp_biz_no(self):
        return self._idp_biz_no

    @idp_biz_no.setter
    def idp_biz_no(self, value):
        self._idp_biz_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def task_value(self):
        return self._task_value

    @task_value.setter
    def task_value(self, value):
        self._task_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.chinfo:
            if hasattr(self.chinfo, 'to_alipay_dict'):
                params['chinfo'] = self.chinfo.to_alipay_dict()
            else:
                params['chinfo'] = self.chinfo
        if self.idp_biz_no:
            if hasattr(self.idp_biz_no, 'to_alipay_dict'):
                params['idp_biz_no'] = self.idp_biz_no.to_alipay_dict()
            else:
                params['idp_biz_no'] = self.idp_biz_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.task_value:
            if hasattr(self.task_value, 'to_alipay_dict'):
                params['task_value'] = self.task_value.to_alipay_dict()
            else:
                params['task_value'] = self.task_value
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
        o = AlipayCommerceAcommunicationPointTaskNotifyModel()
        if 'chinfo' in d:
            o.chinfo = d['chinfo']
        if 'idp_biz_no' in d:
            o.idp_biz_no = d['idp_biz_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'task_value' in d:
            o.task_value = d['task_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


