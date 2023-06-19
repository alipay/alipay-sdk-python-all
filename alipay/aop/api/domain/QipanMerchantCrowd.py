#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QipanMerchantCrowd(object):

    def __init__(self):
        self._apply_channel_list = None
        self._crowd_code = None
        self._crowd_desc = None
        self._crowd_name = None
        self._crowd_size = None
        self._external_crowd_code = None
        self._hidden = None
        self._processable = None
        self._status = None

    @property
    def apply_channel_list(self):
        return self._apply_channel_list

    @apply_channel_list.setter
    def apply_channel_list(self, value):
        if isinstance(value, list):
            self._apply_channel_list = list()
            for i in value:
                self._apply_channel_list.append(i)
    @property
    def crowd_code(self):
        return self._crowd_code

    @crowd_code.setter
    def crowd_code(self, value):
        self._crowd_code = value
    @property
    def crowd_desc(self):
        return self._crowd_desc

    @crowd_desc.setter
    def crowd_desc(self, value):
        self._crowd_desc = value
    @property
    def crowd_name(self):
        return self._crowd_name

    @crowd_name.setter
    def crowd_name(self, value):
        self._crowd_name = value
    @property
    def crowd_size(self):
        return self._crowd_size

    @crowd_size.setter
    def crowd_size(self, value):
        self._crowd_size = value
    @property
    def external_crowd_code(self):
        return self._external_crowd_code

    @external_crowd_code.setter
    def external_crowd_code(self, value):
        self._external_crowd_code = value
    @property
    def hidden(self):
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        self._hidden = value
    @property
    def processable(self):
        return self._processable

    @processable.setter
    def processable(self, value):
        self._processable = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_channel_list:
            if isinstance(self.apply_channel_list, list):
                for i in range(0, len(self.apply_channel_list)):
                    element = self.apply_channel_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_channel_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_channel_list, 'to_alipay_dict'):
                params['apply_channel_list'] = self.apply_channel_list.to_alipay_dict()
            else:
                params['apply_channel_list'] = self.apply_channel_list
        if self.crowd_code:
            if hasattr(self.crowd_code, 'to_alipay_dict'):
                params['crowd_code'] = self.crowd_code.to_alipay_dict()
            else:
                params['crowd_code'] = self.crowd_code
        if self.crowd_desc:
            if hasattr(self.crowd_desc, 'to_alipay_dict'):
                params['crowd_desc'] = self.crowd_desc.to_alipay_dict()
            else:
                params['crowd_desc'] = self.crowd_desc
        if self.crowd_name:
            if hasattr(self.crowd_name, 'to_alipay_dict'):
                params['crowd_name'] = self.crowd_name.to_alipay_dict()
            else:
                params['crowd_name'] = self.crowd_name
        if self.crowd_size:
            if hasattr(self.crowd_size, 'to_alipay_dict'):
                params['crowd_size'] = self.crowd_size.to_alipay_dict()
            else:
                params['crowd_size'] = self.crowd_size
        if self.external_crowd_code:
            if hasattr(self.external_crowd_code, 'to_alipay_dict'):
                params['external_crowd_code'] = self.external_crowd_code.to_alipay_dict()
            else:
                params['external_crowd_code'] = self.external_crowd_code
        if self.hidden:
            if hasattr(self.hidden, 'to_alipay_dict'):
                params['hidden'] = self.hidden.to_alipay_dict()
            else:
                params['hidden'] = self.hidden
        if self.processable:
            if hasattr(self.processable, 'to_alipay_dict'):
                params['processable'] = self.processable.to_alipay_dict()
            else:
                params['processable'] = self.processable
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
        o = QipanMerchantCrowd()
        if 'apply_channel_list' in d:
            o.apply_channel_list = d['apply_channel_list']
        if 'crowd_code' in d:
            o.crowd_code = d['crowd_code']
        if 'crowd_desc' in d:
            o.crowd_desc = d['crowd_desc']
        if 'crowd_name' in d:
            o.crowd_name = d['crowd_name']
        if 'crowd_size' in d:
            o.crowd_size = d['crowd_size']
        if 'external_crowd_code' in d:
            o.external_crowd_code = d['external_crowd_code']
        if 'hidden' in d:
            o.hidden = d['hidden']
        if 'processable' in d:
            o.processable = d['processable']
        if 'status' in d:
            o.status = d['status']
        return o


