#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NotaryResultDTO(object):

    def __init__(self):
        self._content = None
        self._gmt_create = None
        self._status = None
        self._sync_chain_time = None
        self._tx_hash = None
        self._type = None
        self._url = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sync_chain_time(self):
        return self._sync_chain_time

    @sync_chain_time.setter
    def sync_chain_time(self, value):
        self._sync_chain_time = value
    @property
    def tx_hash(self):
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, value):
        self._tx_hash = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sync_chain_time:
            if hasattr(self.sync_chain_time, 'to_alipay_dict'):
                params['sync_chain_time'] = self.sync_chain_time.to_alipay_dict()
            else:
                params['sync_chain_time'] = self.sync_chain_time
        if self.tx_hash:
            if hasattr(self.tx_hash, 'to_alipay_dict'):
                params['tx_hash'] = self.tx_hash.to_alipay_dict()
            else:
                params['tx_hash'] = self.tx_hash
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NotaryResultDTO()
        if 'content' in d:
            o.content = d['content']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'status' in d:
            o.status = d['status']
        if 'sync_chain_time' in d:
            o.sync_chain_time = d['sync_chain_time']
        if 'tx_hash' in d:
            o.tx_hash = d['tx_hash']
        if 'type' in d:
            o.type = d['type']
        if 'url' in d:
            o.url = d['url']
        return o


