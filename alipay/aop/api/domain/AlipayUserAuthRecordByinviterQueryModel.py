#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthRecordByinviterQueryModel(object):

    def __init__(self):
        self._check_expire = None
        self._invited_id = None
        self._invited_openid = None
        self._invited_status = None
        self._inviter_id = None
        self._inviter_openid = None
        self._inviter_status = None
        self._page_num = None
        self._page_size = None
        self._scene_id = None

    @property
    def check_expire(self):
        return self._check_expire

    @check_expire.setter
    def check_expire(self, value):
        self._check_expire = value
    @property
    def invited_id(self):
        return self._invited_id

    @invited_id.setter
    def invited_id(self, value):
        self._invited_id = value
    @property
    def invited_openid(self):
        return self._invited_openid

    @invited_openid.setter
    def invited_openid(self, value):
        self._invited_openid = value
    @property
    def invited_status(self):
        return self._invited_status

    @invited_status.setter
    def invited_status(self, value):
        if isinstance(value, list):
            self._invited_status = list()
            for i in value:
                self._invited_status.append(i)
    @property
    def inviter_id(self):
        return self._inviter_id

    @inviter_id.setter
    def inviter_id(self, value):
        self._inviter_id = value
    @property
    def inviter_openid(self):
        return self._inviter_openid

    @inviter_openid.setter
    def inviter_openid(self, value):
        self._inviter_openid = value
    @property
    def inviter_status(self):
        return self._inviter_status

    @inviter_status.setter
    def inviter_status(self, value):
        if isinstance(value, list):
            self._inviter_status = list()
            for i in value:
                self._inviter_status.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_expire:
            if hasattr(self.check_expire, 'to_alipay_dict'):
                params['check_expire'] = self.check_expire.to_alipay_dict()
            else:
                params['check_expire'] = self.check_expire
        if self.invited_id:
            if hasattr(self.invited_id, 'to_alipay_dict'):
                params['invited_id'] = self.invited_id.to_alipay_dict()
            else:
                params['invited_id'] = self.invited_id
        if self.invited_openid:
            if hasattr(self.invited_openid, 'to_alipay_dict'):
                params['invited_openid'] = self.invited_openid.to_alipay_dict()
            else:
                params['invited_openid'] = self.invited_openid
        if self.invited_status:
            if isinstance(self.invited_status, list):
                for i in range(0, len(self.invited_status)):
                    element = self.invited_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invited_status[i] = element.to_alipay_dict()
            if hasattr(self.invited_status, 'to_alipay_dict'):
                params['invited_status'] = self.invited_status.to_alipay_dict()
            else:
                params['invited_status'] = self.invited_status
        if self.inviter_id:
            if hasattr(self.inviter_id, 'to_alipay_dict'):
                params['inviter_id'] = self.inviter_id.to_alipay_dict()
            else:
                params['inviter_id'] = self.inviter_id
        if self.inviter_openid:
            if hasattr(self.inviter_openid, 'to_alipay_dict'):
                params['inviter_openid'] = self.inviter_openid.to_alipay_dict()
            else:
                params['inviter_openid'] = self.inviter_openid
        if self.inviter_status:
            if isinstance(self.inviter_status, list):
                for i in range(0, len(self.inviter_status)):
                    element = self.inviter_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inviter_status[i] = element.to_alipay_dict()
            if hasattr(self.inviter_status, 'to_alipay_dict'):
                params['inviter_status'] = self.inviter_status.to_alipay_dict()
            else:
                params['inviter_status'] = self.inviter_status
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthRecordByinviterQueryModel()
        if 'check_expire' in d:
            o.check_expire = d['check_expire']
        if 'invited_id' in d:
            o.invited_id = d['invited_id']
        if 'invited_openid' in d:
            o.invited_openid = d['invited_openid']
        if 'invited_status' in d:
            o.invited_status = d['invited_status']
        if 'inviter_id' in d:
            o.inviter_id = d['inviter_id']
        if 'inviter_openid' in d:
            o.inviter_openid = d['inviter_openid']
        if 'inviter_status' in d:
            o.inviter_status = d['inviter_status']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        return o


