#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SoundInfo(object):

    def __init__(self):
        self._album_name = None
        self._audit_reject_desc = None
        self._latest_audit_status = None
        self._out_album_id = None
        self._out_sound_id = None
        self._sound_name = None
        self._sound_order = None
        self._status = None

    @property
    def album_name(self):
        return self._album_name

    @album_name.setter
    def album_name(self, value):
        self._album_name = value
    @property
    def audit_reject_desc(self):
        return self._audit_reject_desc

    @audit_reject_desc.setter
    def audit_reject_desc(self, value):
        self._audit_reject_desc = value
    @property
    def latest_audit_status(self):
        return self._latest_audit_status

    @latest_audit_status.setter
    def latest_audit_status(self, value):
        self._latest_audit_status = value
    @property
    def out_album_id(self):
        return self._out_album_id

    @out_album_id.setter
    def out_album_id(self, value):
        self._out_album_id = value
    @property
    def out_sound_id(self):
        return self._out_sound_id

    @out_sound_id.setter
    def out_sound_id(self, value):
        self._out_sound_id = value
    @property
    def sound_name(self):
        return self._sound_name

    @sound_name.setter
    def sound_name(self, value):
        self._sound_name = value
    @property
    def sound_order(self):
        return self._sound_order

    @sound_order.setter
    def sound_order(self, value):
        self._sound_order = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.album_name:
            if hasattr(self.album_name, 'to_alipay_dict'):
                params['album_name'] = self.album_name.to_alipay_dict()
            else:
                params['album_name'] = self.album_name
        if self.audit_reject_desc:
            if hasattr(self.audit_reject_desc, 'to_alipay_dict'):
                params['audit_reject_desc'] = self.audit_reject_desc.to_alipay_dict()
            else:
                params['audit_reject_desc'] = self.audit_reject_desc
        if self.latest_audit_status:
            if hasattr(self.latest_audit_status, 'to_alipay_dict'):
                params['latest_audit_status'] = self.latest_audit_status.to_alipay_dict()
            else:
                params['latest_audit_status'] = self.latest_audit_status
        if self.out_album_id:
            if hasattr(self.out_album_id, 'to_alipay_dict'):
                params['out_album_id'] = self.out_album_id.to_alipay_dict()
            else:
                params['out_album_id'] = self.out_album_id
        if self.out_sound_id:
            if hasattr(self.out_sound_id, 'to_alipay_dict'):
                params['out_sound_id'] = self.out_sound_id.to_alipay_dict()
            else:
                params['out_sound_id'] = self.out_sound_id
        if self.sound_name:
            if hasattr(self.sound_name, 'to_alipay_dict'):
                params['sound_name'] = self.sound_name.to_alipay_dict()
            else:
                params['sound_name'] = self.sound_name
        if self.sound_order:
            if hasattr(self.sound_order, 'to_alipay_dict'):
                params['sound_order'] = self.sound_order.to_alipay_dict()
            else:
                params['sound_order'] = self.sound_order
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
        o = SoundInfo()
        if 'album_name' in d:
            o.album_name = d['album_name']
        if 'audit_reject_desc' in d:
            o.audit_reject_desc = d['audit_reject_desc']
        if 'latest_audit_status' in d:
            o.latest_audit_status = d['latest_audit_status']
        if 'out_album_id' in d:
            o.out_album_id = d['out_album_id']
        if 'out_sound_id' in d:
            o.out_sound_id = d['out_sound_id']
        if 'sound_name' in d:
            o.sound_name = d['sound_name']
        if 'sound_order' in d:
            o.sound_order = d['sound_order']
        if 'status' in d:
            o.status = d['status']
        return o


